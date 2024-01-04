import qrcode

feature = qrcode.QRCode(version=1, box_size=10, border=1)
feature.add_data("https://mreshank.github.io")
feature.make(fit=True)
generate_image = feature.make_image(fill_color="blue", back_color="black")
generate_image.save("GeneratedImages/qrcodex.png")