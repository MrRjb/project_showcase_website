import streamlit
import pandas

streamlit.set_page_config(layout="wide")
col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/Self-1.jpg")
    
with col2:
    streamlit.title("Rupankar Borah")
    content = """
    Hi, I am Rupankar! I am a Python Programmer, teacher 
    and founder of PythonDisciples. 
    I have built various apps as part of my journey of learning to code with Python. 
    As a self-taught developer, I believe in learning through adversity 
    to maximize the utilization of the Brain throughout the learning process. 
    Hence, I have built 'A LOT' of apps which can be found in my GitHub Page. 
    And will mentor students to learn to code my way - THE HARD WAY!     
    """
    streamlit.info(content)
    
streamlit.subheader("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = streamlit.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")
        
with col4:
    for index, row in df[10:].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")