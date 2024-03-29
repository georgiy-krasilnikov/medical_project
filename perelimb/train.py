from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Dropout
from keras.applications import InceptionV3
from keras.callbacks import ModelCheckpoint

train_path = "train"  # путь для обучающей выборки
test_path = "test"  # путь для контрольной выбокри

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

batch_size = 15  # размерность подвыборки
img_width, img_height = (
    499,
    499,
)  # размерность тензора на основе изображения для входных данных в нейронную сеть

train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode="binary",
)  # генератор для обучения
test_generator = test_datagen.flow_from_directory(
    test_path,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode="binary",
)  # генератор для тестирования на контрольной выборке

inception = InceptionV3(
    include_top=False, input_shape=(img_width, img_height, 3)
)  # импорт модели InceptionV3

for layer in inception.layers:
    layer.trainable = False  # игнорируем слой для классификации изображений на ILSVRC

model = (
    Sequential()
)  # немного модифицируем нашу модель, добавляя несколько дополнительных слоёв
model.add(inception)
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

steps_per_epoch = (
    train_generator.n // train_generator.batch_size
)  # устанавливаем размеры шагом
validation_steps = test_generator.n // test_generator.batch_size
callback = ModelCheckpoint(
    filepath="perelimb_InceptionV3.h5", monitor="val_accuracy", save_best_only=True
)

model.fit(
    train_generator,
    epochs=15,
    steps_per_epoch=steps_per_epoch,
    validation_data=test_generator,
    validation_steps=validation_steps,
    callbacks=callback,
)
