
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
