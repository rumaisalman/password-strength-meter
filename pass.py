import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter 🔐")

st.title("Password Strength Meter 🔐")
st.markdown("""
    ## Welcome to the Password Strength Meter!
    A tool that checks the password strength and suggests a stronger password.
""")

common_passwords = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "123123", "admin", "letmein", "welcome", "monkey", 
    "1234", "12345", "iloveyou", "sunshine", "princess", 
    "flower", "superman", "asdfgh", "qwerty123", "login", "hello", "whatever","12345678", "qwerty1", "111111", "hi", "654321"
}

password = st.text_input("Enter your password", type="password")

if password:  
    if password.lower() in common_passwords:
        st.error("❌ This is a common password. Please choose a stronger one!")
    else:
        feedback = []
        score = 0

        if len(password) >= 8:
            score += 1
        else:
            feedback.append("🔹 Password should be at least 8 characters long.")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("🔹 Include both uppercase and lowercase letters.")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            feedback.append("🔹 Include at least one number (0-9).")

        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append("🔹 Include at least one special character (!@#$%^&*).")


        if score <= 2:
            strength_message = "⚠️ Weak password: missing key elements."
        elif score == 3:
            strength_message = "🟡 Moderate password: consider adding more security features."
        else:
            strength_message = "✅ Strong password: meets all security criteria."

        st.subheader("Password Strength")
        st.write(strength_message)


        if feedback:
            st.subheader("Improvement Suggestions")
            for tip in feedback:
                st.write(tip)
else:
    st.info("Please enter your password to get started.")
