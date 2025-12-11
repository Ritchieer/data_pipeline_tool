Market Data Pipeline Tool

High-Performance OHLCV Processing for Quantitative Research & Backtesting

This repository contains a clean, modular, and production-ready Python Market Data Pipeline designed for quantitative trading research.
It transforms raw minute-level futures/crypto data into analysis-ready, vectorized OHLCV datasets suitable for backtesting, machine learning, and systematic strategy development.

Developed by a CQF Candidate with real trading experience in MNQ/NQ micro futures, this tool reflects both practical trading needs and professional quant engineering standards.

🔧 Features
✔ 1. Raw Market Data Simulation

Generates realistic minute-level OHLCV data using stochastic price evolution (random walk), including optional missing values to emulate real-world exchange imperfections.

✔ 2. Data Cleaning

Forward-fills missing OHLC values

Replaces missing Volume with 0

Removes malformed rows while preserving time index integrity

✔ 3. Resampling Engine (1-Min → 5-Min / 15-Min / Hourly)

Produces clean resampled OHLCV bars using Pandas’ optimized vectorized operations:

Open: first

High: max

Low: min

Close: last

Volume: sum
✔ 4. Deterministic Output Path

Automatically saves output CSV files into:

(data_pipeline_tool_root)/data/


Regardless of the working directory, thanks to a robust __file__-based path resolver.
