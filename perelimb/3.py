import tensorflow as tf
from keras.applications import InceptionResNetV2
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam

# Задайте размер изображений

train_path = "train"  # путь для обучающей выборки
test_path = "test"
# Создайте генераторы данных для обучения и проверки
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1.0/255)

img_width, img_height = 499, 499
batch_size = 8
train_generator = train_datagen.flow_from_directory(
train_path,
target_size=(img_width, img_height),
batch_size=batch_size,
class_mode="binary"
)

test_generator = test_datagen.flow_from_directory(
test_path,
target_size=(img_width, img_height),
batch_size=batch_size,
class_mode="binary"
)

# Загрузите предобученную модель InceptionResNetV2
InceptionResNetV2 = InceptionResNetV2(weights=None, include_top=False, input_shape=(img_width, img_height, 3))
callback = ModelCheckpoint(filepath="InceptionResNetV2_perelimb_model3.h5", monitor="val_accuracy", save_best_only=True)
# Добавьте свои слои поверх InceptionResNetV2
x = InceptionResNetV2.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation="relu")(x)
x = tf.keras.layers.Dropout(0.5)(x)  # добавим dropout для предотвращения переобучения
x = Dense(256, activation="relu")(x)
x = tf.keras.layers.Dropout(0.5)(x)  # добавим dropout для предотвращения переобучения
output = Dense(1, activation="sigmoid")(x)


# Создайте модель на базе InceptionResNetV2
model = Model(inputs=InceptionResNetV2.input, outputs=output)
model.load_weights("InceptionResNetV2_model1.h5")

model.compile(optimizer=Adam(1e-4), loss="binary_crossentropy", metrics=["accuracy"])

model.fit(train_generator, epochs=15, steps_per_epoch=len(train_generator), validation_data=test_generator, validation_steps=len(test_generator),callbacks=[callback])

accuracy = model.evaluate(test_generator)

print("Результат fine tune'd = ", accuracy[1])
