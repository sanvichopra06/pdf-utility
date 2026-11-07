import streamlit as st
import tempfile
import os
from pdf_merger import merge_pdf
from image_converter import images_to_pdf

if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = None

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #FFF0F3;
}

/* Main content area */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Main title */
h1 {
    color: #e83174;
    font-family: Georgia, serif;
    font-weight: bold;
}

/* Section headings */
h2, h3 {
    color: #C44569;
    font-family: Georgia, serif;
}

/* Normal text */
p, label {
    color: #6D3045;
}

/* Buttons */
.stButton > button {
    background-color: #D85A7F;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.5rem 1.5rem;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #B83B65;
    color: white;
    border: none;
}

/* File uploader */
[data-testid="stFileUploaderDropzone"] {
    background-color: #FFF8FA;
    border: 2px dashed #E8A1B2;
    border-radius: 15px;
}

/* Download button */
.stDownloadButton > button {
    background-color: #A53860;
    color: white;
    border: none;
    border-radius: 12px;
}

.stDownloadButton > button:hover {
    background-color: #842D4D;
    color: white;
}

/* Dropdown */
.stSelectbox [data-baseweb="select"] {
    background-color: #FFF8FA;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


st.title("PDF Utility")
st.write("Your documents, simplified.")

st.divider()

st.subheader("Choose Your Tool")

col1, col2 = st.columns(2)

with col1:
    if st.button("Merge PDFs", use_container_width=True):
        st.session_state.selected_tool = "Merge PDF Files"

with col2:
    if st.button("Images to PDF", use_container_width=True):
        st.session_state.selected_tool = "Convert Images to PDF"

if st.session_state.selected_tool is None:
    st.info("Select a tool above to get started.")

if st.session_state.selected_tool == "Merge PDF Files":
    st.subheader("Merge PDF Files")

    uploaded_files = st.file_uploader("Upload PDF Files", 
                                    type= ["pdf"], 
                                    accept_multiple_files=True)
    if uploaded_files:
        st.write("Uploaded files: ")
        for file in uploaded_files:
            st.write(file.name)

        if st.button("Merge PDFs"):
            st.write("Merging!")
            pdf_paths = []
            with tempfile.TemporaryDirectory() as temp_dir:
                for file in uploaded_files:
                    path = os.path.join(temp_dir, file.name)
                    with open(path, "wb") as f:
                        f.write(file.getbuffer())
                    pdf_paths.append(path)
                output_path = os.path.join(temp_dir, "merged.pdf")

                success = merge_pdf(pdf_paths, output_path)

                if success:
                    with open(output_path, "rb") as f:
                        st.download_button(
                            label="Download Merged PDF",
                            data=f,
                            file_name="merged.pdf",
                            mime="application/pdf"
                )
                        
if st.session_state.selected_tool == "Convert Images to PDF":
    st.subheader("Convert Images to PDF")

    uploaded_imgs = st.file_uploader("Upload Images", 
                                    type= ["jpg", "jpeg", "png"], 
                                    accept_multiple_files=True)
    if uploaded_imgs:
        st.write("Uploaded images: ")
        for file in uploaded_imgs:
            st.write(file.name)

        if st.button("Merge Images"):
            st.write("Converting Images!")
            image_paths = []
            with tempfile.TemporaryDirectory() as temp_dir:
                for file in uploaded_imgs:
                    path = os.path.join(temp_dir, file.name)
                    with open(path, "wb") as f:
                        f.write(file.getbuffer())
                    image_paths.append(path)
                output_path = os.path.join(temp_dir, "merged_images.pdf")

                success = images_to_pdf(image_paths, output_path)

                if success:
                    with open(output_path, "rb") as f:
                        st.download_button(
                            label="Download Merged Images",
                            data=f,
                            file_name="merged_images.pdf",
                            mime="application/pdf"
                            )
