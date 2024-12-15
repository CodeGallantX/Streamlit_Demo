import streamlit as st
import time

st.success("Transfer Successful!")
st.error("Error occurred!")
st.warning("Warning: Network breach imminent")
st.info("You have been selected to participate in the DevSprint3.0 contest")
st.exception(RuntimeError("RuntimeError exception"))



st.balloons()

st.subheader("Progress bar")
st.progress(10)

st.subheader("Wait the execution")
with st.spinner("Wait for it..."):
    time.sleep(10)




st.sidebar.title("StatEase")
st.sidebar.markdown("[Join our community](#)")


st.sidebar.title("StatEase")
st.sidebar.markdown("[Join our community](#)")