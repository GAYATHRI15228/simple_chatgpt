import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
google_api_key = "AIzaSyBJtHZ1DIEvwFzQGvPE42MdcguR2NhdmSo"
model = ChatGoogleGenerativeAI(api_key=google_api_key, model="gemini-1.5-flash")

def get_bot_response(query):
    try:
        result = model.invoke(query)
        return result.content  
    except Exception as e:
        return f"An error occurred: {e}"
if "history" not in st.session_state:
    st.session_state.history = []
st.title("Generative AI")
user_input = st.text_input("You: ", "")
if st.button("Send"):
    if user_input.strip():
        response = get_bot_response(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})
    else:
        st.write("Please enter a valid input.")
for entry in st.session_state.history:
    st.write(f"You: {entry['user']}")
    st.write(f"Bot: {entry['bot']}")
st.write(" ")
