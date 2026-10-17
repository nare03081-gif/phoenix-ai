import streamlit as st
from google import genai

st.set_page_config(page_title="Phoenix AI", page_icon="🔥")
st.title("🔥 Phoenix AI")
st.caption("Ձեր սեփական արհեստական բանականության հարթակը")

client = genai.Client(api_key="AQ.Ab8RN6K-xO3pcLLt-C5An2bgYp7DdFMWAjsPC8y6zSfvxVOuMg")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Գրեք ձեր հարցը այստեղ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
