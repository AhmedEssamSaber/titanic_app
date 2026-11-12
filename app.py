
import streamlit as st

import pandas as pd
import plotly.express as px
import plotly.io as pio

from utills.data import load_data
from utills.config import ORDERS, COLORS


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
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    outcome = data["survival"].value_counts().reset_index()

    fig = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
                color_discrete_map=COLORS, title="Died vs survived")
    st.plotly_chart(fig, use_container_width=True)
