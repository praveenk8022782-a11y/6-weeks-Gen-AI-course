import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Subtitle
st.subheader("Learning Streamlit Basics")

# Text
st.write("This is a simple web app built using Python and Streamlit.")

# Input box
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋 Welcome to Streamlit!")

# Number input
age = st.number_input("Enter your age", min_value=1, max_value=100)

st.write("Your age is:", age)

# Slider
level = st.slider("Select your skill level", 1, 10)

st.write("Skill level:", level)

# Button
if st.button("Click Me"):
    st.info("Button clicked successfully!")

# Simple calculation
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("Add Numbers"):
    result = num1 + num2
    st.success(f"Result: {result}")

# Checkbox
if st.checkbox("Show message"):
    st.warning("You enabled the checkbox!")

# Radio buttons
option = st.radio("Choose language", ["Python", "Java", "C++"])

st.write("You selected:", option)