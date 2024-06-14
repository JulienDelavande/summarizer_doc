import streamlit as st
from utils import upload_file
import backend

# Page configuration
st.set_page_config(page_title="Document Summary App", layout="wide")

if 'summaries' not in st.session_state:
    st.session_state['summaries'] = []

# Sidebar
st.sidebar.header("Uploaded Documents")
uploaded_files = st.sidebar.file_uploader("Drag and drop or select files", accept_multiple_files=True, type=["pdf", "docx", "txt"])
button_summarize = st.sidebar.button("Summarize")

if button_summarize:
    if uploaded_files:
        content = upload_file(uploaded_files)
        summary = backend.get_summary(content)
        st.session_state['summaries'].append(summary)
    else:
        st.sidebar.write("No files uploaded yet.")

# Main
st.title("Summary of the docs")

if st.session_state['summaries']:
    st.write(st.session_state['summaries'][-1])
else:
    st.write("Upload documents to get a summary. \n No summaries to display yet.")
