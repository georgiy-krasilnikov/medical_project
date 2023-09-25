from os import listdir, remove, rename

from PIL import Image
from glob import glob


def compress_img(dir1, dir2, quality=100, width=499, height=499):
    for file in dir1:
        name = file
        in_dir = listdir(dir1 + "/" + name)
        for file in in_dir:
            img = Image.open("dir1" + "/" + name + "/" + file)
            img = img.resize((width, height), Image.ANTIALIAS)
            try:
                img.save(dir2 + "/" + file, quality=quality, optimize=True)
            except OSError:
                img = img.convert("RGB")
                img.save(dir2 + "/" + file, quality=quality, optimize=True)


def convert_images(dir, name):
    dir1 = listdir(dir)
    i = 0
    for file in dir1:
        img = Image.open(dir + "/" + file)
        rgb_img = img.convert("RGB")
        new_name = name + str(i) + ".bmp"
        i += 1
        rename(dir + "/" + file, dir + "/" + new_name)


limb_train_zdorov_dir = listdir("limb/train/zdorov")
limb_train_bolen_dir = listdir("limb/train/bolen")
limb_test_zdorov_dir = listdir("limb/test/zdorov")
limb_test_bolen_dir = listdir("limb/test/bolen")

perelimb_train_zdorov_dir = listdir("perelimb/train/zdorov")
pereperelimb_train_bolen_dir = listdir("perelimb/train/bolen")
perelimb_test_zdorov_dir = listdir("perelimb/test/zdorov")
perelimb_test_bolen_dir = listdir("perelimb/test/bolen")

limb_train_dir = glob("limb/train/**/*.bmp", recursive=True)
limb_test_dir = glob("limb/test/**/*.bmp", recursive=True)
perelimb_train_dir = glob("perelimb/train/**/*.bmp", recursive=True)
perelimb_test_dir = glob("perelimb/test/**/*.bmp", recursive=True)

compress_img("limb_norma_train", limb_train_zdorov_dir)
compress_img("limb_nenorma_train", limb_train_bolen_dir)
compress_img("limb_norma_test", limb_zdorov_dir)
compress_img("limb_nenorma_test", limb_limb_test_bolen_dir)

compress_img("perelimb_norma_train", perelimb_train_zdorov_dir)
compress_img("perelimb_nenorma_train", perelimb_train_bolen_dir)
compress_img("perelimb_norma_test", perelimb_zdorov_dir)
compress_img("perelimb_nenorma_test", perelimb_limb_test_bolen_dir)

convert_images(limb_train_zdorov_dir, "zdorov.")
convert_images(limb_train_bolen_dir, "bolen.")
convert_images(limb_test_zdorov_dir, "zdorov.")
convert_images(limb_test_bolen_dir, "bolen.")

convert_images(perelimb_train_zdorov_dir, "zdorov.")
convert_images(perelimb_train_bolen_dir, "bolen.")
convert_images(perelimb_test_zdorov_dir, "zdorov.")
convert_images(perelimb_test_bolen_dir, "bolen.")
