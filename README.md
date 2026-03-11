# Bronze → Silver → Gold ETL Pipeline (PySpark + Delta Lake)

This project demonstrates a **serverless-compatible ETL pipeline** on Databricks, moving data from raw Bronze layer to a clean Silver layer, and then to an incremental Gold layer with surrogate keys. It also includes a **data generator** for testing purposes.

---

## Architecture Overview

1. **Bronze Layer**  
   - Pulls raw data files (e.g., CSV, JSON, Parquet) from source systems.  
   - Minimal transformations; only ingestion of raw data.  

2. **Silver Layer**  
   - Cleans and standardizes data from Bronze.  
   - Ensures consistent schema, handles basic data quality checks.  

3. **Gold Layer**  
   - Incremental load from Silver using `modifiedDate` watermark.  
   - Generates surrogate keys (`OrderKey`).  
   - Merges new and updated records into Gold Delta table.  
   - Maintains `create_date` and `update_date`.  
   - Compatible with **serverless compute** (avoids RDDs and unsupported functions).

4. **Data Generator**  
   - Creates synthetic data for testing and demonstration.  
   - Can generate multiple orders with random values.  
   - Supports incremental simulation by updating `modifiedDate`.  

---

## Features

- **Incremental Load:** Only new or updated rows in Silver are processed.  
- **Surrogate Key Generation:** Automatically assigns sequential `OrderKey`.  
- **Merge Logic:**  
  - Updates existing records in Gold.  
  - Inserts new records.  
- **Timestamps:** Tracks `create_date` and `update_date`.  
- **Serverless Compatible:** Avoids RDD-based operations and unsupported PySpark functions.  
- **Synthetic Data Generation:** Easily simulate new and updated records for testing.  

---

## Setup Instructions

1. Clone the repository:

```bash
git clone <repo_url>
cd <repo_name>
