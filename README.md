# Telco Customer Churn Analysis

This repository contains the project materials for analyzing customer churn in a telecommunications company. The goal of this project is to understand the drivers of churn and provide actionable insights to improve customer retention.


## Project Overview

The project focuses on identifying key factors contributing to customer churn using advanced data analytics techniques. By leveraging the Telco Customer dataset, I built a predictive model that enables better decision-making for retention strategies.


## Key Highlights

### Data
- **Dataset**: `Telco-Customer-Churn.csv`
- Features include customer demographics, service details, and churn status.

### Methodology
1. **Data Preprocessing**:
   - Handled missing values and inconsistencies.
   - Encoded categorical variables.
   - Standardized numerical data for modeling.
2. **Exploratory Data Analysis (EDA)**:
   - Uncovered patterns and trends in customer behavior.
   - Visualized relationships between features and churn.
3. **Predictive Modeling**:
   - Built classification models (Two-Class Boosted Decision Tree) to predict churn.
   - Evaluated models using metrics like accuracy, precision, recall, and F1-score.

4. **Deployment**:
   - Deployed the trained model to Azure Machine Learning using **Azure ML Designer**.
   - Created a **real-time endpoint** for predictions.
   - Used a **scoring script** to parse new data and provide churn probabilities.


### Azure Pipeline

This project utilized **Azure Machine Learning Designer** for the end-to-end workflow. Below is the pipeline created:

<img width="667" alt="image" src="https://github.com/user-attachments/assets/616554a2-5a65-4bfe-a3a1-e2dccba6e19a" />

#### Pipeline Steps:
1. **Clean Missing Data**: Removed missing values to prepare a clean dataset.
2. **Edit Metadata**: Updated data types and column metadata.
3. **Convert to Indicator Values**: Transformed categorical data into numerical format.
4. **SQL Transformation**: Applied SQL-based feature engineering.
5. **Execute Python Script**: Ran custom preprocessing steps via Python.
6. **Normalize Data**: Scaled numerical features to improve model performance.
7. **Split Data**: Split the dataset into training and testing subsets.
8. **Train Model**: Trained a Two-Class Boosted Decision Tree model to predict customer churn.

#### Deployment Workflow:
- **Model Deployment**: The trained model was registered in Azure Machine Learning.
- **Endpoint Creation**: A real-time endpoint was created for predictions, enabling API-based integrations.
- **Scoring Script**: A custom scoring script was used to parse incoming data and return predictions.


## Results

- Key drivers of churn identified include **contract type**, **monthly charges**, and **tenure**.
- Deployed endpoint enables seamless testing of new customer data for predicting churn probability.


## Files Included
1. **`Marketing Analytics Project.ipynb`**: Complete analysis and modeling process in Python.
2. **`Telco-Customer-Churn.csv`**: Dataset used for the analysis.
3. **Pipeline Visual**: Snapshot of the pipeline created in Azure ML Designer.
4. **Scoring Script**: Python script used for model deployment and inference.


