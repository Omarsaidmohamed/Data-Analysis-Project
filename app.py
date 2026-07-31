# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Analyst Job Market Dashboard")
Job_Postings = pd.read_csv("cleaned_job_postings.csv") 

# Define remote job
remote_jobs=[]
for remote in Job_Postings["work_type"]:
    if remote == "Remote":
        remote_jobs.append(remote)

#     KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Jobs", len(Job_Postings))
col2.metric("Companies", Job_Postings["company_name"].nunique())
col3.metric("Average Salary",f"${Job_Postings["salary_avg"].mean():,.0f}")
col4.metric("Remote Jobs", len(remote_jobs))

# -------- SLIDER -----
n_rows= st.slider("Choose number of rows to display" , min_value=5 ,max_value=len(Job_Postings))
colmns_to_show = st.multiselect("Select colmns to show" , Job_Postings.columns.tolist(), default=Job_Postings.columns.tolist())
st.write(Job_Postings[:n_rows][colmns_to_show])

#     Taps
tab1 , tab2 , tab3 = st.tabs(["Job Analysis" , "Salary" , "Skills"])

with tab1:
# ----- Top 10 Job Titles -----
    top_titles = Job_Postings["title"].value_counts().head(10).sort_values()
    fig = px.bar(x=top_titles.values , y=top_titles.index , title="Top 10 Job Titles" , labels={"x" : "Number Of Top Jobs Postings" , "y" : "Job Title" ,})
    fig.update_traces(text=top_titles.values,textposition="outside")
    st.plotly_chart(fig)
    st.divider()

#  ------ Most Freq Locations In Job Postings -------
    most_locations = Job_Postings["location"].value_counts().head(10)
    fig,ax = plt.subplots(figsize=(10,4))
    sns.barplot(x= most_locations.values , y=most_locations.index, color="#FF5C85")
    fig.tight_layout()
    ax.set_title("Most Freq Locations In Job Postings" , weight="bold")
    ax.grid(linestyle="--" , alpha=0.4)
    ax.set_ylabel("Location" , fontsize=12)
    ax.set_xlabel("Number of freq locations" , fontsize=12)
    st.pyplot(fig)
    st.divider()

#      -------- Distribution of Remote and On-site Jobs ----------
    most_work_type = Job_Postings["work_type"].value_counts()
    fig,ax = plt.subplots(figsize=(10,4))
    sns.countplot(data = Job_Postings , x="work_type", color = "#859E80")
    ax.set_xlabel("Work Type" , fontsize=14 , ha = "center")
    ax.set_ylabel("Count" , fontsize=14 , ha = "center")
    ax.grid(linestyle="--" , alpha=0.4)
    ax.set_title("Distribution of Remote and On-site Jobs",fontsize=15,weight="bold")
    st.pyplot(fig)
    st.divider()

#    -------- Top 10 job posting companies ---------
    top_companies = Job_Postings["company_name"].value_counts().head(10)
    fig,ax = plt.subplots(figsize=(10 , 4))
    ax.barh(top_companies.index , top_companies.values , color="cyan" )
    ax.set_title("Top 10 job posting companies" , fontsize=15 , weight="bold")
    ax.set_xlabel("Frequansis" , fontsize = 12)
    ax.set_ylabel("Companies" , fontsize = 12)
    ax.grid(linestyle="--" , alpha=0.4)
    ax.invert_yaxis()
    fig.tight_layout()
    for i , value in enumerate(top_companies.values):
        ax.text(value+1 ,i , str(value))
    st.pyplot(fig)
    st.divider()

with tab2:
    clear_salary = Job_Postings.copy()
    clear_salary = clear_salary.dropna(subset=["salary_standardized"])
    clear_salary["work_type"].value_counts()
    fig = px.box(clear_salary , x="work_type" , y="salary_standardized" , title="Compare Between Remote Salary And On Site Salary" , color="work_type")
    st.plotly_chart(fig)
    st.divider()


#     ------- most skills frequanced --------
with tab3:
    freq_skills_list = []
    for row in Job_Postings["description_tokens"]:
        if len(row) > 0:
            freq_skills_list.extend(row)
    freq_skills_series = pd.Series(freq_skills_list)
    tob_skills = freq_skills_series.value_counts().head(10)

#   ------ Top  Frequanced Skills -------
    fig, ax = plt.subplots(figsize=(10,4))
    plt.barh(tob_skills.index, tob_skills.values , color="Orange")
    ax.set_title("Top 10 Frequanced Skills" , weight="bold" )
    ax.set_xlabel("Frequances")
    ax.set_ylabel("Skills")
    ax.invert_yaxis()
    for i , value in enumerate(tob_skills.values):
        ax.text(value+1 , i , str(value))
    st.pyplot(fig)
    st.divider()

#  ------- Skills VS Salary --------
    fig,ax = plt.subplots(figsize=(10,4))
    sns.regplot(
        data=Job_Postings,
        x="skills_count",
        y="salary_standardized",
        line_kws=({"color": "red"}),
        scatter_kws=({"alpha" : 0.5})
        )
    ax.set_xlabel("Skill Count" , fontsize=12)
    ax.set_ylabel("Salary" , fontsize=12)

    ax.grid(linestyle="--" , alpha=0.6)
    ax.set_title("Number Of Skills VS Salary" , weight="bold")
    st.pyplot(fig)
    st.divider()


st.caption(
    "Created by Omar Said Mohamed"
)


