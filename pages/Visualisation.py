import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.subheader("Histogram")
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15, color="red") #color= "pink"
st.pyplot(fig)

st.subheader("Forex Trends")
df = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['loss', 'neutral', 'profit'],
)

# st.line_chart(df)
st.bar_chart(df)