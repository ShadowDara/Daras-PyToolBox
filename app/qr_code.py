import qrcode

def main():
    data = input()

    qr = qrcode.make(data)

    file_name = input()

    qr.save(file_name)

    print("QR-Code wurde gespeichert!")
