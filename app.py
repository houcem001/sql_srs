import streamlit as st
import pandas as pd
import duckdb

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
sql_query = st.text_area(label="Ma reqeute")
st.write(sql_query)
result = duckdb.query(sql_query).df()
st.dataframe(result)
