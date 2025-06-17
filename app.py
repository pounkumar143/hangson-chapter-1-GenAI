import streamlit as st
from Ollama import query_ollama

st.set_page_config(page_icon='welcome my for ai world')
st.title('Welcome to My AI World')
prompt=st.text_area('ask me everything', height=200)

if st.button('Generate'):
    with st.spinner('loading for your content...'):
        response = query_ollama(prompt, model="llama3")
        st.markdown('### response:')
        st.write(response)
        