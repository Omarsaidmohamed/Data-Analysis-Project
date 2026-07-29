#  Data Analyst Job Postings Analysis

##  Project Overview

This project analyzes **Data Analyst job postings** to explore current hiring trends, required technical skills, work arrangements, salary information, and job market insights.

The project follows a complete data analysis workflow, including data cleaning, feature engineering, exploratory data analysis (EDA), and data visualization using Python.

---

##  Dataset

* **Source:** Kaggle
* Dataset Link: 
[Data Analyst Job Postings Dataset](https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search)

The original dataset contains real-world job postings collected from Google Jobs.

---

##  Project Objectives

* Clean and prepare raw job posting data.
* Analyze the most common job titles.
* Identify the most requested technical skills.
* Explore work arrangements (Remote vs On-site).
* Analyze salary information where available.
* Generate meaningful insights about the Data Analyst job market.

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Regular Expressions (Regex)

---

##  Data Cleaning

The dataset was cleaned before analysis by:

* Removing unnecessary columns.
* Handling missing values where appropriate.
* Removing duplicate records.
* Standardizing categorical values.
* Preparing salary-related information.
* Creating a separate cleaned dataset for analysis.

---

##  Feature Engineering

Several new features were created to improve the analysis, including:

* Main job role categorization.
* Technical skill extraction.
* Skill count analysis.
* Additional features derived from the original dataset using Python and Regular Expressions.

---

##  Exploratory Data Analysis (EDA)

The project explores several aspects of the job market, including:

* Most common job titles
* Most requested technical skills
* Most common job locations
* Remote vs On-site job distribution
* Salary distribution
* Salary comparison across work arrangements

Visualizations were created using:

* Matplotlib
* Seaborn
* Plotly

---

##  Key Findings

Some of the insights obtained from the analysis include:

* SQL appeared among the most frequently requested technical skills.
* Python and Excel were also highly demanded across many job postings.
* On-site positions were more common than remote positions in the analyzed dataset.
* Salary information was available for only a subset of job postings, limiting salary-related analysis.

---

##  Limitations

* Many job postings did not include salary information.
* Some fields contained missing values.
* The dataset represents Google Job Search results and may not reflect the entire job market.
* Results depend on the available data collected in the dataset.

---

##  Repository Structure

```text
├── Job_Postings_Project.ipynb
├── cleaned_job_postings.csv
├── requirements.txt 
└── README.md
```

---

##  How to Run

1. Clone the repository.
2. Install the required Python libraries.
3. Open the Jupyter Notebook.
4. Run the notebook cells in order.

---

