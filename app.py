import streamlit as st
import requests  # Import requests to send the HTTP POST request

# Define the EmailJS API URL
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

# Default to ABOUT if session_state is not set
if "page" not in st.session_state:
    st.session_state.page = "ABOUT"

# Main Content
st.title("BLESSY JEBARAJ")

# Buttons for page navigation
col1, col2, col3 = st.columns([1, 2, 1])  # You can adjust the column layout for better spacing
with col1:
    if st.button("ABOUT"):
        st.session_state.page = "ABOUT"
with col2:
    if st.button("PORTFOLIO"):
        st.session_state.page = "PORTFOLIO"
with col3:
    if st.button("CONTACT"):
        st.session_state.page = "CONTACT"

if st.session_state.page == "ABOUT":
    col1, col2 = st.columns([4, 3])  # Adjust the numbers to control column width (1: smaller, 2: larger)
    
    with col2:
        st.image("blessy_picture.jpeg", width=200)  # Replace with your actual image file name and path
    
    with col1:
        st.header("Hello!")
        st.write(""" 
        I’m a **Analytics Engineer** with expertise in building data pipelines, 
        creating insightful dashboards, and implementing data-driven solutions. 
        I have experience working with various tools like **Tableau**, **Python**, 
        **SQL**, **dbt**, **Airflow**, **Looker**, and **Cloud Technologies**. 
        Explore my work and get in touch!
        """)
    
    st.subheader("Connect with Me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/blessyjebaraj2010/)")
    st.markdown("[GitHub](https://github.com/blessyjebaraj)")

elif st.session_state.page == "PORTFOLIO":
    st.header("Skills")
    st.write(""" 
    - Data Engineering
    - Business Intelligence (BI) Tools (Tableau, Looker)
    - Python Programming
    - Data Modeling and ETL/ELT
    - SQL & NoSQL Databases
    - Cloud Platforms (AWS, GCP)
    """)
 
    st.subheader("Analytical Solutions")
    st.write("A dynamic Tableau dashboard for analysing Customer Churn")
    st.markdown("[View Dashboard](https://public.tableau.com/app/profile/blessy.jebaraj123/viz/Blessy_Jebaraj_Dashboard/CHURNANALYSISSTRY)")
    
    st.subheader("Watch the Demo of Headcount Analytics")
    st.video("tableau.mp4")

    st.subheader("G2M Dashboard")
    st.write("G2M Services, LLC specializes in transforming public sector business development through advanced data analytics.")
    st.write("Their mission is to empower stakeholders in public sector IT with the insights needed to navigate complex markets efficiently")
    st.write("This is a brief overview of the Tableau dashboards I built for the clients of G2M")
    st.video("g2m.mp4")

elif st.session_state.page == "CONTACT":
    st.header("Contact Me")
    st.write("Feel free to reach out via email at blessy.jebaraj@gmail.com.")
    
    st.header("And I'd love to hear your thoughts")
    
    def send_email(name, email, message):
        data = {
            "service_id": "service_ymmdp3g",  # Your EmailJS service ID
            "template_id": "template_ytxlqih",  # Replace with your EmailJS template ID
            "user_id": "9w6qlhoSbglKqkpcf",  # Replace with your EmailJS user ID
            "template_params": {
                "from_name": name,
                "from_email": email,
                "message": message,
            },
        }

        response = requests.post(EMAILJS_URL, json=data)
        if response.status_code == 200:
            st.success("Your message has been sent successfully!")
        else:
            st.error("Something went wrong. Please try again.")
    
    with st.form("message_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and message:
                send_email(name, email, message)
            else:
                st.error("Please fill out all fields.")
