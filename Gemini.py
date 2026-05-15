import streamlit as st
from google import genai

st.secrets["GOOGLE_API_KEY"] = userdata.get('GeminiAPI')

# Configura o cliente da SDK do Gemini
from google import genai
client = genai.Client()
MODEL_ID = "gemini-2.5-flash"

from IPython.display import HTML, Markdown
resposta = client.models.generate_content(
    model=MODEL_ID,
    contents='Me diga o o top 5 de claudinho e buxexa, dando nota para as músicas.',
)
# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))

resposta.candidates
