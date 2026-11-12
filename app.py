
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

c1_1, c2_1, c3_1, c4_1 = st.columns(4)
with c1_1:
    st.metric("Total passengers", len(data))
with c2_1:
    st.metric("Survived Rate", f"{len(data[data['survival'] == 'Survived']) / len(data) * 100:.1f}%")
with c3_1:
    st.metric("Median Age", round(data["age"].median(), 1))
with c4_1:
    st.metric("Median Fare", round(data["fare"].median(), 1))


c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(plot_family_size(data), use_container_width=True)

with c2:
    st.plotly_chart(plot_outcome(data), use_container_width=True)
