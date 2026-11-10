import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)

col1.image(img, caption="img")

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
rgb = cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB)
col2.image(rgb, caption="H")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

fator = col1.slider("Saturação", 0.0, 3.5, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Saturação")

fator_brilho = col1.slider("Brilho", 0.0, 2.0, 1.5)
v = hsv[:, :, 2].astype(float)
v = v * fator_brilho
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Brilho")

giro = col2.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
girada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
col2.image(girada, caption="Matiz girada")

# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)

escala = np.zeros((1, 12, 3), dtype=np.uint8)
escala[0, :, 0] = np.arange(0, 180, 15)
escala[0, :, 1] = 255
escala[0, :, 2] = 255

rgb = cv2.cvtColor(escala, cv2.COLOR_HSV2RGB)
col1.image(rgb.repeat(40, axis=0).repeat(40, axis=1),caption="escala")

h_min, h_max = col1.slider("Faixa de H na escala",0,179,(90, 130))

mascara = cv2.inRange(escala,(h_min, 0, 0),(h_max, 255, 255))

col2.image(mascara.repeat(40, axis=0).repeat(40, axis=1),caption="mascara")

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

h_min, h_max = col1.slider("Faixa de H",0,179,(140, 179))

mascara = cv2.inRange(hsv,(h_min, 60, 40),(h_max, 255, 255))

col1.image(mascara, caption="mascara")

so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0
col2.image(so_cor, caption="Só a cor escolhida")

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)

altura, largura = img.shape[0], img.shape[1]

y = col1.slider("y", 0, altura - 1, altura // 4)
x = col1.slider("x", 0, largura - 1, largura // 4)
t = col1.slider("tamanho", 10, largura, largura // 3)

recorte = img[y:y + t, x:x + t]
col1.image(recorte, caption="recorte")

nova = img.copy()
regiao = nova[y:y + t, x:x + t]
negativo = 255 - regiao
nova[y:y + t, x:x + t] = negativo

col2.image(nova, caption="Negativo no recorte")

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)

horizontal = img[:, ::-1]
col1.image(horizontal, caption="Espelhada na horizontal")

vertical = img[::-1, :]
col2.image(vertical, caption="Espelhada na vertical")