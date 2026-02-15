import qrcode

data = "https://alexcorteno7788.github.io/Pagina-Majo/"

img = qrcode.make(data)

img.save("QR.png")

print("✅ Código QR generado y guardado como mi_qr.png")
