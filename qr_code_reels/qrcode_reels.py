#pip install qrcode
#pip install pillow

import qrcode

link = 'https://instagram.com/pyter.a?igshid=YmMyMTA2M2Y='

qr_reels = qrcode.QRCode(version=1,box_size=5,border=5)

qr_reels.add_data(link)
qr_reels.make()

qr_imagem = qr_reels.make_image(fill_color='black',\
                                 back_color='white')

qr_imagem.save('pytera_ig.png')











