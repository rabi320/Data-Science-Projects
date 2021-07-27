import streamlit as st
import pandas as pd
import numpy as np
import pickle
#image

#pipeline tools
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from PIL import Image



image = Image.open('Data/diamond.jpg')
st.image(image)

#title
st.write("""
# Diamond Price Estimator 💎
How much is your daimond worth?
""")
st.write('---')