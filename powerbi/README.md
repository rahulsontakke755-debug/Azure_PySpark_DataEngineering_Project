# Power BI Dashboard
## Overview
Power BI was used as the reporting and visualization layer for the Azure Data Engineering project.
The dashboard connects to analytics-ready Gold datasets and provides interactive analysis of learner performance, attendance, training, assessment and placement data.

## Dashboard Pages
### 1. Learner Performance & Placement Dashboard
Key visuals:
- Total Learners
- Learners by Centre
- Learners by Course
- Learners by Gender
- Attendance Status
- Assessment Result
- Placement Status
- Average Assessment Score
- Average Placement Salary

### 2. Detailed Analytics
This page provides detailed analysis of:
- Daily Attendance Trend
- Placement Status Count
- Course-wise Training Status
- Attendance by Status
- Average Salary by Placement Status
- Training Status Distribution
- Average Assessment Score by Assessment
- Placement by Company
- Learner Details

### 3. Filters & Learner Analysis
Interactive filters:
- Centre
- Course
- Gender
Analysis includes:
- Learner Count by Centre
- Learner Count by Course & Gender
- Learner Count by Gender
- Learner Status Distribution
- Average Assessment Score by Course
- Average Placement Salary by Company
- Assessment Details

## Data Model
Power BI uses dimension and fact datasets from the Gold layer.

### Dimensions
- dim_learner
- dim_centre
- dim_date

### Facts
- fact_attendance
- fact_training
- fact_assessment
- fact_placement

## Key Analytics
The dashboard provides insights into:
- Learner distribution across centres and courses
- Attendance performance
- Training status
- Assessment results and scores
- Placement status
- Placement companies
- Average placement salary
- 
## Interactive Analysis
Centre, Course and Gender slicers allow users to filter the dashboard and analyze learner performance dynamically.

## Technology
- Power BI
- Azure Databricks
- Delta Lake
- PySpark
- Azure Data Lake Storage Gen2

- ## Dashboard Screenshots

### Page 1 – Learner Performance & Placement Dashboard

![Dashboard Page 1](./screenshots/LinkedIn_Page1_Clean.jpg)

### Page 2 – Detailed Analytics

![Dashboard Page 2](./screenshots/LinkedIn_Page2_Clean.jpg)

### Page 3 – Filters & Learner Analysis

![Dashboard Page 3](./screenshots/LinkedIn_Page3_Clean.jpg)
