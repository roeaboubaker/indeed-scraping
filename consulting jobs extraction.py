#!/usr/bin/env python
# coding: utf-8

# In[20]:


pip install beautifulsoup4


# In[21]:


pip install requests


# In[22]:


pip install selenium


# In[23]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


# In[24]:


# Set up Chrome options to customize the browser behavior
options = webdriver.ChromeOptions() 

# Set user-agent to mimic a browser behavior
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36')

# Initialize a Chrome WebDriver instance with customized options
driver = webdriver.Chrome(options=options) 

# URL of the webpage to scrape
url = "https://www.indeed.com/jobs?q=consultant&l=&from=searchOnDesktopSerp&vjk=d2916675afdc0a34"

# Open the URL in the Chrome WebDriver instance
driver.get(url)

# Sleep for 5 seconds to ensure the page loads completely before scraping
sleep(5)

# Get the HTML source code of the page after it has fully loaded
html = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')


# In[25]:


def get_data(job_listing):
    # Extract job title
    title = job_listing.find("a").find("span").text.strip()
    
    # Extract company name if available, otherwise assign an empty string
    try:
        company = job_listing.find('span', class_="css-63koeb eu4oa1w0").text.strip()
    except AttributeError:
        company = ''

    # Extract job location if available, otherwise assign an empty string
    try:
        location = job_listing.find('div', class_='css-1p0sjhy eu4oa1w0').text.strip()
    except AttributeError:
        location = ''

    # Extract date posted
    try:
        date_posted = job_listing.find('span', class_="css-qvloho eu4oa1w0").text.strip()
    except AttributeError:
        date_posted = ''
    
    # Return a tuple containing all the extracted information
    return ('consultant',title, company, location, date_posted)


# In[26]:


# Define an empty list to store the extracted data
records = []

# Loop to scrape data from multiple pages until there are no more pages available
while True:
    try:
        # Extract the URL of the next page if available
        url = 'https://ng.indeed.com/' + soup.find('a', {'aria-label':'Next Page'}).get('href')
    except AttributeError:
        # If there are no more pages available, break the loop
        break
    
    # Open the next page in the browser
    driver.get(url)
    
    # Get the HTML source code of the next page
    html = driver.page_source
    
    # Parse the HTML of the next page using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all job listings on the next page
    job_listings = soup.find_all('div', class_='job_seen_beacon') 

    # Iterate through each job listing on the page
    for job_listing in job_listings:
        # Extract data from the current job listing
        record = get_data(job_listing)
        
        # Append the extracted data to the records list
        records.append(record)

# Close the Chrome WebDriver instance
driver.quit()


# In[27]:


# Convert list of records into a DataFrame
df = pd.DataFrame(records, columns=['ID','Title', 'Company', 'Location','Date Posted'])

# Save DataFrame to an csv file
df.to_csv('consulting_job.csv', index=False)

print("Data saved to consulting_job.csv")


# In[28]:


display(df)


# In[ ]:




