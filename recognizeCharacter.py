import easyocr


def karakterTanıma(croppedImage):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(croppedImage)
    text = result[0][-2]
    return text
