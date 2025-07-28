import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Players',
    page_icon='👤',
    layout='wide',
)

df_data = st.session_state["data"]

Clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Selecione um clube", Clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"**{club}**")

columns = ["Age", "Photo", "Overall", "Value(£)", "Wage(£)", "Release Clause(£)", "Joined",
"Height(cm.)", "Weight(lbs.)", "Contract Valid Until"]

st.dataframe(df_filtered[columns], column_config={
    "Overall": st.column_config.ProgressColumn(
        "Overall",
        min_value=0,
        max_value=100,
        format="%d"
    ),
    "Photo": st.column_config.ImageColumn("Foto"),
    "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%d", min_value=0, max_value=df_filtered["Wage(£)"].max()),
    "Flag": st.column_config.ImageColumn("Country")
})