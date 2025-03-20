import streamlit as st
import requests  # Import requests to send the HTTP POST request

# Define the EmailJS API URL
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

# Title
st.title("BLESSY JEBARAJ")

# Create two columns
col1, col2 = st.columns([4, 3])  # Adjust the numbers to control column width (1: smaller, 2: larger)

# Left column: Your picture
with col2:
    st.image("blessy_picture.jpeg", width=200)  # Replace with your actual image file name and path

# Right column: About Me section
with col1:
    st.header("Hello!")
    st.write("""
    I’m a **Data Engineer** with expertise in building data pipelines, 
    creating insightful dashboards, and implementing data-driven solutions. 
    I have experience working with various tools like **Tableau**, **Python**, 
    **SQL**, and **Cloud Technologies**. Explore my work and get in touch!
    """)

# Links to social profiles
st.subheader("Connect with Me")
st.markdown("[LinkedIn](https://www.linkedin.com/in/blessyjebaraj2010/)")
st.markdown("[GitHub](https://github.com/blessyjebaraj)")

# Skills Page
st.header("Skills")
st.write("""
- Data Engineering
- Business Intelligence (BI) Tools (Tableau, Looker)
- Python Programming
- Data Modeling and ETL
- SQL & NoSQL Databases
- Cloud Platforms (AWS, GCP)
""")

# Project 1: Stock Portfolio App
st.subheader("Stock Portfolio Tracker")
st.write("I built an interactive app that allows users to track their stock portfolio with real-time data and visualize portfolio growth.")
st.markdown("[View Project](https://github.com/blessysprofile/stock-portfolio-app)")

# Project 2: Tableau Dashboard Embedding
st.subheader("Tableau Dashboard on Portfolio Performance")
st.write("A dynamic Tableau dashboard for monitoring portfolio performance over time.")
st.markdown("[View Dashboard](https://public.tableau.com/app/profile/blessy.jebaraj123/viz/Blessy_Jebaraj_Dashboard/CHURNANALYSISSTRY)")

# Add Snipping Tool Video (Local file)
st.subheader("Watch the Snipping Tool Demo")
st.video("tableau.mp4")

# Contact Page (Placeholder for now)
st.header("Contact Me")
st.write("Feel free to reach out via email at blessy.jebaraj@gmail.com.")


# Contact Form - Message for Users to Drop a Message
st.header("Drop Me a Message!")

# EmailJS Integration (Updated to send a user message)
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

# Form for users to send a message
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