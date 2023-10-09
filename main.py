import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        api_key = st.sidebar.text_input(
            label="What is your OpenAI API key?",
            max_chars=200,
            key="api_key",
        )
        youtube_url = st.sidebar.text_area(
            label="What is the Youtube video url?",
            max_chars=200,
        )
        query = st.sidebar.text_area(
            label="Ask me about the video",
            max_chars=100,
            key="query",
        )

        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url and api_key:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response = lch.get_response_from_query(db, query, api_key)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, 80))
        