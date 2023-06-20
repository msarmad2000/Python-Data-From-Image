from PIL import Image
import pytesseract

# Open the image file
image = Image.open('C:\\Users\\hp\\Desktop\\book.png')

# Specify the full path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Split the OCR text into sentences
sentences = text.split('.')

# Iterate over the sentences and print those containing the word "pixel"
for sentence in sentences:
    if 'height' in sentence.lower():
        print(sentence)


# Close the image file
image.close()
