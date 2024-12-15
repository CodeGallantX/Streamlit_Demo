import streamlit as st

st.subheader("Containerizing Method #1")
container = st.container()
container.write("The following are also written in the container:")
container.time_input("Set time for interview:")
st.code(r'''
container = st.container()
container.write("The following are also written in the container:")
container.time_input("Select time:")
        ''')

st.subheader('OR')

st.subheader("Containerizing Method #2")
with st.container():
    st.write("The following are also written in the container:")
    st.time_input("Select time:")

st.code(r'''
with st.container():
    st.write("The following are also written in the container:")
    st.time_input("Select time:")
        ''')



st.write("This is written outside the container")
st.time_input("Set time:")