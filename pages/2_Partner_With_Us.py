import streamlit as st

st.title("Partner With Us 🤝")

st.write("""
We are always looking for partners who share our mission of sustainability and clean water access.

If you're a:
- 🌍 Non-profit
- 🏢 Corporate CSR team
- 🧑‍💼 Social entrepreneur

Fill out the form below and let’s explore ways to collaborate!
""")

# Contact Form
with st.form("partnership_form"):
    name = st.text_input("Your Name")
    org = st.text_input("Organization / Company")
    email = st.text_input("Email")
    message = st.text_area("How would you like to partner with us?")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thanks {name}! We'll be in touch at {email} soon.")
