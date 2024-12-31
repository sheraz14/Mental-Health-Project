import streamlit as st
import ollama

# Initialize conversation history 
st.session_state.setdefault('conversation_history', [])

def generate_response(user_input):
    # Add user input to conversation history
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    
    # Generate AI response using Ollama
    try:
        print("Sending request to Ollama...")  # Debugging
        response = ollama.chat(model="llama3:8b", messages=st.session_state['conversation_history'])
        print("Received response from Ollama:", response)  # Debugging
        ai_response = response['message']['content']
    except Exception as e:
        st.error(f"Error generating response: {e}")
        print("Error:", e)  # Debugging
        return None
    
    # Add AI response to conversation history
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

# Streamlit app
st.title("Mental Health Support Agent")

# Display conversation history
for msg in st.session_state['conversation_history']:
    role = "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

# User input
user_message = st.text_input("How can I help you today?")

if user_message:
    with st.spinner("Thinking..."):
        ai_response = generate_response(user_message)
        if ai_response:
            st.markdown(f"**AI:** {ai_response}")
