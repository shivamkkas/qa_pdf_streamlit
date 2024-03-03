# PDF Question Answering Streamlit App

This Streamlit app allows users to upload a PDF document and ask questions related to its content. The app extracts text from the uploaded PDF using the PyPDF2 library and uses a pre-trained question-answering model from the Hugging Face Transformers library to provide answers to user questions.

## Dependencies

- **Streamlit**: A Python library for creating web apps for machine learning and data science projects.
- **PyPDF2**: A Python library for working with PDF files, used here to extract text from PDF documents.
- **transformers**: A Python library by Hugging Face for natural language processing tasks, such as question answering. It provides pre-trained models and pipelines for various NLP tasks.

You can install these dependencies using the following command:

pip install -r requirements.txt


## Usage

1. Run the Streamlit app using the following command:

streamlit run app.py


2. In the web browser, you will see the app interface.
   
3. Upload a PDF file by clicking on the "Upload a PDF file" button.

4. Once the PDF is uploaded, you can view the extracted text from the PDF.
   
5. Enter a question related to the PDF content in the text box provided.
   
6. Click on the "Get Answer" button to get the answer to your question.

## File Structure

The project's file structure is as follows:

pdf-qa-streamlit/
│
├── app.py # Main Streamlit application file
├── README.md # Project README file
├── requirements.txt # List of Python dependencies
└── uploads/ # Folder to store uploaded PDF files


## Contributing

Contributions to the project are welcome! Feel free to submit bug reports, suggest improvements, or open pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the PyPDF2 library for PDF text extraction and the transformers library for question answering.

## Contact

For questions or inquiries, please contact [Shivam Kashyap](mailto:kashyapboyshivam12@gmail.com).

## Links

- [GitHub Repository](https://github.com/your_username/pdf-qa-streamlit)
