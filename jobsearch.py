import streamlit as st
import requests

# API Configuration
API_URL = "https://jsearch.p.rapidapi.com/search"
HEADERS = {
    "X-RapidAPI-Key": "9a3f3976d9msh692f92ea3a36bdbp1f0042jsn428ab170dbdd",  # Replace with your RapidAPI key
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# Streamlit App Layout
st.title("Job Recommendation Site")

# Input Fields
search_query = st.text_input("Enter Job Title", "Data Engineer")
location = st.text_input("Enter Location", "Berlin")
num_jobs = st.slider("Number of Jobs to Fetch", 1, 20, 10)

# Fetch Job Listings
if st.button("Search Jobs"):
    params = {"query": f"{search_query} in {location}", "num_pages": 1, "num_jobs": num_jobs}
    response = requests.get(API_URL, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        jobs = response.json().get("data", [])
        
        if not jobs:
            st.write("No matching jobs found.")
        else:
            for job in jobs:
                st.write(f"**{job['job_title']}** at {job['employer_name']} ({job['job_city']}, {job['job_country']})")
                st.write(f"[Job Link]({job['job_apply_link']})")
                st.write("---")
    else:
        st.error("Failed to fetch job listings. Please try again later.")