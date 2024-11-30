#!/usr/bin/env python
# coding: utf-8

# In[124]:


import pandas as pd


# In[125]:


pip install matplotlib


# In[126]:


import matplotlib.pyplot as plt


# In[127]:


import seaborn as sns


# In[128]:


engineer=pd.read_csv("engineer_job.csv")


# In[129]:


display(engineer)


# In[130]:


# Filter rows with 'engineer' in the job title
filtered_engineer=engineer[engineer['Title'].str.contains('engineer', case=False)]

# Display the filtered DataFrame
display(filtered_engineer)


# In[131]:


analyst=pd.read_csv("analysis_job.csv")


# In[132]:


display(analyst)


# In[133]:


# Filter rows with ' analyst' in the job title
filtered_analyst=analyst[analyst['Title'].str.contains('analyst', case=False)]

# Display the filtered DataFrame
display(filtered_analyst)


# In[134]:


consultant=pd.read_csv("consulting_job.csv")


# In[135]:


display(consultant)


# In[136]:


# Filter rows with 'consultant' in the job title
filtered_consultant= consultant[consultant['Title'].str.contains('consultant', case=False)]

# Display the filtered DataFrame
display(filtered_consultant)


# In[137]:


#DATA PROCESSING


# In[138]:


filtered_engineer.info()


# In[139]:


filtered_consultant.info()


# In[140]:


filtered_analyst.info()


# In[141]:


#DATA CLEANING


# In[142]:


missing_values=filtered_engineer.isnull().sum()


# In[143]:


display("missing_values:", missing_values)


# In[144]:


missing_values=filtered_analyst.isnull().sum()


# In[145]:


display("missing_values:", missing_values)


# In[146]:


filtered_analyst=filtered_analyst.dropna()


# In[147]:


missing_values=filtered_consultant.isnull().sum()


# In[148]:


display("missing_values:", missing_values)


# In[149]:


filtered_engineer.to_csv("filtered-engineer_job.csv" , index=False)


# In[150]:


filtered_analyst.to_csv("filtered-analysis_job.csv" , index=False)


# In[151]:


filtered_consultant.to_csv("filtered-consulting_job.csv" , index=False)


# In[152]:


#DATA CONCATINATING


# In[153]:


all_jobs = pd.concat([filtered_engineer,filtered_analyst,filtered_consultant])


# In[154]:


display(all_jobs)


# In[155]:


all_jobs.to_csv("all_jobss.csv" , index=False)


# In[156]:


#EXTRACTED DATA ABALYSIS


# In[157]:


#frequency of each job type
job_frequency = all_jobs['ID'].value_counts()


# In[158]:


display(job_frequency)


# In[159]:


# Plotting the job frequencies
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
job_frequency.plot(kind='bar')
plt.title('Frequency of Each Job Type')
plt.xlabel('Job Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for y-axis
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


# In[160]:


# Group data by ID
grouped = all_jobs.groupby('ID')

# Create a new figure for the plot
plt.figure(figsize=(15, 30))

# Loop through each group (ID)
for i, (name, group) in enumerate(grouped):
    # Count occurrences of each job title within the group
    job_counts = group['Title'].value_counts()
    # Select the top 10 job titles
    top_10_jobs = job_counts.head(10)
    # Plot the distribution of top 10 job titles for each ID
    plt.subplot(len(grouped), 1, i+1)
    top_10_jobs.plot(kind='bar', label=f'ID {name}')
    plt.title(f'Top 10 Jobs for ID {name}')
    plt.xlabel('Job Title')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.legend()

plt.tight_layout()
plt.show()


# In[191]:


# Identify companies offering the most job opportunities
company_job_counts = all_jobs['Company'].value_counts().head(20)  # 20 the desired number of top companies
top_companies = company_job_counts.index.tolist()


# In[192]:


# Calculate the percentage of each job title within each company
company_job_percentages = {}
for company in top_companies:
    total_jobs = all_jobs[all_jobs['Company'] == company]['ID'].count()
    job_titles = all_jobs[all_jobs['Company'] == company]['ID'].value_counts()
    company_job_percentages[company] = (job_titles / total_jobs) * 100
display(company_job_percentages[company] )


# In[193]:


plt.subplots(2, 1, figsize=(15, 10))


# In[194]:


# Plotting company job counts
plt.subplot(2, 1, 1)
company_job_counts.plot(kind='bar', color='skyblue')
plt.title('Top Companies by Job Opportunities')
plt.xlabel('Company')
plt.ylabel('Number of Job Opportunities')


# In[195]:


# Define custom colors
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'lime', 'pink', 'skyblue', 'yellow', 'brown']

#plot the distribution of job titles within each company
plt.figure(figsize=(12, 8))
for i, (company, job_percentages) in enumerate(company_job_percentages.items()):
    plt.bar(job_percentages.index, job_percentages.values, alpha=0.7, label=company, color=colors[i % len(colors)])

plt.title('Distribution of Job Titles within Top Companies (Percentage)')
plt.xlabel('Job Title')
plt.ylabel('Percentage')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()


# In[185]:


# Identify locations with the highest demand for roles
location_job_counts = all_jobs['Location'].value_counts().head(12)  # 12 number of top locations
top_locations = location_job_counts.index.tolist()


# In[167]:


plt.figure(figsize=(15, 10))
# Plotting locations with the highest demand for roles
plt.subplot(2, 1, 1)
location_job_counts.plot(kind='bar', color='skyblue')
plt.title('Locations with the Highest Demand for Roles')
plt.xlabel('Location')
plt.ylabel('Number of Job Opportunities')


# In[ ]:





# In[ ]:




