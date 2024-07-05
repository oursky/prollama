import streamlit as st
import ollama
import time


def askllm(message, model='llama3'):
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': message}])
        return response['message']['content']
    except Exception as e:
        error_message = str(e).lower()
        return f"An error occurred with model '{model}': {str(e)}"


def stream_response(messages):
    lines = messages.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            yield word + " "
            time.sleep(0.1)
        yield "\n"


def show_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def main():
    st.set_page_config(
        page_title="Prollama",
        page_icon="favicon.png",
        initial_sidebar_state="collapsed",
        menu_items=None
    )
    
    st.header(":blue[ProLlama]")
    user_input = st.chat_input("Enter your prompt here", key="1")

    # Show placeholder text or messages in session
    if 'messages' not in st.session_state:
        intro_line = f"""Greetings! Chat securely with ProLlama, your local AI assistant. How can I help you today?"""
        st.caption(intro_line)
        st.session_state['messages'] = []
    show_messages()

    if user_input:
        with st.chat_message("user"): # Receive user prompt
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        messages = "\n".join(msg["content"] for msg in st.session_state.messages)
        response = askllm(messages) # Send prompt to LLM
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): # Show response to user
            st.write_stream(stream_response(response))
    elif st.session_state['messages'] is None:
        st.info("Enter a prompt to start the conversation")


if __name__ == "__main__":
    main()
