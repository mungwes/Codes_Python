import PyPDF2

def delete_pages(input_pdf_path, output_pdf_path, pages_to_delete):
    """
    Delete specified pages from a PDF.
    
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to the output PDF file.
    :param pages_to_delete: List of page numbers to delete (0-indexed).
    """
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        if page_num not in pages_to_delete:
            pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(output_pdf_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)
    print(f"Pages {pages_to_delete} deleted successfully.")

def add_pages(input_pdf_path, pages_to_add_paths, output_pdf_path):
    """
    Add specified pages to a PDF.
    
    :param input_pdf_path: Path to the input PDF file.
    :param pages_to_add_paths: List of paths to the PDF files whose pages are to be added.
    :param output_pdf_path: Path to the output PDF file.
    """
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    for add_pdf_path in pages_to_add_paths:
        add_pdf_reader = PyPDF2.PdfReader(add_pdf_path)
        for page in add_pdf_reader.pages:
            pdf_writer.add_page(page)
    
    with open(output_pdf_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)
    print(f"Pages from {pages_to_add_paths} added successfully.")

# Example usage:
input_pdf = r'C:\Users\SyandaM\Desktop\Codes_Python\delete_add_pdf\to_be_wroked_on\Supporting-Documents.pdf'
output_pdf_delete = r'CC:\Users\SyandaM\Desktop\Codes_Python\delete_add_pdf\results\output_deleted.pdf'
output_pdf_add = r'C:\Users\SyandaM\Desktop\Codes_Python\delete_add_pdf\results\output_added.pdf'
pages_to_delete = [0,1,2,4,5,6]  # Deleting the first and second pages (0-indexed)
#pages_to_add = ['add_page1.pdf', 'add_page2.pdf']  # Paths to the PDF files whose pages you want to add

# Delete pages
delete_pages(input_pdf, output_pdf_delete, pages_to_delete)

# Add pages
#add_pages(input_pdf, pages_to_add, output_pdf_add)
