import os
from pdf_merger import merge_pdf, validate_pdf
from image_converter import images_to_pdf, validate_image

def merge_pdf_main():
    while True:
        try:
            num = int(input("How many PDFs do you want to merge? "))
            if num <=0:
                print("Enter valid number")
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    pdf_list = []
    for i in range(num):
        while True: 
            path= input(f"Enter PDF {i+1} path: ").strip().strip('"').strip("'")
            if not os.path.isfile(path):
                print("File not found, try again")
            elif not path.lower().endswith(".pdf"):
                print("File format not supported")
            elif validate_pdf(path):
                print("PDF uploaded successfully")
                pdf_list.append(path)
                break

    filename = input("Enter output file name: ").strip()
    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"
    merge_pdf(pdf_list, filename)

def convert_image_main():
    while True:
        try:
            num = int(input("How many images do you want to convert? "))
            if num <=0:
                print("Enter valid number")
            else:
                break
        except ValueError:
            print("Please enter a valid number")
    image_list = []
    for i in range(num):
        while True:
            img = input(f"Enter image {i+1} path: ").strip().strip('"').strip("'")

            if not os.path.isfile(img):
                print("File not found, try again")

            elif not img.lower().endswith((".jpg", ".jpeg", ".png")):
                print("File format not supported")

            elif validate_image(img):
                print("Image uploaded successfully")
                image_list.append(img)
                break
    filename = input("Enter output file name: ").strip()

    if not filename.lower().endswith(".pdf"):
        filename += ".pdf"

    images_to_pdf(image_list, filename )



print("PDF Utility Tool")
print()
while True:
    print("1. Merge PDF Files")
    print("2. Convert Images to PDF")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid choice")
        continue

    if choice == 1:
        print("Merging PDFs")
        merge_pdf_main()

    elif choice == 2:
        print("Converting Images to PDF")
        convert_image_main()

    elif choice == 3:
        print("Exit")
        break
    else:
        print("Command Not Found")