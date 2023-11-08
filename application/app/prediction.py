import keras.utils as image
from tensorflow.keras.models import load_model
from PIL import Image 

def prediction(file_path, zone, model_name) -> float:
    model = load_model('/home/_georgiy/_georgiy@laptop360/Универ/5 семестр 2023 3 курс/Медицинский проект 3 курс/medical_project/models/' + zone + '_' + model_name) # загрузка моделей для принятия решения
    img = Image.open(file_path)
    img = img.resize((499, 499))
    img = image.load_img(file_path, target_size=(499, 499))  # загрузка изображения
   
    x = image.img_to_array(img)
    x = x.reshape(1, 499, 499, 3)
    x /= 255

    prediction = model.predict(x)  # обработка нейросетями

    return prediction[0][0]