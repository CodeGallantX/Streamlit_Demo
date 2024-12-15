import streamlit as st

st.success("Transfer Successful!")
st.error("Error occurred!")
st.warning("Warning: Network breach imminent")
st.info("You have been selected to participate in the DevSprint3.0 contest")
st.exception(RuntimeError("RuntimeError exception"))


st.sidebar.title("StatEase")
st.sidebar.markdown("[Join our community](#)")