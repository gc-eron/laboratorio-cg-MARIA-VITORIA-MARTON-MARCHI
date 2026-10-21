import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira do Benin")
bandeira = np.zeros((10, 15, 3), dtype=np.uint8)
bandeira[:, :6] = (0, 135, 81)
bandeira[:5, 6:] = (252, 209, 22)
bandeira[5:, 6:] = (232, 17, 45)
st.image(ampliar(bandeira))