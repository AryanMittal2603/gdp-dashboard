
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np

dataframe = np.random.randn(5, 5)
st.dataframe(dataframe)


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
