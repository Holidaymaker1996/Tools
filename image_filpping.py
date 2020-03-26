from PIL import Image

# 生成一个宽高都是 100 的 rgba 模式的图片
# img = Image.new('RGBA', (100, 100))

log = print


def crop(image, frame):
    """
    image 是一个 Image 对象
    frame 是一个 tuple 如下 (x, y, w, h)
        用于表示一个矩形的左上角座标 x y 和 宽高 w h

    不修改原图像
    返回一个 Image 对象, 它是用 frame 把 image 裁剪出来的新图像
    """
    x, y, w1, h1 = frame[0], frame[1], frame[2], frame[3]
    # 对旧图像，取它对应区域的像素
    img = Image.new('RGBA', (w1, h1))
    for x1 in range(w1):
        for y1 in range(h1):
            # 新图像坐标
            position = (x1, y1)
            # 旧图像坐标
            old_position = (x + x1, y + y1)
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img


def flip(image):
    """
    image 是一个 Image 对象

    不修改原图像
    返回一个 Image 对象, 它是 image 上下镜像的图像
    """
    x, y = image.size
    print(x, y, 1111111111)
    img = Image.new('RGBA', (x, y))
    for i in range(x):
        for j in range(y):
            position = (i, j)
            old_position = (i, y - j - 1)
            # print(position, old_position)  左闭右开
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img


def flop(image):
    """
    image 是一个 Image 对象

    不修改原图像
    返回一个 Image 对象, 它是 image 左右镜像的图像
    """
    x, y = image.size
    img = Image.new('RGBA', (x, y))
    for i in range(x):
        for j in range(y):
            position = (i, j)
            old_position = (x - i - 1, j)
            # print(position, old_position)  左闭右开
            r, g, b, a = image.getpixel(old_position)
            img.putpixel(position, (r, g, b, a))
    return img


def main():
   

    img = Image.open('a.jpg')
    img = img.convert('RGBA')
    # i = crop(img, (0, 0, 50, 20))
    # i.save('crop.png')
    # i = flip(img)
    # i.save('flip.png')
    i = flop(img)
    i.show()
    i.save('b.png')
    pass


if __name__ == '__main__':
    main()

    # JPG不支持透明度，所以要么丢弃Alpha（透明度）, 要么保存为.png文件
    # Pillow中很多方法都需要传入一个表示矩形区域的元祖参数。

    # 这个元组参数包含四个值，分别代表矩形四条边的距离X轴或者Y轴的距离。顺序是(左，顶，右，底)。
    # 其实就相当于，矩形的左上顶点坐标为(左，顶)，矩形的右下顶点坐标为(右，底)，两个顶点就可以确定一个矩形的位置。

    # 右和底坐标稍微特殊，跟python列表索引规则一样，是左闭又开的。可以理解为[左, 右)和[顶， 底)这样左闭右开的区间。
    # 比如(3, 2, 8, 9)就表示了横坐标范围[3, 7]；纵坐标范围[2, 8]的矩形区域。
