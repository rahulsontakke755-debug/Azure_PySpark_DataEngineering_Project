# Azure Data Factory Pipeline Documentation
## Azure Services Used
- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Azure Databricks
- Azure Event Hubs
- Power BI

## Data Flow
CSV Source → Azure Data Factory → ADLS Gen2 → Azure Databricks / PySpark → Bronze → Silver → Gold → Power BI

## ADLS Gen2 Structure
The ADLS Gen2 storage account contains the following containers:
- source
- bronze
- silver
- gold

### Source
Contains the incoming CSV files used for data ingestion.

### Bronze
Stores raw ingested data in Delta format.

### Silver
Stores cleaned and transformed data.

### Gold
Stores analytics-ready dimension and fact datasets.

## Azure Data Factory
Azure Data Factory is used as the orchestration and ingestion layer.

### ADF Components
- Linked Service
- Datasets
- Copy Data Activity
- Pipelines
- Triggers

## Data Ingestion Process
1. CSV files are placed in the ADLS Gen2 source container.
2. Azure Data Factory connects to ADLS Gen2 using a Linked Service.
3. Datasets define the source and destination data locations.
4. Copy Data activities move source data into the Bronze layer.
5. Databricks/PySpark processes the Bronze data.
6. Cleaned data is stored in the Silver layer.
7. Analytics-ready data is stored in the Gold layer.
8. Gold data is consumed by Power BI for reporting.

## Pipeline Processing
ADF pipelines were created for ingesting the project datasets from the source location into ADLS Gen2 Bronze storage.
The pipelines cover datasets such as:
- Learners
- Centres
- Attendance
- Training
- Assessment
- Placement

## Orchestration
Azure Data Factory acts as the orchestration layer between the source data and Databricks processing.
ADF handles data movement, while Azure Databricks and PySpark handle transformation and data processing.

## Integration with Databricks
ADF and Databricks are used together in the data engineering workflow:
ADF → ADLS Gen2 → Databricks/PySpark → Delta Lake

## Security
Secrets and connection strings are not stored in the GitHub repository.
Sensitive credentials are managed through secure Azure/Databricks configuration.

## Project Architecture
Source CSV
↓
Azure Data Factory
↓
ADLS Gen2
↓
Bronze Delta
↓
Azure Databricks / PySpark
↓
Silver Delta
↓
Gold Delta
↓
Power BI
