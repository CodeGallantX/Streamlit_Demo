import streamlit as st

st.title("StatEase")

st.header("Welcome to StatEase!!")

st.markdown("Markdown **of** _a_ [section](#)")
st.markdown("[See Data Visualisation examples](Visualisation) ")

st.subheader("Subheader: Introduction")

st.caption("Your statistics buddy for Computer Science Students taking STA111 in LASUSTECH - caption")

st.code("Code: Written in Python")

st.latex(r'''ax^2 + bx + c = 0''')

st.sidebar.title("StatEase")
st.sidebar.markdown("[Join our community](#)")