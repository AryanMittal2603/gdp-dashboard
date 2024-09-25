
import pandas as pd
import math
from pathlib import Path
import streamlit as st
import numpy as np


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
