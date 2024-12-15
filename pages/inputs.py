import streamlit as st


st.header("Input Fields:")
st.subheader("Inputs")
st.checkbox("I agree to the terms and conditions")
st.button("Submit")
st.radio("Pick your gender", ['Male', 'Female'])
st.selectbox("Pick your gender", ['Male', 'Female'])
st.multiselect("Choose a department", ['Industrial Mathematics', 'Chemistry', "Computer Science"])
st.select_slider("Pick a mark", ['Bad', 'Good', "Excellent"])
st.slider("Age: ", 15, 29)

st.subheader("Other Inputs")
st.number_input("Pick a number", 0, 10)
st.text_input("Enter your username: ")
st.date_input("Enter your Date of Birth: ")
st.time_input("Set time of meeting")
st.text_area("Write short bio...")
st.file_uploader("Upload a photo")
st.color_picker("Choose colour theme")



st.sidebar.title("StatEase")
st.sidebar.markdown("[Join our community](#)")