# data_pipeline_tool
# 📈 期貨/加密貨幣市場數據管道工具 (Market Data Pipeline Tool)

### 🎯 服務目標
本專案提供一套高效、穩健的 Python 骨架，專門用於處理和結構化高頻金融數據（期貨、加密貨幣、外匯）。協助策略開發者快速將原始數據轉換為可直接用於回測的 Pandas DataFrame 格式，解決數據清洗、重採樣和缺失值處理等常見痛點。

### ✨ 核心功能
1. **數據清洗 (Data Cleaning):** 自動處理 NaN 值和異常數據點。
2. **時間重採樣 (Resampling):** 將 Tick 數據或分鐘數據高效轉換為 5 分鐘、15 分鐘等策略K線。
3. **時間同步 (Time Synchronization):** 確保所有數據 (例如價格和成交量) 保持時間序列的一致性。
4. **向量化準備 (Vectorization Ready):** 輸出結構化的 DataFrame，適用於高性能的 NumPy/Pandas 向量化回測。

### 🛠️ 專案技術棧
* **語言：** Python 3.9+
* **核心函式庫：** Pandas, NumPy
