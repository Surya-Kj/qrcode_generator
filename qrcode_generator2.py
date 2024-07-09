import qrcode
# from PIL import Image
import qrcode.constants
import qrcode.image.styles
# import qrcode.image.styles.colormasks
import qrcode.main
qr = qrcode.main.QRCode(version=1,
                        error_correction=qrcode.ERROR_CORRECT_H,
                        box_size=10,
                        border=4)
qr.add_data("https://www.wscubetech.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("wscube_qr2.png")
  