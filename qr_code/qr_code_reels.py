import qrcode 

link = 'https://github.com/Rhuan-Messias'

qr_reels = qrcode.QRCode(version=1,box_size=5,border=5) 

#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
#The box_size parameter controls how many pixels each “box” of the QR code is.
#The border parameter controls how many boxes thick the border should be.

qr_reels.add_data(link)
qr_reels.make()
# o método make() faz o QR code ser gerado, com o link que adicioinamos a ele 

qr_imagem = qr_reels.make_image(fill_color= 'black', back_color = 'white')

#fill_color é a cor da linha e back_color é o background 

qr_imagem.save('github_rhuan.png') #png para mensagens, jpg para o link 

#pillow save() function to save the qr images
