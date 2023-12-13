import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("Hello World")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "assistant", "content": prompt})
