import PyPDF2

def split_pdf(input_pdf_path, output_pdf_prefix, page_ranges):
    """
    Split a PDF into multiple PDFs based on specified page ranges.
    
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_prefix: Prefix for the output PDF files.
    :param page_ranges: List of tuples specifying the page ranges to split. Each tuple is (start, end).
    """
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    
    for idx, (start, end) in enumerate(page_ranges):
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(start, end + 1):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_pdf_path = f"{output_pdf_prefix}_{idx + 1}.pdf"
        with open(output_pdf_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)
        print(f"Created {output_pdf_path} with pages from {start + 1} to {end + 1}.")

# Example usage:
input_pdf = r"C:\Users\SyandaM\Desktop\Codes_Python\split_pdf\to_be_wroked_on\Supporting-Documents.pdf"
output_pdf_prefix = r"C:\Users\SyandaM\Desktop\Codes_Python\split_pdf\results\split_results"
page_ranges = [(0, 0), (1, 3), (4, 5)]  # Split into three PDFs with specified page ranges

# Split PDF
split_pdf(input_pdf, output_pdf_prefix, page_ranges)