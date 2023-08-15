import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Simple Streamlit App")

# Header
st.header("Welcome to Streamlit!")

# Subheader
st.subheader("This is a basic example of a Streamlit app.")

# Text
st.write("Streamlit is great for creating interactive web apps for data science!")

# Markdown
st.markdown("## Let's explore some data:")

# Dataframe
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 28, 22],
    "Score": [85, 90, 78, 92]
})

st.write("Here's a sample DataFrame:")
st.dataframe(data)

# Line chart
st.markdown("### Line Chart:")
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['A', 'B'])
st.line_chart(chart_data)

# Bar chart
st.markdown("### Bar Chart:")
bar_chart_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [15, 30, 10, 45]
})
st.bar_chart(bar_chart_data, x='Category', y='Values')

# Interactive widgets
st.markdown("### Interactive Widgets:")
option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

number = st.slider("Select a number", 0, 100, 50)
st.write("You selected:", number)

if st.button("Say Hello"):
    st.write("Hello, world!")

# Display image
st.markdown("### Display an Image:")
image = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
st.image(image, caption="Streamlit Logo", use_column_width=True)

# Display audio
st.markdown("### Display Audio:")
audio = "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3"
st.audio(audio, format="audio/mp3")

# Display video
st.markdown("### Display Video:")
video = "https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4"
st.video(video, format="video/mp4")

# Display map
st.markdown("### Display Map:")
st.map(data)
