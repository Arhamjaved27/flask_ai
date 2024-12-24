import streamlit as st

st.title("AIBYTEC'S Chatbot")
st.markdown("this is the tesing message")

def process_chatbot_message(msg):
    st.markdown(msg)
    print("Testing")



# user_input = st.chat_input("Type your question here...")

# if user_input:
    # st.session_state.Conversation.append({"role": "\n\n user", "content": user_input})