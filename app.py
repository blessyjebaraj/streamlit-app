import streamlit as st
import requests  # Import requests to send the HTTP POST request

# Define the EmailJS API URL
EMAILJS_URL = "https://api.emailjs.com/api/v1.0/email/send"

# Default to ABOUT if session_state is not set
if "page" not in st.session_state:
    st.session_state.page = "ABOUT"

# Main Content with custom styling
st.markdown("""
    <style>
        /* Import Poppins font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            background-color: #f9f9f9;
            font-family: 'Poppins', sans-serif;
        }

        .main-title {
            font-size: 50px;
            color: #1e3a8a;
            font-weight: bold;
            text-align: center;
            margin-top: 40px;
            background: linear-gradient(90deg, #4b8f8c, #3b82f6);
            -webkit-background-clip: text;
            color: transparent;
        }

        .header {
            font-size: 32px;
            color: #2f4f4f;
            font-weight: 600;
            margin-top: 20px;
            text-transform: uppercase;
        }

        .subheader {
            font-size: 18px;
            color: #5f6368;
            font-weight: 500;
        }

        .button {
            background-color: #8a9a5b;
            color: white;
            border-radius: 8px;
            padding: 15px 30px;
            font-size: 18px;
            margin-top: 30px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .button:hover {
            background-color: #6e7b38;
            transform: scale(1.05);
        }

        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }

        .col-img {
            border-radius: 50%;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }

        .page-button-container {
            display: flex;
            justify-content: space-evenly;
            margin-top: 40px;
        }

        .page-button-container button {
            background-color: #2f3b52;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 20px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .page-button-container button:hover {
            background-color: #1d2b3b;
            transform: scale(1.1);
        }

        .footer {
            font-size: 16px;
            color: #757575;
            text-align: center;
            margin-top: 60px;
        }

        .footer a {
            color: #4b8f8c;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">BLESSY JEBARAJ</h1>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
with col1:
    if st.button("ABOUT", key="about_button", use_container_width=True):
        st.session_state.page = "ABOUT"
with col2:
    if st.button("PORTFOLIO", key="portfolio_button", use_container_width=True):
        st.session_state.page = "PORTFOLIO"
with col3:
    if st.button("CONTACT", key="contact_button", use_container_width=True):
        st.session_state.page = "CONTACT"
with col4:
    with open("Blessy_Jebaraj_CV.pdf", "rb") as file:
        st.download_button(
            label="DOWNLOAD CV",
            data=file,
            file_name="Blessy_Jebaraj_CV.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# Page content with improved styling
if st.session_state.page == "ABOUT":
    col1, col2 = st.columns([4, 3])  # Adjust the numbers to control column width (1: smaller, 2: larger)

    with col2:
        st.image("blessy_picture.jpeg", width=250, use_container_width=True)

    with col1:
        st.markdown('<h2 class="header">Hello!</h2>', unsafe_allow_html=True)
        st.write(""" 
        I’m an **Analytics Engineer** with expertise in building data pipelines, 
        creating insightful dashboards, and implementing data-driven solutions. 
        I have experience working with various tools like **Tableau**, **Python**, 
        **SQL**, **dbt**, **Airflow**, **Looker**, and **Cloud Technologies**. 
        Explore my work and get in touch!
        """)

    st.subheader("Connect with Me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/blessyjebaraj2010/)")
    st.markdown("[GitHub](https://github.com/blessyjebaraj)")

elif st.session_state.page == "PORTFOLIO":
    st.markdown('<h2 class="header">Skills</h2>', unsafe_allow_html=True)
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
    st.markdown('<h2 class="header">Contact Me</h2>', unsafe_allow_html=True)
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

        submit_button = st.form_submit_button("Send Message", use_container_width=True)

        if submit_button:
            if name and email and message:
                send_email(name, email, message)
            else:
                st.error("Please fill out all fields.")

# Footer for extra flair
st.markdown('<div class="footer">Made with ❤️ by <a href="https://github.com/blessyjebaraj" target="_blank">Blessy Jebaraj</a></div>', unsafe_allow_html=True)
