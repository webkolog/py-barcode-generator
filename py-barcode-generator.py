import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display
user_data = input("Enter the data to encode in the barcode: ")
code = barcode.get('code128', user_data, writer=ImageWriter())
filename = code.save("clcoding_barcode")
display(Image(filename=filename))