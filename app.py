import openai
import streamlit as st

st.title('👩‍💼 Knowledge Assistant')

api_key = st.sidebar.text_input('API Key', type='password')

client = openai.OpenAI(
    api_key= api_key,
    base_url="https://api.aimlapi.com/",
)

def generate_response(system_role, user_input):
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_input},
        ],
        temperature=0.7,
        max_tokens=512,
    )
    chat_completion.choices[0].message.content

with st.form('my_form'):
    system_instructions = st.text_area('Enter System Role:')
    user_query= st.text_area('Enter user content:')
    submitted = st.form_submit_button('Submit')
   
    if submitted:
        try:
            generate_response(system_instructions,user_query )
        except Exception as e:
            print('Failed to upload to ftp: %s', repr(e))
