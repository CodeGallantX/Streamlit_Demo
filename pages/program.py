import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the page
st.set_page_config(
    page_title="StatEase - Statistics Hub",
    page_icon="📊",
    layout="wide"
)

# Initialize session state for dataset
if "uploaded_data" not in st.session_state:
    st.session_state["uploaded_data"] = None

# App title and description
st.title("📊 StatEase")
st.write("A user-friendly statistics app for descriptive analysis, visualizations, and more!")

# Sidebar Navigation
st.sidebar.title("Menu")
options = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Upload Dataset", "Descriptive Statistics", "Data Visualizations", "Manual Data Input"]
)

# Home Page
if options == "Home":
    st.subheader("Welcome to StatEase!")
    st.write("""
        - Upload your dataset to begin statistical analysis.
        - Compute descriptive statistics and measures of central tendency.
        - Visualize your data with interactive charts and plots.
        - Manually input data for grouped or ungrouped frequency tables.
        - Future feature: Inferential statistics and hypothesis testing.
    """)

# Upload Dataset Section
elif options == "Upload Dataset":
    st.subheader("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload your CSV or Excel file:", type=["csv", "xlsx"])

    if uploaded_file:
        # Load CSV or Excel file
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Store dataset in session state
        st.session_state["uploaded_data"] = df

        st.write("**Preview of Uploaded Data**")
        st.dataframe(df.head())

        # Summary statistics
        st.write("**Dataset Summary**")
        st.write(df.describe())

        # Handle missing values
        st.write("**Missing Values**")
        st.write(df.isnull().sum())
    else:
        st.info("Please upload a file to proceed.")

# Descriptive Statistics Section
elif options == "Descriptive Statistics":
    st.subheader("Descriptive Statistics")

    if st.session_state["uploaded_data"] is None:
        st.warning("Please upload a dataset first in the 'Upload Dataset' section.")
    else:
        df = st.session_state["uploaded_data"]
        st.write("**Choose Columns for Analysis**")
        numeric_columns = df.select_dtypes(include=np.number).columns
        selected_columns = st.multiselect("Select numeric columns:", numeric_columns)

        if selected_columns:
            selected_data = df[selected_columns]
            st.write("**Summary Statistics**")
            st.write(selected_data.describe())

            # Compute central tendencies
            st.write("**Central Tendency Measures**")
            for col in selected_columns:
                st.write(f"- **{col}**: Mean = {selected_data[col].mean():.2f}, Median = {selected_data[col].median():.2f}, Mode = {selected_data[col].mode()[0]}")

            # Measures of dispersion
            st.write("**Measures of Dispersion**")
            for col in selected_columns:
                st.write(f"- **{col}**: Variance = {selected_data[col].var():.2f}, Std. Dev. = {selected_data[col].std():.2f}")

# Data Visualizations Section
elif options == "Data Visualizations":
    st.subheader("Data Visualizations")

    if st.session_state["uploaded_data"] is None:
        st.warning("Please upload a dataset first in the 'Upload Dataset' section.")
    else:
        df = st.session_state["uploaded_data"]
        st.write("**Choose Columns for Visualization**")
        all_columns = df.columns
        selected_columns = st.multiselect("Select columns to visualize:", all_columns)

        if selected_columns:
            st.write("**Available Plots**")
            plot_type = st.selectbox("Select a plot type:", ["Histogram", "Boxplot", "Scatter Plot"])

            if plot_type == "Histogram":
                for col in selected_columns:
                    st.write(f"**Histogram for {col}**")
                    plt.figure(figsize=(8, 4))
                    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
                    st.pyplot(plt)

            elif plot_type == "Boxplot":
                for col in selected_columns:
                    st.write(f"**Boxplot for {col}**")
                    plt.figure(figsize=(8, 4))
                    sns.boxplot(y=df[col], color="orange")
                    st.pyplot(plt)

            elif plot_type == "Scatter Plot":
                if len(selected_columns) < 2:
                    st.warning("Please select at least two columns for a scatter plot.")
                else:
                    x_axis = st.selectbox("Select X-axis:", selected_columns)
                    y_axis = st.selectbox("Select Y-axis:", selected_columns)

                    st.write(f"**Scatter Plot: {x_axis} vs {y_axis}**")
                    plt.figure(figsize=(8, 4))
                    sns.scatterplot(x=df[x_axis], y=df[y_axis], color="green")
                    st.pyplot(plt)

# Manual Data Input Section
elif options == "Manual Data Input":
    st.subheader("Manual Data Input")
    input_type = st.radio("Choose Data Input Type:", ["Ungrouped Data", "Grouped Data"])

    if input_type == "Ungrouped Data":
        st.write("Enter ungrouped data points in the table below:")
        num_points = st.number_input("Number of data points:", min_value=1, max_value=100, value=5)

        # Create a table for input
        ungrouped_data = pd.DataFrame({"Data Points": [0] * num_points})
        edited_data = st.experimental_data_editor(ungrouped_data)
        st.write("**Entered Data:**")
        st.write(edited_data)

    elif input_type == "Grouped Data":
        st.write("Enter grouped data in the table below:")
        num_classes = st.number_input("Number of classes:", min_value=1, max_value=10, value=5)

        # Create a table for input
        grouped_data = pd.DataFrame({
            "Class Interval": [""] * num_classes,
            "Frequency": [0] * num_classes
        })
        edited_data = st.experimental_data_editor(grouped_data)
        st.write("**Entered Grouped Frequency Table:**")
        st.write(edited_data)