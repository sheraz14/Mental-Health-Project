import streamlit as st
import ollama

st.session_state.setdefault('conversation_history', [])

def generate_response(user_input):
    st.session_state['conversation_history'],append({"role":"user", "content":user_input})
    
    response= ollama.chat(model="llama3.1:8b", messages=st.session_state['conversation'])
    

