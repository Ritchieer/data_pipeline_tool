🚀 Market Data Pipeline Tool

High-Performance OHLCV Processing for Quantitative Research & Backtesting

This repository contains a clean, modular, and production-ready Python Market Data Pipeline designed for quantitative trading research.
It transforms raw minute-level futures/crypto data into analysis-ready, vectorized OHLCV datasets suitable for backtesting, machine learning, and systematic strategy development.

Developed by a CQF Candidate with real trading experience in MNQ/NQ micro futures, this tool reflects both practical trading needs and professional quant engineering standards.

🔧 Features
1. Raw Market Data Simulation

Generates realistic minute-level OHLCV data using a stochastic price model (random walk), including optional missing values to emulate exchange imperfections.

2. Data Cleaning

Forward-fills missing OHLC values

Replaces missing Volume with 0

Cleans malformed rows while preserving the chronological index

3. Resampling Engine

Converts 1-minute bars to 5-minute, 15-minute, or hourly OHLCV bars using optimized pandas vectorization:

Open → first

High → max

Low → min

Close → last

Volume → sum

4. Deterministic File Output

Automatically saves processed data to:

(data_pipeline_tool_root)/data/


using a stable __file__-based path resolver (works even when run from another directory).

📂 Project Structure
data_pipeline_tool/
│
├─ data_pipeline_tool/
│   ├─ src/
│   │   └─ data_processor.py     # Main pipeline script
│   └─ data/
│       └─ NQ_5min_processed.csv # Output generated after execution
│
└─ README.md

🧪 Running the Pipeline

Run from repository root:

python data_pipeline_tool/src/data_processor.py


Upon completion, you will see:

Simulation summary

Cleaning report

Resampling logs

Generated CSV located in:

data/NQ_5min_processed.csv

📊 Use Cases

This pipeline is ideal for:

Futures & crypto strategy research

Machine learning model dataset preparation

Building a clean preprocessing layer for quant workflows

Educational or portfolio projects demonstrating quant engineering

Expandable for:

Technical indicators

Live market data ingestion

Backtesting engine integration

🛠 Technology Stack

Python 3.9+

Pandas

NumPy

Modular, readable, quant-oriented architecture

📈 Planned Enhancements

Technical indicators (MA, RSI, Bollinger Bands, ATR)

MNQ strategy example (trend or volatility compression)

Monte Carlo robustness add-on

Binance / IBKR API ingestion

Unified “Quant Starter Kit” (Pipeline + Backtest + Risk Tools)

👨‍💻 About the Author
Quant Research & Python Backtesting Consultant (CQF Candidate)

MNQ / NQ / ES futures practitioner.
I help traders and developers turn trading ideas into clean, testable Python systems with:

Market data engineering

Vectorized backtesting

Risk modeling & position sizing

Strategy prototyping

📬 Contact
LinkedIn

https://www.linkedin.com/in/chih-hsiao-82558a368/

Upwork

(Coming soon — will be added once available)

⭐ Support

If you find this project useful, please consider starring the repository.

🚀 Final Note

This repository functions as both a practical tool and part of a professional quant portfolio, demonstrating capability in:

Clean code architecture

Quant workflow design

Realistic trading knowledge

Production-ready data engineering

Perfect for recruiters, quant teams, and clients evaluating technical depth.

📌 End of README
