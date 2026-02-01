# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Thabo's Researcher Profile")

# Collect basic information
name = "Mr. Thabo Rolffy Masoga"
field = "Biochemistry"
institution = "University of Venda"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("publications.csv", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "Masoga")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
thermostability_data = pd.DataFrame({
    "Experiment": ["pfhsp40", "pfhop", "pff1010c", "pfhsp70", "pfhsp90"],
    "Temperature (degCelcius)": [55.0, 60.0, 56.0, 70.5, 68.7],
})

substrate_affinity_data = pd.DataFrame({
    "Protein": ["pfhsp40", "pfhop", "pff1010c", "pfhsp70", "pfhsp90"],
    "Binding Affinity (AI)": [0.8, 0.4, 0.7, 0.6, 0.65],
})


# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["thermostability_data", "substrate_affinity_data"]
)

if data_option == "thermostability_data":
    st.write("### Thermostability Data")
    st.dataframe(thermostability_data)
    # Add widget to filter by Temperature
    temperature_filter = st.slider("Filter by Temperature (degCelcius)", 55.0, 70.5, (55.0, 70.5))
    filtered_temperature = thermostability_data[
        thermostability_data["Temperature (degCelcius)"].between(temperature_filter[0], temperature_filter[1])
    ]
    st.write(f"Filtered Results for Temperature Range {temperature_filter}:")
    st.dataframe(filtered_temperature)

elif data_option == "substrate_affinity_data":
    st.write("### Substrate Affinity Data")
    st.dataframe(substrate_affinity_data)
    # Add widget to filter by Binding Affinity
    affinity_filter = st.slider("Filter by Binding Affinity (AI)", 0.4, 0.8, (0.4, 0.8))
    filtered_affinity = substrate_affinity_data[
        substrate_affinity_data["Binding Affinity (AI)"].between(affinity_filter[0], affinity_filter[1])
    ]
    st.write(f"Filtered Results for Binding Affinity Range {affinity_filter}:")
    st.dataframe(filtered_affinity)


# Add a contact section
st.header("Contact Information")
email = "thabo.masoga0618@gmail.com"

st.write(f"You can reach {name} at {email}.")