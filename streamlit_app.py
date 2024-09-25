
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np

st.write("Printing Streamlit Dataframe (st.dataframe) :")

dataframe = np.random.randn(5, 5)
st.dataframe(dataframe)

st.write("Printing pandas directly:")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
