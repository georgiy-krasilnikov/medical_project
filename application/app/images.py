from db import db
from models import Image

def read_bin(path):
    with open(path, "rb") as img:
        f = img.read()
        b = bytes(f).hex()
        return b

def load_images(path, zone, sample, info):
    img = Image(read_bin(path), info)

    match (zone == 'limb', sample == 'train'):
        case (True, True):
            db.input_train_images_to_limb(img=img)
        case (True, False):
            db.input_test_images_to_limb(img=img)
        case (False, True):
            db.input_train_images_to_perelimb(img=img)
        case (False, False):
            db.input_test_images_to_perelimb(img=img)

    