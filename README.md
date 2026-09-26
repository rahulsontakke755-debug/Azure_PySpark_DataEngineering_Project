# Azure PySpark Data Engineering Project
## Project Overview
End-to-end Azure Data Engineering project built using PySpark and Azure Databricks to process learner, attendance, training, assessment and placement data.

## Architecture
CSV → Azure Data Factory → ADLS Gen2 → Azure Databricks / PySpark → Bronze → Silver → Gold → Power BI

## Technologies Used
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- Auto Loader
- MERGE / Upsert
- Change Data Feed (CDF)
- Azure Event Hubs
- Structured Streaming
- Z-Ordering
- Liquid Clustering
- Power BI

## Data Processing
### Bronze Layer
- Ingested raw CSV data into ADLS Gen2.
- Used Auto Loader for incremental file ingestion.
- Stored data in Delta format.

### Silver Layer
- Data cleaning and validation
- Data type casting
- Deduplication
- Business transformations
- Joins and aggregations

### Gold Layer
- Created analytics-ready dimension and fact datasets.
- Learner, Centre and Date dimensions
- Attendance, Training, Assessment and Placement facts

## Incremental Data Processing
- Delta MERGE for upsert processing
- Change Data Feed (CDF) for tracking data changes
- Auto Loader for detecting new files
- Checkpointing to maintain processing state

## Event-Driven Processing
Azure Event Hubs was integrated with Databricks Structured Streaming for processing learner events.

## Delta Lake Optimization
- Z-Ordering
- Liquid Clustering
- OPTIMIZE
- Delta Lake ACID transactions

## Power BI
Created interactive dashboards for:
- Learner Performance
- Attendance Analysis
- Training Analysis
- Assessment Performance
- Placement Analysis
- Salary Analysis

## Project Type
Portfolio / Demo project using synthetic data.

## Key Learning
This project provided hands-on experience with Azure Data Engineering, PySpark, Databricks, Delta Lake, incremental processing, streaming and Power BI.
