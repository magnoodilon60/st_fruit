import streamlit as st
from PIL import Image
from gtts import gTTS
import random
import time
import os
from googletrans import Translator

# Lista de nomes e caminhos das imagens
image_data = [
    {"nome": "Ameixa", "imagem": "Ameixa.jpg"},
    {"nome": "Ameixas Pretas Secas", "imagem": "Ameixas Pretas Secas.jpg"},
    {"nome": "Amora", "imagem": "Amora.jpg"},
    {"nome": "Banana", "imagem": "Banana.jpg"},
    {"nome": "Cacau", "imagem": "Cacau.jpg"},
    {"nome": "Caju", "imagem": "Caju.jpg"},
    {"nome": "Caqui", "imagem": "Caqui.jpg"},
    {"nome": "Carambola", "imagem": "Carambola.jpg"},
    {"nome": "Cereja", "imagem": "Cereja.jpg"},
    {"nome": "Coco ", "imagem": "Coco.jpg"},
    {"nome": "Damasco", "imagem": "Damasco.jpg"},
    {"nome": "Figo", "imagem": "Figo.jpg"},
    {"nome": "Framboesa", "imagem": "Framboesa.jpg"},
    {"nome": "Fruta do conde", "imagem": "Fruta do conde.jpg"},
    {"nome": "Goiaba", "imagem": "Goiaba.jpg"},
    {"nome": "Graviola", "imagem": "Graviola.jpg"},
    {"nome": "Groselha", "imagem": "Groselha.jpg"},
    {"nome": "Jabuticaba", "imagem": "Jabuticaba.jpg"},
    {"nome": "Jaca", "imagem": "Jaca.jpg"},
    {"nome": "Kiwi", "imagem": "Kiwi.jpg"},
    {"nome": "Laranja", "imagem": "Laranja.jpg"},
    {"nome": "Lichia", "imagem": "Lichia.jpg"},
    {"nome": "Limão", "imagem": "Limão.jpg"},
    {"nome": "Fruta Maçã", "imagem": "Maçã.jpg"},
    {"nome": "Mamão", "imagem": "Mamão.jpg"},
    {"nome": "Manga", "imagem": "Manga.jpg"},
    {"nome": "Maracujá", "imagem": "Maracujá.jpg"},
    {"nome": "Marmelo", "imagem": "Marmelo.jpg"},
    {"nome": "Mexerica", "imagem": "Mexerica.jpg"},
    {"nome": "Mirtilo", "imagem": "Mirtilo.jpg"},
    {"nome": "Nectarina", "imagem": "Nectarina.jpg"},
    {"nome": "Nêspera", "imagem": "Nêspera.jpg"},
    {"nome": "Pêra", "imagem": "Pera.jpg"},
    {"nome": "Pêssego", "imagem": "Pêssego.jpg"},
    {"nome": "Romã", "imagem": "Romã.jpg"},
    {"nome": "Tamarindo", "imagem": "Tamarindo.jpg"},
    {"nome": "Tangerina", "imagem": "Tangerina.jpg"},
    {"nome": "Uva", "imagem": "Uva.jpg"},

]
img = Image.open('frutas.jpg')
st.image(img,use_column_width=True)
st.title('Apredendo o nome das frutas em Ingês')

# Mostra as imagens
# columns = st.columns(3)
# for i, data in enumerate(image_data):
#     with columns[i % 3]:
#         img = Image.open(data["imagem"])
#         st.image(img, caption=data["nome"], use_column_width=True)

# Botão para acionar a roleta
if st.button('Clique aqui'):
    #st.write('Girando a roleta...')
    time.sleep(3)  # Simulando o giro da roleta por 1 segundo
    chosen_fruit = random.choice(image_data)
    translator = Translator()
    st.image(Image.open(chosen_fruit["imagem"]), caption=chosen_fruit["nome"] + ' -- ' + translator.translate(chosen_fruit["nome"], dest='en').text, use_column_width=True)
    #st.image(Image.open(chosen_fruit["imagem"]), caption=chosen_fruit["nome"], use_column_width=True)

    # Traduzindo o nome da fruta para o inglês
    #translator = Translator()
    translated_name = translator.translate(chosen_fruit["nome"], dest='en').text

    # Vocalização do nome da fruta em inglês
    tts = gTTS(text=translated_name, lang='en')
    tts.save("chosen_fruit.mp3")
    st.audio("chosen_fruit.mp3", format="audio/mp3")
    os.remove("chosen_fruit.mp3")