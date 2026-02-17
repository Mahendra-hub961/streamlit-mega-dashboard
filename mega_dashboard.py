import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mega Streamlit Project",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("🚀 Mega App Navigation")

menu = st.sidebar.radio(
    "Go to Section",
    [
        "🏠 Home",
        "👤 Profile",
        "🧩 Components Demo",
        "📊 Data Tools",
        "📈 Charts",
        "🎯 Utilities",
        "ℹ About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Mega Streamlit Project Demo")

# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------
if menu == "🏠 Home":

    st.title("🎓 Welcome to Mega Streamlit App")

    st.write("""
    This is a **large professional Streamlit application** that demonstrates:
    
    ✔ User Inputs  
    ✔ Widgets  
    ✔ Charts  
    ✔ File Upload  
    ✔ Data Processing  
    ✔ Sidebar Navigation  
    ✔ Interactive Components  
    """)

    st.success("Use sidebar to explore features!")

    st.image("https://via.placeholder.com/900x300")

# ---------------------------------------------------------
# PROFILE PAGE
# ---------------------------------------------------------
elif menu == "👤 Profile":

    st.title("👤 Profile Dashboard")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://via.placeholder.com/200")

    with col2:
        st.subheader("Personal Details")
        st.write("Name: John Doe")
        st.write("Role: Data Science Student")
        st.write("Country: India")

        st.subheader("Skills")
        skills = ["Python", "SQL", "Machine Learning", "Streamlit"]
        for skill in skills:
            st.write("✔", skill)

        st.progress(85, text="Skill Progress")

# ---------------------------------------------------------
# COMPONENTS DEMO
# ---------------------------------------------------------
elif menu == "🧩 Components Demo":

    st.title("🧩 Interactive Components")

    st.header("User Input Form")

    name = st.text_input("Enter Name")
    age = st.slider("Select Age", 1, 100, 25)

    if st.button("Submit Details"):
        st.success(f"Hello {name}, Age {age}")

    st.divider()

    st.header("Checkbox Example")

    if st.checkbox("Show Hidden Message"):
        st.info("🎉 Secret Text Visible!")

    st.divider()

    st.header("Selectbox Example")

    lang = st.selectbox(
        "Choose Programming Language",
        ["Python", "Java", "C++", "JavaScript", "SQL"]
    )

    st.write("Selected:", lang)

    st.divider()

    st.header("Radio Buttons")

    gender = st.radio("Select Gender", ["Male", "Female", "Other"])
    st.write("Gender:", gender)

    st.divider()

    st.header("Multiselect Example")

    hobbies = st.multiselect(
        "Choose Hobbies",
        ["Reading", "Gaming", "Coding", "Traveling"]
    )

    st.write("Your hobbies:", hobbies)

    st.divider()

    st.header("Counter Example")

    count = 0
    if st.button("Increase Counter"):
        count += 1
    st.write("Counter:", count)

    st.divider()

    if st.button("Show Success Message"):
        st.balloons()
        st.success("Action Successful!")

# ---------------------------------------------------------
# DATA TOOLS
# ---------------------------------------------------------
elif menu == "📊 Data Tools":

    st.title("📊 Data Tools")

    st.subheader("Sample DataFrame")

    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 90, 78]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.divider()

    st.subheader("Upload CSV File")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.write("Uploaded Data:")
        st.dataframe(df)

    st.divider()

    st.subheader("Generate Random Data")

    rows = st.slider("Select Rows", 5, 100, 10)
    random_df = pd.DataFrame(
        np.random.randn(rows, 3),
        columns=["A", "B", "C"]
    )

    st.dataframe(random_df)

# ---------------------------------------------------------
# CHARTS PAGE
# ---------------------------------------------------------
elif menu == "📈 Charts":

    st.title("📈 Data Visualization")

    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(chart_data)

    st.bar_chart(chart_data)

    st.area_chart(chart_data)

# ---------------------------------------------------------
# UTILITIES PAGE
# ---------------------------------------------------------
elif menu == "🎯 Utilities":

    st.title("🎯 Utility Tools")

    st.subheader("Current Date & Time")
    st.write(datetime.now())

    st.divider()

    st.subheader("Simple Calculator")

    num1 = st.number_input("Enter Number 1")
    num2 = st.number_input("Enter Number 2")

    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply"])

    if st.button("Calculate"):

        if operation == "Add":
            st.success(num1 + num2)

        elif operation == "Subtract":
            st.success(num1 - num2)

        elif operation == "Multiply":
            st.success(num1 * num2)

    st.divider()

    st.subheader("Text Analyzer")

    text = st.text_area("Enter text")

    if st.button("Analyze"):
        st.write("Characters:", len(text))
        st.write("Words:", len(text.split()))

# ---------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------
elif menu == "ℹ About":

    st.title("ℹ About This App")

    st.write("""
    This Mega Streamlit App demonstrates:
    
    ✔ Multi-page navigation  
    ✔ Interactive widgets  
    ✔ Data visualization  
    ✔ File upload handling  
    ✔ Utility tools  
    ✔ Dashboard design  
    """)

    rating = st.slider("Rate this App", 1, 5)
    st.write("Your rating:", rating, "⭐")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption("🚀 Mega Professional Streamlit Project")
