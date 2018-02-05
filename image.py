from PIL import Image
import android_test


def getImage():
    # android_test.android_get_screnncap('test')
    # android_test.android_pull_screnncap_to_current_path('test')
    image = Image.open('./test.png')

    #获取图片的属性
    #SIZE
    w, h = image.size
    print('{} x {}'.format(w, h))
    # L RGB CMYK
    mode = image.mode
    print(mode)

    # 打开图片
    # image.show()

    # bands = image.getbands()
    # print(bands)

    # bboxs = image.getbbox()
    # print(bboxs)

    # data = list(image.getdata())
    # print(data)

    # pixel = image.getpixel((500,500))
    # print(pixel)


    #剪切图片
    # region = (100,100,300,300)
    # cropimg = image.crop(region)
    # cropimg.save('crop.png')
    # cropimg.show()

    #缩放图片
    # im_resize = image.resize((128,128))
    # im_resize.save('resize.png')

    #旋转图片
    # im_rotate = image.rotate(45)
    # im_rotate.show()

    #图像翻转
    # im_transpose = image.transpose(Image.FLIP_LEFT_RIGHT)
    # im_transpose = image.transpose(Image.FLIP_TOP_BOTTOM)
    # im_transpose = image.transpose(Image.ROTATE_90)
    # im_transpose = image.transpose(Image.ROTATE_180)
    # im_transpose = image.transpose(Image.ROTATE_270)
    # im_transpose.show()


def main():
    getImage()


if __name__ == '__main__':
    main()
