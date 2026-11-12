
import streamlit as st

import pandas as pd
import plotly.express as px
import plotly.io as pio

from utills.data import load_data
from utills.config import ORDERS, COLORS
from utills.figures import plot_family_size, plot_outcome

df = load_data()
st.set_page_config(layout="wide")
pio.renderers.default = "plotly_mimetype+notebook_connected"   


st.title("Titanic app")


show_data = st.checkbox("Show data")
if show_data:
    st.dataframe(df.head(10), hide_index=True)

classes = st.multiselect("Select classes", df["class"].unique(), default=df["class"].unique())
gender = st.radio("Select gender", ["male", "female"], horizontal=True)

data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]


c1, c2 = st.columns(2)

with c1:
    fig = plot_family_size(data)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    fig = plot_outcome(data)
    st.plotly_chart(fig, use_container_width=True)
