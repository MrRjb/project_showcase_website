import streamlit
from send_email import send_email

streamlit.header("Contact Me")

with streamlit.form(key="email_forms"):
    user_email = streamlit.text_input("Your Email Address here")
    raw_message = streamlit.text_area("Your Message")
    button = streamlit.form_submit_button("Submit")
    
    message = f"""\
Subject: New Message from {user_email}

From: {user_email}
    
{raw_message}
"""
    
    if button:
        print("I was pressed")
        send_email(message)
        streamlit.info("Email sent succesfully!")
    