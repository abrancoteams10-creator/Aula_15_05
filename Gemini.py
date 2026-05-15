import streamlit as st
from google import genai

# SENHA DE ACESSO
SENHA_CORRETA = "1895"

st.title("Teste Gemini")

senha = st.text_input("Digite a senha", type="password")

if senha == SENHA_CORRETA:

    # Pega a chave dos secrets do Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]

    # Cria o cliente Gemini
    client = genai.Client(api_key=api_key)

    MODEL_ID = "gemini-2.5-flash"

    st.success("Acesso liberado!")

    prompt = st.text_input("Digite algo")

    if st.button("Enviar"):

        resposta = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )

        st.write(resposta.text)

elif senha != "":
    st.error("Senha incorreta!")
