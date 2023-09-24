from os import listdir, remove, rename

from PIL import Image
from glob import glob

def compress_img(dir, dir2,  quality=100, width=499, height=499):
    for file in dir:
        name = file;
        in_dir = listdir('norma'+'/'+file);
        for file in in_dir:
            img = Image.open('norma'+'/'+name+"/"+file)
            img = img.resize((width, height), Image.ANTIALIAS)
            try:
                img.save(dir2 + '/' + file, quality=quality, optimize=True)
            except OSError:
                img = img.convert("RGB")
                img.save(dir2 + '/' + file, quality=quality, optimize=True)

def delete(dir):
    for file in dir:
        remove(file)

def convert_images(dir, name):
    dir1 = listdir(dir)
    i = 0
    for file in dir1:
        img = Image.open(dir + '/' + file)
        rgb_img = img.convert('RGB')
        new_name = name + str(i) + '.bmp'
        i += 1
        rename(dir + '/' + file, dir + '/' + new_name)
nenorma=listdir('norma')
compress_img(nenorma, 'test/zdorov')
convert_images('test/zdorov', 'zdorov.')






