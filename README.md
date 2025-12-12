# Market Data Pipeline Tool
High-performance OHLCV processing for quantitative research and backtesting.

This repository provides a clean and reproducible Python-based pipeline for transforming raw minute-level futures/crypto market data into analysis-ready OHLCV datasets.  
Developed by a **CQF Candidate** with real trading experience in MNQ/NQ micro futures.

---

## Features

### 1. Raw Data Simulation

- Generates realistic 1-minute OHLCV data using a random-walk model.
- Includes intentionally missing values to emulate real exchange imperfections.

### 2. Data Cleaning

- Forward-fills missing OHLC values.
- Replaces missing Volume with 0.
- Ensures index continuity for downstream analysis.

### 3. Resampling Engine

- Converts 1-minute data to 5-minute, 15-minute, or hourly bars.
- Fully vectorized Pandas operations (no loops).

Aggregation rules:

Open -> first
High -> max
Low -> min
Close -> last
Volume -> sum

### 4. Deterministic Output Path

Output CSV files are always saved under:

data_pipeline_tool/data/

regardless of the execution directory, using `__file__` to resolve paths.

---

## Project Structure
data_pipeline_tool/
│
├─ data_pipeline_tool/
│ ├─ src/
│ │ └─ data_processor.py # Main pipeline script
│ └─ data/
│ └─ NQ_5min_processed.csv # Auto-generated output
│
└─ README.md

---

## How to Run

From the project root, run:

python data_pipeline_tool/src/data_processor.py


After running, you will see:

- Simulation logs
- Cleaning summary
- Resampling summary
- Output CSV at:

data/NQ_5min_processed.csv

---

## Use Cases

This pipeline is suitable for:

- Futures & crypto strategy research
- Backtesting preparation
- Machine learning dataset generation
- Quant portfolio projects
- Teaching or demonstrating market data preprocessing

---

## Technology Stack

- Python 3.9+
- Pandas
- NumPy

Clean, modular, and quant-oriented code architecture.

---

## Planned Additions

- Technical indicators (MA, RSI, Bollinger Bands)
- MNQ strategy example (5-minute trend or volatility compression)
- Monte Carlo robustness tests
- Binance / IBKR API data ingestion
- Full Quant Starter Kit (Pipeline + Backtest + Risk Tools)

---

# About the Author

### Quant Research & Python Backtesting Consultant (CQF Candidate)

Experience includes:

- MNQ / NQ / ES futures trading
- Market data engineering
- Vectorized backtesting
- Position sizing and risk modeling

I help traders and developers convert trading ideas into **clean, testable, systematic Python workflows**.

---

## Contact

**LinkedIn:**  
https://www.linkedin.com/in/chih-hsiao-82558a368/

**Upwork:**  
(Coming soon – link will be added once available)

---

## Support

If you find this project helpful, please consider starring the repository.

---

## Final Note

This project serves as both a functional tool and part of a professional quant portfolio, demonstrating:

- Clean engineering
- Practical market understanding
- Backtesting readiness
- Reliable data workflow design
