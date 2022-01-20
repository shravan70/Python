

def main():
    try:
        im = Image.open('/Users/shannu/Desktop/image.jpeg')
        width, height = im.size
        print(width, height)
        im = im.rotate(180)

    except IOError:
        pass
