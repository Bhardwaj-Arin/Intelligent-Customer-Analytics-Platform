# Phase 1: Data Understanding & Initial Assessment

## Objective

The objective of Phase 1 is to thoroughly understand the dataset before performing any cleaning, visualization, or machine learning. This phase focuses on understanding the business problem, dataset structure, feature information, and overall data quality.

> **Rule:** Never start cleaning or modeling without first understanding the data.

---

# Why is Phase 1 Important?

A machine learning model is only as good as the quality of data provided to it. Most real-world data science projects spend a significant amount of time understanding the data before any preprocessing or modeling begins.

This phase helps answer questions like:

- What does the dataset represent?
- What is the business problem?
- What does each feature mean?
- Are there missing values?
- Are there duplicate records?
- Are the data types correct?
- Is the data reliable enough for analysis?

---

# Deliverables

At the end of this phase, the project should contain:

```
reports/
│
├── Business_Problem.md
├── Data_Dictionary.md
├── Initial_Data_Quality_Report.md
├── profiling/
│   └── data_profiling_report.html
│
└── figures/
```

---

# Files Created

## 1. Business_Problem.md

### Purpose

Describes the business context of the project.

### Contains

- Business problem
- Project objective
- Business goals
- Expected outcome
- Success metrics

### Why?

Every data science project exists to solve a business problem, not just build a machine learning model.

---

## 2. Data_Dictionary.md

### Purpose

Provides documentation for every feature in the dataset.

### Contains

- Column Name
- Data Type
- Description
- Business Importance

Example:

| Column | Description |
|---------|-------------|
| CustomerID | Unique customer identifier |
| Invoice | Invoice number |
| Quantity | Number of products purchased |
| Price | Unit price |
| Country | Customer's country |

---

## 3. Initial_Data_Quality_Report.md

### Purpose

Documents the overall quality of the dataset.

### Contains

- Dataset dimensions
- Missing values
- Duplicate records
- Data types
- Outliers
- Invalid values
- Initial observations
- Cleaning recommendations

---

## 4. Data Profiling Report

Generated automatically using **ydata-profiling**.

### Purpose

Provides a quick summary of:

- Missing values
- Correlations
- Distributions
- Warnings
- Data types
- Duplicate information

---

# Notebook

```
notebooks/
└── 01_Data_Understanding.ipynb
```

This notebook contains the initial exploration of the dataset.

Typical sections include:

1. Import Libraries
2. Load Dataset
3. Dataset Overview
4. Data Types
5. Missing Values
6. Duplicate Records
7. Unique Values
8. Statistical Summary
9. Memory Usage
10. Initial Observations

---

# Important Functions Used

## Dataset Shape

```python
df.shape
```

Purpose:
- Number of rows
- Number of columns

---

## Column Names

```python
df.columns
```

Purpose:
- View all features

---

## First Records

```python
df.head()
```

Purpose:
- Quick inspection of data

---

## Random Samples

```python
df.sample(5)
```

Purpose:
- Detect unusual records

---

## Dataset Information

```python
df.info()
```

Purpose:
- Data types
- Missing values
- Memory usage

---

## Statistical Summary

```python
df.describe()
```

Purpose:
- Numerical statistics

---

## Missing Values

```python
df.isnull().sum()
```

Purpose:
- Count missing values

---

## Duplicate Records

```python
df.duplicated().sum()
```

Purpose:
- Identify duplicate rows

---

## Unique Values

```python
df.nunique()
```

Purpose:
- Cardinality of each feature

---

## Memory Usage

```python
df.memory_usage(deep=True)
```

Purpose:
- Estimate dataset memory consumption

---

# Key Observations to Record

During this phase, record observations such as:

- Dataset size
- Number of features
- Missing values
- Duplicate records
- Incorrect data types
- High-cardinality columns
- Potential outliers
- Business assumptions

Example:

> Approximately 24% of CustomerID values are missing, indicating many transactions may belong to anonymous customers.

---

# Common Data Quality Issues

- Missing Values
- Duplicate Records
- Incorrect Data Types
- Invalid Entries
- Outliers
- Inconsistent Formatting

These issues are **identified** in Phase 1 but are **resolved** in Phase 2.

---

# Interview Questions

### Why is Data Understanding important?

Because understanding the dataset helps identify data quality issues, business context, and feature meanings before preprocessing and modeling.

---

### Difference between Data Understanding and Data Cleaning?

**Data Understanding**
- Explore the dataset
- Identify issues
- Understand business context

**Data Cleaning**
- Fix the identified issues

---

### Why create a Data Dictionary?

A Data Dictionary documents the meaning and purpose of every feature, improving project maintainability and communication between technical and business teams.

---

### Why generate a Data Profiling Report?

It provides an automated summary of the dataset, helping identify potential problems quickly.

---

### Why don't we build models immediately?

Because poor-quality data leads to poor-quality models.

---

# Best Practices

- Never modify the raw dataset.
- Keep observations documented.
- Understand every feature before cleaning.
- Separate business understanding from technical analysis.
- Save all reports and figures for future reference.
- Follow a structured notebook workflow.

---

# Outcome of Phase 1

After completing this phase, you should have:

- Complete understanding of the business problem
- Understanding of every feature
- Initial assessment of data quality
- Documentation of observations
- Professional profiling report
- Data dictionary
- Data quality report

This serves as the foundation for **Phase 2: Data Cleaning & Preprocessing**.