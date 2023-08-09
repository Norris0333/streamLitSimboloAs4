import streamlit as st
import random

st.title("Even or Odd Number Checker")

# Function to generate a new random number
def generate_random_number():
    return random.randint(1, 100)

# Add a button to generate a new random number
if st.button("Generate New Random Number"):
    random_number = generate_random_number()
    is_even = random_number % 2 == 0
    st.write(f"Random Number: {random_number}")
    st.write("It's Even!" if is_even else "It's Odd!")
