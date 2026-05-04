# Financial News Sentiment ETL Pipeline

## 📌 Objective
An automated ETL (Extract, Transform, Load) pipeline designed to ingest financial news headlines, analyze their market sentiment using an open-source Large Language Model (LLM), and output structured data for quantitative analysis and algorithmic trading strategies.

## 🛠️ Tech Stack & Architecture
* **Language:** Python
* **Data Processing:** Pandas
* **Machine Learning / NLP:** Hugging Face `transformers`, PyTorch
* **Model:** `ProsusAI/finbert` (A pre-trained NLP model specifically fine-tuned on corporate financial text and SEC filings).
* **Environment:** Databricks / Local Python Environment

## 🔄 Pipeline Workflow

### 1. Extract
* Ingests financial news data including headlines, publishers, and UNIX timestamps. 
* *Note: The current iteration utilizes structured mock data to bypass cloud-server IP blocking from financial APIs (e.g., Yahoo Finance).*

### 2. Transform
* **Data Cleaning:** Converts raw UNIX timestamps into standard Datetime objects. 
* **AI Integration:** Deploys the FinBERT model to read each headline and classify the contextual market sentiment.
* **Logic:** The model processes the text tensor and outputs a definitive classification (`POSITIVE`, `NEGATIVE`, or `NEUTRAL`), which is appended as a new feature column.

### 3. Load
* Validates the schema and exports the enriched, AI-scored dataset into a structured `CSV` format.
* The output is formatted and ready to be ingested into a cloud data warehouse (Snowflake/PostgreSQL) or a visualization tool (Tableau).

## 🚀 How to Run Locally

**1. Install Dependencies**
Ensure you have Python installed, then run the following command to install the required libraries:
```bash
pip install pandas transformers torch