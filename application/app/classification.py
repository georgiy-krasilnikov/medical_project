import matplotlib.pyplot as plt
from PIL import Image 
import keras.utils as image

from models import limb_InceptionV3, limb_Xception, limb_InceptionResNetV2

def result(file_path, zone) -> str:  # функция, выводящая результат распознавания каждого изображения в каждой папке контрольной выборки
    if zone == 'limb':
        prediction1 = prediction(file_path, limb_InceptionV3)
        prediction2 = prediction(file_path, limb_Xception)
        prediction3 = prediction(file_path, limb_InceptionResNetV2)

    res = make_decision(pred1=prediction1, pred2=prediction2, pred3=prediction3)
    img = Image.open(file_path)
    show(res, img)
    return res

def show(title, img):  # функция показа результата распознавания
    plt.imshow(img.convert("RGBA"))
    plt.title(title)
    plt.show()

def make_decision(pred1=float, pred2=float, pred3=float) -> str:
    bolen_count = 0
    zdorov_count = 0

    if pred1 > 0.5:
        zdorov_count += 1
    else:
        bolen_count += 1

    if pred2 > 0.5:
        zdorov_count += 1
    else:
        bolen_count += 1

    if pred3 > 0.5:
        zdorov_count += 1
    else:
        bolen_count += 1
    
    if bolen_count > zdorov_count:
        return 'Патoлогия'
    
    return 'Относительная норма'


def prediction(file_path, model) -> float:
    img = Image.open(file_path)
    img = img.resize((499, 499))
    img = image.load_img(file_path, target_size=(499, 499))  # загрузка изображения
   
    x = image.img_to_array(img)
    x = x.reshape(1, 499, 499, 3)
    x /= 255

    prediction = model.predict(x)  # обработка нейросетями

    return prediction[0][0]


    
