#create a simple qrcode file
#install libraries
#write code
import qrcode
#We can store this YouTube URL into a variable called website_link:
website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
#Next, we want to create an instance of qrcode. Since it's a Python library, we can call the package constructor to create a qrcode object, customized to our specifications.
#in this example, we will create a QR code with a version of 1, and a box size and border size of 5
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')

