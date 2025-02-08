import qrcode

class QRCodePDFEmbedder:
    def __init__(self, pdf_url:str, output_qr_path:str):
        self.pdf_url = pdf_url
        self.output_qr_path = output_qr_path

    def generate_qr(self):
        print(f'Hello world!')