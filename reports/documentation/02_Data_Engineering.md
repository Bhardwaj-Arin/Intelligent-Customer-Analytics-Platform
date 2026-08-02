# Phase 2: Data Engineering

## Overview

The objective of this phase was to build a robust and reusable **Data Engineering Pipeline** that transforms the raw customer transaction dataset into a clean, validated, and analysis-ready dataset.

Instead of performing data cleaning directly inside Jupyter notebooks, a modular pipeline was developed following software engineering best practices. This approach improves code readability, maintainability, scalability, and reusability.

The processed dataset generated in this phase serves as the foundation for all subsequent phases, including Exploratory Data Analysis (EDA), Feature Engineering, Machine Learning, and Dashboard Development.

---

# Objectives

The primary objectives of this phase were:

- Build a modular data processing pipeline.
- Validate the quality and integrity of the raw dataset.
- Handle missing values and duplicate records.
- Convert columns to appropriate data types.
- Create additional useful features.
- Save the cleaned dataset for downstream tasks.
- Follow industry-standard project architecture.

---

# Project Structure

```
project/

├── config/
│   ├── config.py
│   └── paths.py
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── src/
│   └── data/
│       ├── loader.py
│       ├── validator.py
│       ├── cleaner.py
│       └── pipeline.py
│
├── notebooks/
├── reports/
├── models/
├── dashboard/
└── app.py
```

---

# Data Pipeline Workflow

```
Raw Dataset
      │
      ▼
Data Loader
      │
      ▼
Data Validator
      │
      ▼
Data Cleaner
      │
      ▼
Processed Dataset
      │
      ▼
Exploratory Data Analysis (Next Phase)
```

---

# Modules Developed

## 1. Data Loader (`loader.py`)

Responsible for loading the raw dataset into a Pandas DataFrame.

**Responsibilities**

- Read dataset from disk.
- Handle file loading.
- Return DataFrame.

---

## 2. Data Validator (`validator.py`)

Responsible for inspecting dataset quality before any modifications.

**Validation Checks**

- Dataset dimensions
- Missing values
- Duplicate records
- Data types
- Invalid or inconsistent values
- Required column availability

The validator reports issues but does not modify the dataset.

---

## 3. Data Cleaner (`cleaner.py`)

Responsible for transforming raw data into analysis-ready data.

**Cleaning Operations**

- Remove duplicate records.
- Handle missing values.
- Convert data types.
- Remove invalid observations.
- Create derived features.
- Standardize the dataset.

---

## 4. Data Pipeline (`pipeline.py`)

Acts as the central controller of the entire data engineering process.

Pipeline execution:

```
Load Data
    ↓
Validate Data
    ↓
Clean Data
    ↓
Save Processed Dataset
```

This allows the complete workflow to be executed using a single function call.

---

# Configuration Files

## config.py

Stores project-wide constants such as:

- Column names
- Required columns
- Default parameters
- Business constants

---

## paths.py

Stores all project paths.

Examples include:

- Raw data directory
- Processed data directory
- Reports directory
- Models directory

Using centralized paths improves maintainability and portability.

---

# Data Engineering Best Practices Followed

- Modular programming
- Separation of concerns
- Reusable code structure
- Centralized configuration
- Automated processing pipeline
- Clean project architecture
- Consistent folder organization
- Readable and maintainable code

---

# Output of Phase 2

At the end of this phase, the project successfully produces a cleaned and validated dataset stored in the `data/processed/` directory.

This processed dataset is now ready for:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Customer Segmentation
- Machine Learning
- Dashboard Development

---

# Key Learnings

During this phase, the following concepts were implemented:

- Data Engineering fundamentals
- Data validation
- Data cleaning
- Modular programming
- Pipeline architecture
- Configuration management
- File handling with `pathlib`
- Software engineering principles for data science projects

---

# Technologies Used

- Python
- Pandas
- NumPy
- Pathlib
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# Conclusion

Phase 2 established the data engineering foundation of the project by transforming raw customer transaction data into a clean, structured, and reusable dataset. By implementing a modular pipeline and following industry-standard software engineering practices, the project became easier to maintain, extend, and integrate with future phases such as EDA, Feature Engineering, Machine Learning, and Deployment.