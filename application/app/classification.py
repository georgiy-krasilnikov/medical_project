import matplotlib.pyplot as plt
import keras.utils as image
from tensorflow.keras.models import load_model
from PIL import Image 

from prediction import prediction

def result(file_path, zone):  # функция, выводящая результат распознавания каждого изображения в каждой папке контрольной выборки
    prediction1 = prediction(file_path, zone, 'InceptionV3.h5')
    prediction2 = prediction(file_path, zone, 'Xception.h5')
    prediction3 = prediction(file_path, zone, 'InceptionResNetV2.h5')

    res = make_decision(pred1=prediction1, pred2=prediction2, pred3=prediction3)
    print(res)
    


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
        return 'Паталогия'
    
    return 'Относительная норма'



    