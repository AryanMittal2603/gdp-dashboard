
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
