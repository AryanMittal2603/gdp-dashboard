
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
