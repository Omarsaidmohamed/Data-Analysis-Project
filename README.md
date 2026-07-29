# Data Analyst Job Postings Analysis

## Overview

This project analyzes Data Analyst job postings to understand the job market, salary trends, required skills, and hiring patterns.

The main goal of this project is to clean the dataset, explore the data, and find useful insights about Data Analyst jobs.

## Dataset

The dataset used in this project is **Data Analyst Job Postings** from Kaggle.
Dataset Link:
[Data Analyst Job Postings Dataset](https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search)

The dataset contains job advertisements with information about:

* Job titles
* Companies
* Locations
* Salary information
* Job descriptions
* Required skills

For this project, a sample of **1,000 job postings** was selected from the original dataset to perform the analysis.

## Data Cleaning

The dataset required several cleaning steps before analysis:

* Removed unnecessary columns
* Handled missing values
* Cleaned location and work type information
* Processed salary columns
* Extracted and analyzed skills from job descriptions
* Created new useful columns:

  * `work_type`
  * `skills_count`
  * `salary_category`

## Exploratory Data Analysis

The analysis focuses on:

* Most common Data Analyst job titles
* Companies hiring Data Analysts
* Job locations distribution
* Remote vs On-site jobs
* Salary analysis
* Most required skills
* Relationship between skills and salaries

## Tools & Libraries

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly Express 
* Jupyter Notebook

## Key Insights

The project explores questions like:

* Which companies have the most Data Analyst job postings?
* What are the most common required skills?
* How are salaries distributed?
* Are remote jobs common in the Data Analyst field?
* Which skills appear most frequently in job descriptions?
* Is working on-site or remotly more lucrative?

## Limitations

This analysis has some limitations:

* A sample of **1,000 job postings** was used instead of the full dataset.
* Many job postings did not include salary information.
* Some skills may not have been extracted perfectly because they were identified from job descriptions.
* The results represent the selected sample and may not reflect the entire Data Analyst job market.

## Conclusion

This project provides an overview of the Data Analyst job market by analyzing job postings data and extracting useful information about salaries, skills, and job opportunities.
