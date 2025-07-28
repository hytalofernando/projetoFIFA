import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime



if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por: [@Hytalo Fernando]")


btn = st.button("🔍 Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/nyagami/ea-sports-fc-25-database-ratings-and-stats")

st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2023 fonece informações detalhadas sobre os jogadores, incluindo:
    - Nome
    - Posição
    - Equipe
    - Nacionalidade
    - Valor de mercado
    - Classificação geral
    - Estatísticas de jogo
""")

