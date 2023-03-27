import streamlit as st
from key import API_KEY
import openai
import pyperclip

openai.api_key = API_KEY


def ask(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ],
    )
    return (response.choices[0]["message"]["content"].strip())


with st.form("my_form", clear_on_submit=False):

    params = st.experimental_get_query_params()
    if "q" in params:
        q = params["q"][0]
    else:
        q = ""
    header = st.text_area(
        "依頼内容", value="以下のメールが来ました。私(=畠山)が返信する必要があります。丁寧な文面を作成してください。")
    description = st.text_area('メール内容', value=q)
    submitted = st.form_submit_button("作文")


if submitted:
    ans = ask("届いたメールの内容:"+str(header)+str(description))
    st.text(ans)
    pyperclip.copy(ans)
