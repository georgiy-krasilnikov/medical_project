from os import listdir

import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout, Flatten, Dense
from keras.applications import VGG16
from keras.models import Sequential
from keras.optimizers import Adam
import keras.utils as image

def result(dir, true, pred1, pred2, model): #функция, выводящая результат распознавания каждого изображения в каждой папке контрольной выборки
    count_bolen = 0 
    count_zdorov = 0
    img_dir = listdir(dir) 
    for file in img_dir: #перебор файлов в папке
        img = image.load_img(dir + '/' + file, target_size=(399, 399)) #загрузка изображения
        x = image.img_to_array(img)
        x = x.reshape(1, 399, 399, 3)
        x /= 255
        prediction = model.predict(x) #обработка нейросетью

        if (prediction[0][0] < (0.5)): #вывод результата в зависимости от успешности распознавания
            if (true == 'zdorov'):
                count_zdorov += 1; #счётчик ошибок "здоровых" (якобы больных)
                show(pred1, prediction[0][0], img) #болен
        else:
            if (true == 'bolen'):
                count_bolen += 1 #счётчик ошибок "больных" (якобы здоровых)
                show(pred2, prediction[0][0], img) #здоров
            else:
                show(pred2, prediction[0][0], img) #здоров
    print('Якобы здоровых: ', count_bolen)
    print('Якобы больных: ', count_zdorov)

def show(title, pred, img): #функция показа результата распознавания с помощью библиотеки matplotlib
    plt.imshow(img.convert('RGBA'))
    plt.title(title + str(pred))
    plt.show()

train_dir = 'train' #установка путей к обучающей и контрольной выборкам
test_dir = 'test'
img_width, img_height = 399, 399 #размеры для изображений
input_shape = (img_width, img_height, 3)
batch_size = 45 #размер мини-выборки

vgg16_net = VGG16(weights='imagenet', include_top=False, input_shape=(399, 399, 3)) #импорт модели VGG16 (загружаем веса "ImageNet")

vgg16_net.trainable = False 

vgg16_net.summary()

model = Sequential() #немного кастомизируем модель VGG16, добавляя некоторые слои
model.add(vgg16_net)
model.add(Flatten())
model.add(Dense(256, activation='relu')) #полносвязаный слой
model.add(Dropout(0.5)) #Dropout для предотавращения переобучения
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile( #компилируем нашу модель
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=1e-5), 
    metrics=['accuracy'])

datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory( #генератор для обучающей выборки
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

test_generator = datagen.flow_from_directory( #генератор для контрольной выборки
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

model.fit( #обучение модели
    train_generator,
    steps_per_epoch=train_generator.n // batch_size,
    epochs=25,
    validation_data=test_generator,
    validation_steps=test_generator.n // batch_size)

accuracy = model.evaluate(test_generator) #распознавание контрольной выборки
print("Результат: ", accuracy[1]) 

result('test/bolen', 'bolen', 'Патология -> ', 'Якобы условная норма -> ', model)
result('test/zdorov', 'zdorov', 'Якобы патология -> ', 'Условная норма -> ', model)
