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

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Selecione um jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")


col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f} kg")
st.divider()

st.subheader(f"**Overall:** {player_stats['Overall']}")
st.progress(player_stats['Overall']/100)

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisão", value=f"£ {player_stats['Release Clause(£)']:,}")

columns = ['Age', 'Photo', 'Overall', 'Potential', 'Club Logo', 'Value(£)', 'Wage(£)', 'Release Clause(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Flag']

st.dataframe(df_players[columns], column_config={
    "Overall": st.column_config.ProgressColumn(
        "Overall",
        min_value=0,
        max_value=100,
        format="%d"
    ),
    "Photo": st.column_config.ImageColumn("Foto"),
    "Flag": st.column_config.ImageColumn("Country"),
    "Club Logo": st.column_config.ImageColumn("Club Logo")},
    )



st.write("### Dados dos Jogadores")
st.dataframe(df_data)



