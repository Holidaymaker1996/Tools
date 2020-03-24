from PIL import Image

# pip3 install pillow
# 这是 python 用于处理图像文件的库


"""
计算机存储图像的原理

w 是图像宽
h 是图像高
一个图像由 w * h 个像素点组成
每个像素点由 rgba 4 个部分组成
r 红色
g 绿色
b 蓝色
a 透明度

现在的图像 rgba 分别是一个字节表示，一个字节的数值范围是 0 - 255
也就是一个像素点 4 字节，可以表示的颜色范围是 256 的 4 次方

但是很多图像是没有 a 的，所以就只有 3 字节表示一个像素


实现 grayscale 函数，让生成的 sample.png 是黑白的
"""




def grayscale(image):
    w, h = image.size
    for x in range(w):
        for y in range(h):
            position = (x, y)
            r, g, b, a = image.getpixel(position)
            gray = (r + g + b) // 3
            image.putpixel(position, (gray, gray, gray, a))



def main():
    # 打开图像文件
    img = Image.open("sample.png")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    grayscale(img)
    # 保存图像文件
    img.save('sample2.png')


if __name__ == '__main__':
    main()
