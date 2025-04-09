import streamlit as st
import pandas as pd

st.title("Our Locations 📍")

st.write("""
We’re currently working on mapping out our first installations.

Here are some of our pilot locations. More coming soon!
""")

# Updated location data with Birzeit University
location_data = pd.DataFrame({
    'lat': [31.9720],     # Birzeit University
    'lon': [35.1859]
})

st.map(location_data, zoom=13)

st.markdown("🟢 First location: **Birzeit University**")
