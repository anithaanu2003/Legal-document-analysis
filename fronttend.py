import streamlit as st
from backend import comp_process

# Assign your OpenAI API key here
api_key = "sk-proj-9ACtFw0uemetBgLcdCXyItAKpaHua9ta0vlbVrhLF-S7BzXUQw4XQg7tK5T3CeQjNi2a2KmeulT3BlbkFJTPnygtI8D37I-0uDUVfIqNJ9jQjxUUdnvThDnessdQVXCfj5zGNatYgL80KHZExpG_gA"

def frontend():
    # Streamlit UI
    st.set_page_config(page_title="Chat with LAWGPT 🤖")
    st.title("Chat with :green[LAWGPT] using Multiple :red[PDF Files] 🤖!")
    question = st.text_input("Ask Your Legal Below: ")

    with st.sidebar:
        st.image("law.jpeg")
        st.subheader("Upload PDFs Here")
        pdfs=st.file_uploader("Upload PDF File", type=["pdf"], accept_multiple_files=True)
        st.button('Process')
        st.write('question')
        
    if pdfs and api_key is not None:  
        if question:                     
            ans=comp_process(apikey=api_key, pdfs=pdfs, question=question)
            st.write(ans)



if __name__ == "__main__":
    frontend()