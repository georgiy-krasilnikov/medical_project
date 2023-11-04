from os import listdir

import matplotlib.pyplot as plt
import keras.utils as image
from keras.models import load_model


def result(
    dir, true, pred1, pred2, model
):  # функция, выводящая результат распознавания каждого изображения в каждой папке контрольной выборки
    count_bolen = 0
    count_zdorov = 0
    img_dir = listdir(dir)
    for file in img_dir:  # перебор файлов в папке
        img = image.load_img(
            dir + "/" + file, target_size=(499, 499)
        )  # загрузка изображения
        x = image.img_to_array(img)
        x = x.reshape(1, 499, 499, 3)
        x /= 255
        prediction = model.predict(x)  # обработка нейросетью

        if prediction[0][0] < (
            0.5
        ):  # вывод результата в зависимости от успешности распознавания
            if true == "zdorov":
                count_zdorov += 1
                # счётчик ошибок "здоровых" (якобы больных)
                show(pred1, prediction[0][0], img)  # болен
        else:
            if true == "bolen":
                count_bolen += 1  # счётчик ошибок "больных" (якобы здоровых)
                show(pred2, prediction[0][0], img)  # здоров

    print("Якобы здоровых: ", count_bolen)
    print("Якобы больных: ", count_zdorov)


def show(title, pred, img):  # функция показа результата распознавания
    plt.imshow(img.convert("RGBA"))
    plt.title(title + str(pred))
    plt.show()


model = load_model("limb_InceptionV3.h5")

result("limb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("limb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

model = load_model("perelimb_InceptionV3.h5")

result("perelimb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("perelimb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

model = load_model("limb_Xception.h5")

result("limb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("limb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

model = load_model("perelimb_Xception.h5")

result("perelimb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("perelimb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

model = load_model("limb_InceptionResNetV2.h5")

result("limb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("limb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

model = load_model("perelimb_InceptionResNetV2.h5")

result("perelimb/test/bolen", "bolen", "Патология -> ", "Якобы условная норма -> ", model)
result("perelimb/test/zdorov", "zdorov", "Якобы патология -> ", "Условная норма -> ", model)

