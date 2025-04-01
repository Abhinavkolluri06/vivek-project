import pypandoc

# Convert DOCX to PDF
def convert_docx_to_pdf(input_file, output_file):
    try:
        output = pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)
        print(f"Conversion successful! PDF saved to: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

# Convert HTML to PDF
def convert_html_to_pdf(input_file, output_file):
    try:
        output = pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)
        print(f"Conversion successful! PDF saved to: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

print("1.ENTER 1 FOR DOCX TO PDF")
print("2.ENTER 2 FOR HTML TO PDF")
choice = input("")
if choice == "1":
    convert_docx_to_pdf('vivek.docx', 'output_docx_to_pdf.pdf')
elif choice == "2":
    convert_html_to_pdf('.html', 'output_html_to_pdf.pdf')
else:
    print("Wrong Input")
