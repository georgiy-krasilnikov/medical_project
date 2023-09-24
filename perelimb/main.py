from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Flatten, Dropout
from keras.applications import InceptionV3
import matplotlib.pyplot as plt
import keras.utils as image
from os import listdir

def result(dir, true, pred1, pred2, model): #функция, выводящая результат распознавания каждого изображения в каждой папке контрольной выборки
    count_bolen = 0 
    count_zdorov = 0
    img_dir = listdir(dir) 
    for file in img_dir: #перебор файлов в папке
        img = image.load_img(dir + '/' + file, target_size=(499, 499)) #загрузка изображения
        x = image.img_to_array(img)
        x = x.reshape(1, 499, 499, 3)
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

def show(title, pred, img): # функция показа результата распознавания
    plt.imshow(img.convert('RGBA'))
    plt.title(title + str(pred))
    plt.show()

train_path = 'train' # путь для обучающей выборки
test_path = 'test' # путь для контрольной выбокри

train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

batch_size = 10 # размерность подвыборки
img_width, img_height = 499, 499 # размерность тензора на основе изображения для входных данных в нейронную сеть

train_generator = train_datagen.flow_from_directory(train_path, target_size=(img_width, img_height), batch_size=batch_size, class_mode='binary') # генератор для обучения
test_generator = test_datagen.flow_from_directory(test_path, target_size=(img_width, img_height), batch_size=batch_size, class_mode='binary') # генератор для тестирования на контрольной выборке

# inception = InceptionV3(include_top=False, input_shape=(img_width, img_height, 3)) # импорт модели InceptionV3

# for layer in inception.layers:
#     layer.trainable = False # игнорируем слой для классификации изображений на ILSVRC

# model = Sequential() # немного модифицируем нашу модель, добавляя несколько дополнительных слоёв
# model.add(inception)
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(1, activation='sigmoid'))

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model = load_model('perelimb_model.h5')
steps_per_epoch = train_generator.n // train_generator.batch_size # устанавливаем размеры шагом
validation_steps = test_generator.n // test_generator.batch_size


model.fit(train_generator, epochs=15, steps_per_epoch=steps_per_epoch, validation_data=test_generator, validation_steps=validation_steps)

accuracy = model.evaluate(test_generator)
print("Результат обучения = ", accuracy[1])

#result('test/bolen', 'bolen', 'Патология -> ', 'Якобы условная норма -> ', model)
#result('test/zdorov', 'zdorov', 'Якобы патология -> ', 'Условная норма -> ', model)
model.save('perelimb_model.h5')
