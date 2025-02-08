from modules.qrcodes_pdf import QRCodesPDFEmbedder

if __name__ == '__main__':
    pdf_url = ''
    output_qr_path = 'qr_code.png'

    embedder = QRCodesPDFEmbedder(pdf_url, output_qr_path)
    embedder.generate_qr()