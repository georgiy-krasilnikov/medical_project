from os import listdir, remove, rename

from PIL import Image
from glob import glob

def compress_img(dir, quality=100, width=399, height=399):
    for file in dir:
        img = Image.open(dir + '/' + file)
        img = img.resize((width, height), Image.ANTIALIAS)
        try:
            img.save(dir + '/' + file, quality=quality, optimize=True)
        except OSError:
            img = img.convert("RGB")
            img.save(dir + '/' + file, quality=quality, optimize=True)

def delete(dir):
    for file in dir:
        remove(file)

def convert_images(dir, name):
    i = 0
    for file in dir:
        img = Image.open(dir + '/' + file)
        rgb_img = img.convert('RGB')
        rgb_img.save(dir + '/' + file.replace("bmp", "jpg"), quality=100)
        new_name = name + str(i) + '.bmp'
        i += 1
        rename(dir + '/' + img, dir + '/' + new_name)

train_zdorov_dir = listdir('train/zdorov')
train_bolen_dir = listdir('train/bolen')
test_zdorov_dir = listdir('test/zdorov')
test_bolen_dir = listdir('test/bolen')
train_dir = glob('train/**/*.bmp', recursive=True)
test_dir = glob('test/**/*.bmp', recursive=True)

compress_img(train_zdorov_dir)
compress_img(train_bolen_dir)
compress_img(test_zdorov_dir)
compress_img(test_bolen_dir)

convert_images(train_zdorov_dir, 'zdorov.')
convert_images(train_bolen_dir, 'bolen.')
convert_images(test_zdorov_dir, 'zdorov.')
convert_images(test_bolen_dir, 'bolen.')

delete(train_dir)
delete(test_dir)




