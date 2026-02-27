import qrcode

url = input("Enter the Url: ").strip()

file_path = "C:\\Users\\N I T R O\\OneDrive\\Desktop\\python2.0\\instaqrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
print("Qrcode generated Successfully")