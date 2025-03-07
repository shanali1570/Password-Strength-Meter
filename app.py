# create Password Strength Meter with Streamlit
# step by step Explanation with code for study purpose

# Importing Required Libraries
import streamlit as st   # Streamlit Library GUI banane ke liye
import re                # Regular Expression Library (Regex) Password Strength check (analyze) karne ke liye
import random            # Random Library Password Generate karne ke liye
import string          # String Library Password Generate karne ke liye

# Title of the Web Application
st.title("Password Strength Meter")
# Title of the Web Application
st.subheader("Created by: S.M.Shan-e-Ali")
# Title of the Web Application
st.write("This is a Password Strength Meter Web Application, which helps you to check the strength of your password.")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0  # Initial Score of Password zero
    feedback = []   # Empty List for Feedback

    # step 1 Check Password Length
    if len(password) >= 8:
        
        score += 1  # Score Incremented by 1
        
    else:   # If Password Length is less than 8
        feedback.append("Password length should be at least 8 characters.")

    # step 2 Check for Uppercase Letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        
        score += 1  # Score Incremented by 1
        
    else:   # If Password doesn't contain Uppercase Letters
        feedback.append("Password should contain at least one uppercase letter.")

    # step 3 Check for Digits
    if re.search(r'\d', password):
        
        score += 1  # Score Incremented by 1
        
    else:   # If Password doesn't contain Digits
        feedback.append("Password should contain at least one digit.")

    # step 4 Check for Special Characters
    if re.search(r'[!@#$%^&*]', password):
        
        score += 1  # Score Incremented by 1
        
    else:   # If Password doesn't contain Special Characters
        feedback.append("Password should contain at least one special character.")

    # step 5 Return  Password Score and Feedback
    if score == 4:  # If Password Score is 4
        return "Strong Password!","green", feedback # Return Strong Password, Green Color and Feedback
    
    elif score == 3:  # If Password Score is 3
        return "Moderate Password!","orange", feedback # Return Moderate Password, Orange Color and Feedback
    
    else:   # If Password Score is less than 3
        return "Weak Password!","red", feedback # Return Weak Password, Red Color and Feedback

# Function to Generate Random Password
def generate_password():    # Function Definition
    characters = string.ascii_letters + string.digits + "!@#$%^&*"  # Characters for Password Generation 
                                                                    # (Letters, Digits, Special Characters)
    return ''.join(random.choice(characters) for i in range(12))  # Return Random Password of Length 12

# Input Field for Password
password = st.text_input("Enter Your Password:", type="password")  # Input Field for Password

# check password strength and show feedback
if password:  # If Password is not Empty
    result, color, suggestions = check_password_strength(password)  # Check Password Strength
    st.markdown(f'<p style="color:{color}; font-size:20px;"><b>{result}</b></p>', unsafe_allow_html=True)  
                                                                                # Display Password Strength
    if suggestions:  # If Suggestions are there
        st.write("Suggestions:")
        for suggestion in suggestions:  # Display Suggestions
            st.write(suggestion)
else:  # If Password is Empty
    st.write("Please enter a password.")  # Display Message

# Generate Password Button
st.write("Automatically Generate Strong Password")  # Display Message for Generate Password Button 
if st.button("Generate Strong Password"):  # If Generate Password Button is Clicked
    strong_password = generate_password()  # Generate Strong Password
    st.text(f"Suggested Strong Password: {strong_password}")  # Display Strong Password
