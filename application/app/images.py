from os import mkdir
from io import BytesIO

from PIL import Image as image

from db import db
from models import Image

def read_bin(path):
    with open(path, "rb") as img:
        f = img.read()
        b = bytes(f)
        return b

def load_images(path, zone, sample, info):
    img = read_bin(path)

    match (zone == 'limb', sample == 'train'):
        case (True, True):
            db.input_train_images_to_limb(img=img, info=info)
        case (True, False):
            db.input_test_images_to_limb(img=img, info=info)
        case (False, True):
            db.input_train_images_to_perelimb(img=img, info=info)
        case (False, False):
            db.input_test_images_to_perelimb(img=img, info=info)

def download_images(limb=bool, perelimb=bool):
    if limb == True and perelimb == True:
        mkdir('limb_zone')
        mkdir('perelimb_zone')
        mkdir('limb_zone/train')
        mkdir('limb_zone/test')
        mkdir('limb_zone/train/bolen')
        mkdir('limb_zone/train/zdorov')
        mkdir('limb_zone/test/bolen')
        mkdir('limb_zone/test/zdorov')

        mkdir('perelimb_zone/train')
        mkdir('perelimb_zone/test')
        mkdir('perelimb_zone/train/bolen')
        mkdir('perelimb_zone/train/zdorov')
        mkdir('perelimb_zone/test/bolen')
        mkdir('perelimb_zone/test/zdorov')

        train_bolen_imgs = db.get_train_images_from_limb('bolen')
        train_zdorov_imgs = db.get_train_images_from_limb('zdorov')
        test_bolen_imgs = db.get_test_images_from_limb('bolen')
        test_zdorov_imgs = db.get_test_images_from_limb('zdorov')

        save_images('limb_zone/test/bolen', 'bolen', test_bolen_imgs)
        save_images('limb_zone/test/zdorov', 'zdorov', test_zdorov_imgs)
        save_images('limb_zone/train/bolen', 'bolen', train_bolen_imgs)
        save_images('limb_zone/train/zdorov', 'zdorov', train_zdorov_imgs)

        train_bolen_imgs = db.get_train_images_from_perelimb('bolen')
        train_zdorov_imgs = db.get_train_images_from_perelimb('zdorov')
        test_bolen_imgs = db.get_test_images_from_perelimb('bolen')
        test_zdorov_imgs = db.get_test_images_from_perelimb('zdorov')

        save_images('perelimb_zone/test/bolen', 'bolen', test_bolen_imgs)
        save_images('perelimb_zone/test/zdorov', 'zdorov', test_zdorov_imgs)
        save_images('perelimb_zone/train/bolen', 'bolen', train_bolen_imgs)
        save_images('perelimb_zone/train/zdorov', 'zdorov', train_zdorov_imgs)

    elif limb == True and perelimb == False:
        mkdir('limb_zone')
        mkdir('limb_zone/train')
        mkdir('limb_zone/test')
        mkdir('limb_zone/train/bolen')
        mkdir('limb_zone/train/zdorov')
        mkdir('limb_zone/test/bolen')
        mkdir('limb_zone/test/zdorov')

        train_bolen_imgs = db.get_train_images_from_limb('bolen')
        train_zdorov_imgs = db.get_train_images_from_limb('zdorov')
        test_bolen_imgs = db.get_test_images_from_limb('bolen')
        test_zdorov_imgs = db.get_test_images_from_limb('zdorov')

        save_images('limb_zone/test/bolen', 'bolen', test_bolen_imgs)
        save_images('limb_zone/test/zdorov', 'zdorov', test_zdorov_imgs)
        save_images('limb_zone/train/bolen', 'bolen', train_bolen_imgs)
        save_images('limb_zone/train/zdorov', 'zdorov', train_zdorov_imgs)

    elif limb == False and perelimb == True:
        mkdir('perelimb_zone/train')
        mkdir('perelimb_zone/test')
        mkdir('perelimb_zone/train/bolen')
        mkdir('perelimb_zone/train/zdorov')
        mkdir('perelimb_zone/test/bolen')
        mkdir('perelimb_zone/test/zdorov')

        train_bolen_imgs = db.get_train_images_from_perelimb('bolen')
        train_zdorov_imgs = db.get_train_images_from_perelimb('zdorov')
        test_bolen_imgs = db.get_test_images_from_perelimb('bolen')
        test_zdorov_imgs = db.get_test_images_from_perelimb('zdorov')

        save_images('perelimb_zone/test/bolen', 'bolen', test_bolen_imgs)
        save_images('perelimb_zone/test/zdorov', 'zdorov', test_zdorov_imgs)
        save_images('perelimb_zone/train/bolen', 'bolen', train_bolen_imgs)
        save_images('perelimb_zone/train/zdorov', 'zdorov', train_zdorov_imgs)

def save_images(dir=str, type=str, imgs=[memoryview]):
    c = 0
    for i in imgs:
            img = image.open(BytesIO(i))
            img.save(dir+'/'+type+'.'+str(c)+'.bmp')
            c +=1
