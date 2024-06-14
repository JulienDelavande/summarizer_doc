import PyPDF2
import docx

def read_files(uploaded_files):
    # uploaded_files = {f'file_{i}': (file.name, file.getvalue()) for i, file in enumerate(files)}
    files = []
    print(uploaded_files)
    for uploaded_file in uploaded_files:
        file = uploaded_file.file
        if uploaded_file.content_type == "application/pdf":
            text = read_pdf(file)
        elif uploaded_file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = read_docx(file)
        else:
            text = file.read().decode("utf-8")
        files.append(text)

def read_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF file: {e}"

def read_docx(file):
    try:
        doc = docx.Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error reading DOCX file: {e}"
