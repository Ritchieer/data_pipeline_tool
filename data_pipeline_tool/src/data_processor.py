# data_pipeline_tool/src/data_processor.py

import os
from typing import Optional

import numpy as pd  # <- 假的，等一下改
import numpy as np
import pandas as pd


def simulate_raw_data(num_records: int = 1000,
                      start_time: str = "2025-12-10 09:30:00",
                      initial_price: float = 18000.0,
                      seed: Optional[int] = 44) -> pd.DataFrame:
    """
    階段 1: 模擬從 API 或交易所獲取的原始分鐘 OHLCV 數據。

    參數:
        num_records (int): 要產生幾筆 1 分鐘 K 線。
        start_time (str): 起始時間，字串會被轉成 pandas.Timestamp。
        initial_price (float): 初始價格 (第一根 Close)。
        seed (int | None): 隨機種子，None 則不固定結果。

    返回:
        pd.DataFrame: 包含時間索引的模擬 1 分鐘 OHLCV 數據。
    """
    print("--- 階段 1: 模擬原始分鐘數據 ---")

    if seed is not None:
        np.random.seed(seed)

    # 建立 1 分鐘時間索引
    start_ts = pd.to_datetime(start_time)
    time_index = pd.date_range(start=start_ts, periods=num_records, freq="1min")

    # random walk 產生 Close 價格
    price_changes = np.random.randn(num_records).cumsum() * 0.5
    close_prices = initial_price + price_changes

    df = pd.DataFrame(index=time_index)
    df["Close"] = close_prices
    df["Open"] = df["Close"].shift(1).fillna(initial_price)

    # High / Low 加一點 noise
    df["High"] = df[["Open", "Close"]].max(axis=1) + np.random.rand(num_records) * 0.2
    df["Low"] = df[["Open", "Close"]].min(axis=1) - np.random.rand(num_records) * 0.2

    # Volume: 隨機產生 + 刻意製造 5% NaN
    df["Volume"] = np.random.randint(50, 200, num_records).astype(float)

    nan_idx = df.sample(frac=0.05, random_state=seed).index
    df.loc[nan_idx, "Volume"] = np.nan

    print(f"數據記錄數: {len(df)}")
    print(f"Volume 欄位有 {df['Volume'].isna().sum()} 個 NaN (待清洗)")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    階段 2: 處理常見的金融數據缺失值 (NaN)。

    策略:
        - OHLC 使用前值填補 (forward fill)，避免中斷價格序列。
        - Volume 的 NaN 填為 0，解讀為「當下沒有成交」。

    參數:
        df (pd.DataFrame): 原始市場數據。

    返回:
        pd.DataFrame: 清洗後的數據 (會回傳新的 DataFrame，不修改原始 df)。
    """
    print("\n--- 階段 2: 數據清洗 ---")

    df_clean = df.copy()

    # 1. 處理交易數據 (OHLC) 的缺失值：使用前一個有效值填補 (ffill)
    ohlc_cols = ["Open", "High", "Low", "Close"]
    df_clean[ohlc_cols] = df_clean[ohlc_cols].ffill()

    # 2. 處理 Volume 的缺失值：填補為 0 (假設沒有交易發生)
    df_clean["Volume"] = df_clean["Volume"].fillna(0)

    print(f"清洗後 Volume 欄位 NaN 數量: {df_clean['Volume'].isna().sum()}")
    return df_clean


def resample_data(df: pd.DataFrame, freq: str = "5min") -> pd.DataFrame:
    """
    階段 3: 將分鐘數據高效地重採樣為較長時間週期 (例如 5 分鐘 K 線)。

    參數:
        df (pd.DataFrame): 清洗後的原始市場數據 (分鐘級)。
        freq (str): 目標時間週期，例如 '5min', '15min', '1H'。

    返回:
        pd.DataFrame: 重採樣後的 OHLCV 數據。
    """
    print(f"\n--- 階段 3: 數據重採樣到 {freq} K 線 ---")

    # 核心 Pandas 向量化操作
    resampled = df.resample(freq).agg(
        {
            "Open": "first",   # 該區間第一筆
            "High": "max",     # 區間最高價
            "Low": "min",      # 區間最低價
            "Close": "last",   # 區間最後一筆
            "Volume": "sum",   # 區間成交量總和
        }
    )

    # 移除任何由於市場休市導致的 NaN K 線 (Open 為 NaN 代表整段都沒有資料)
    resampled = resampled.dropna(subset=["Open"])

    # 保證欄位順序一致
    resampled = resampled[["Open", "High", "Low", "Close", "Volume"]]

    print(f"重採樣後數據記錄數: {len(resampled)}")
    return resampled


def output_data(df: pd.DataFrame,
                filename: str = "processed_futures_data.csv") -> str:
    """
    階段 4: 將最終數據輸出為 CSV 檔案，並存入 data/ 資料夾。
    這次會強制將檔案儲存在專案根目錄下。

    參數:
        df (pd.DataFrame): 要輸出的 OHLCV 數據。
        filename (str): 要輸出的檔案名稱。

    返回:
        str: 實際寫出的檔案完整路徑。
    """
    # 找到 src/data_processor.py 所在的絕對路徑
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 回退一層到專案根目錄 (data_pipeline_tool/)
    project_root = os.path.dirname(script_dir)

    output_dir = os.path.join(project_root, "data")
    os.makedirs(output_dir, exist_ok=True)

    full_path = os.path.join(output_dir, filename)
    df.to_csv(full_path)

    print("\n--- 最終輸出成功 ---")
    print(f"檔案已儲存至：{full_path}")
    print("請檢查這個路徑確認檔案生成。")

    return full_path


# --- 專案啟動點：運行整個 Pipeline ---
if __name__ == "__main__":
    # 1. 模擬原始數據
    raw_data = simulate_raw_data(num_records=1000)

    # 2. 數據清洗
    cleaned_data = clean_data(raw_data)

    # 3. 數據重採樣 (1min -> 5min)
    final_data = resample_data(cleaned_data, freq="5min")

    # 4. 數據輸出 (最終步驟)
    output_data(final_data, filename="NQ_5min_processed.csv")

    print("\nPipeline 運行完畢，您的 Market Data Pipeline 專案準備好上傳 GitHub！")
