# importing dependicies
import os
import streamlit as st
import PyPDF2
from transformers import pipeline

# set up a question-answering pipeline

qa_pipeline = pipeline("question-answering",model="distilbert-base-cased-distilled-squad")
#qa_pipeline = pipeline("question-answering",model="bert-large-uncased-whole-word-masking-finetuned-squad")
# this function is used for extracting text from pdf
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def getanswer(context, question):
    # this function for getting answer of questions
    answer = qa_pipeline(question=question, context=context)
    return answer["answer"]

def main():
    st.title("PDF Question Answering App")
    # this is for file uploading
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # saved uploaded file in "uploads " folder
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
            with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())

        # extracting text from pdf using function"extract_text_from_pdf"
        pdf_text = extract_text_from_pdf(os.path.join("uploads", uploaded_file.name))

        # for displaying extracted data
        st.subheader("Text Extracted from PDF:")
        st.text(pdf_text)

        # ask questions related to your pdf
        question = st.text_input("Ask a question about the PDF content")

        if st.button("Get Answer"):
            if question:
                # Get the answer to the user's question
                answer = getanswer(pdf_text, question)
                st.success("Answer: {}".format(answer))
            else:
                st.error("Please enter a question.")

if __name__ == "__main__":
    main()
