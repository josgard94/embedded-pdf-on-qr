import qrcode

class QRCodePDFEmbedder:
    def __init__(self, pdf_url:str, output_qr_path:str):
        self.pdf_url = pdf_url
        self.output_qr_path = output_qr_path

    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.pdf_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.output_qr_path)
        print(f'QR code saved to {self.output_qr_path}')