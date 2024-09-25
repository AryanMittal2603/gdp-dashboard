
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np


map_data = pd.DataFrame(
    np.random.randn(10, 2) / [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
