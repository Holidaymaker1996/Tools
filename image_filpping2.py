from PIL import Image


def rorate_left(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 左转 90 度后的图像
    """
    x, y = image.size
    img = Image.new('RGBA', (y, x))
    for i in range(y):
        for j in range(x):
            position = (i, j)
            old_position = (-j, i)
            # print(position, old_position)  左闭右开
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img


def rorate_right(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 右转 90 度后的图像
    """
    x, y = image.size
    img = Image.new('RGBA', (y, x))
    for i in range(y):
        for j in range(x):
            position = (i, j)
            old_position = (j, -i)
            # print(position, old_position)  左闭右开
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img


def rorate_180(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 旋转 180 度后的图像
    """
    x, y = image.size
    img = Image.new('RGBA', (x, y))
    for i in range(x):
        for j in range(y):
            position = (i, j)
            old_position = (x - i - 1, y - j - 1)
            # print(position, old_position)  左闭右开
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img
    
    
def main():
    img = Image.open('a.jpg')
    img = img.convert('RGBA')
    i = rorate_left(img)
    # i = rorate_right(img)
    # i = rorate_180(img)
    # i.show()
    i.save('b.png')
    


if __name__ == '__main__':
    main()
