from pypdf import PdfWriter, PdfReader

def validate_pdf(path):
    try:
        reader = PdfReader(path)
        print("Valid PDF")
        return True
        
    except Exception:
        print("Invalid/Corrupted PDF")
        return False


def merge_pdf(pdf_files, merged_file):
    writer = PdfWriter()
    try: 
        for file in pdf_files:
            writer.append(file)
        with open(merged_file, "wb") as output:
            writer.write(output)
        print("PDFs merged successfully!")
        return True
    
    except Exception as e:
        print(f"Error {e}")
        return False

    finally:
         writer.close()