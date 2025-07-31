import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(layout="wide", page_title="Scout do Campeonato", page_icon="🏆")

# Cores personalizadas (opcional)
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: white;
    }
    .block-container {
        padding-top: 2rem;
    }
    .css-18e3th9 {
        background-color: #1e1e1e !important;
    }
    .css-1d391kg {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 Painel de Scout - Campeonato da Empresa")

# Carregar dados
df = pd.read_excel("Scout_Champions_Exemplo.xlsx")

# Sidebar
times = df["Time"].unique()
time_selecionado = st.sidebar.selectbox("Selecione um time", sorted(times))

df_time = df[df["Time"] == time_selecionado]

st.subheader(f"📊 Estatísticas do {time_selecionado}")

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    try:
        logo_path = f"logos/{time_selecionado}.png"
        if os.path.exists(logo_path):
            st.image(logo_path, width=120)
        else:
            st.image("https://upload.wikimedia.org/wikipedia/commons/9/99/OOjs_UI_icon_userAvatar.svg", width=100)
    except:
        pass

with col2:
    st.dataframe(df_time.style.format({"Gols": "{:.0f}", "Assistências": "{:.0f}", "Nota": "{:.1f}"}), 
                 height=400, 
                 use_container_width=True)

# Totais do time
total_gols = df_time["Gols"].sum()
total_assist = df_time["Assistências"].sum()

with col3:
    st.markdown("### 🎯 Totais do Time")
    st.metric("Gols", int(total_gols))
    st.metric("Assistências", int(total_assist))

st.markdown("---")

# Craque da Rodada
st.subheader("🏅 Craque da Rodada")

destaque = df.loc[df["Nota"].idxmax()]
col_d1, col_d2 = st.columns([1, 3])

with col_d1:
    try:
        logo_path = f"logos/{destaque['Time']}.png"
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
    except:
        pass

with col_d2:
    st.markdown(f"### {destaque['Jogador']} ({destaque['Time']})")
    st.metric("Nota", destaque["Nota"])
    st.write(f"**Gols:** {destaque['Gols']} | **Assistências:** {destaque['Assistências']}")
