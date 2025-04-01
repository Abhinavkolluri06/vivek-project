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

# Example usage
convert_docx_to_pdf('vivek.docx', 'output_docx_to_pdf.pdf')
convert_html_to_pdf('index.html', 'output_html_to_pdf.pdf')
