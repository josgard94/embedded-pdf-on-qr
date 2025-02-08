from modules.qrcodes_pdf import QRCodePDFEmbedder

if __name__ == '__main__':
    pdf_url = ''
    output_qr_path = 'qr_code.png'

    embedder = QRCodePDFEmbedder(pdf_url, output_qr_path)
    embedder.generate_qr()