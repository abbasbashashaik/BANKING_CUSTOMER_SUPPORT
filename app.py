import streamlit as st
import requests
API_URL="http://127.0.0.1:8000"

st.set_page_config(page_title="question_answerBot",page_icon=":robot:")
st.header(body="**Q&A BOT**")
question=st.chat_input(placeholder="enter question")
bt=st.button(label="check health")
if bt:
    status_check=requests.get(
        API_URL
    )
    data=status_check.json()
    st.write(data["message"])
if question:
    res=requests.post(
        f"{API_URL}/ask",
        json={"q":question}
    )
    answer=res.json()
    st.write(answer)
