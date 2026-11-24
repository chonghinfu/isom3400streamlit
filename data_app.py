import pandas as pd
import streamlit as st

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df = pd.DataFrame(data)
# 2D data--> have column and rows

# Show data with Streamlit elements
st.write("st.dataframe(df)")
st.dataframe(df)                # Interactive table

st.write("st.data_editor(df)")
st.data_editor(df)              # Editable table

st.write("st.table(df)")
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.write("Customize columns")
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'}))
