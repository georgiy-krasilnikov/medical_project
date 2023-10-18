from keras.applications import Xception
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint

# Задайте размер изображений

train_path = "train"  # путь для обучающей выборки
test_path = "test"
# Создайте генераторы данных для обучения и проверки
train_datagen = ImageDataGenerator(
rescale=1.0/255,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1.0/255)

img_width, img_height = 499, 499
batch_size = 35
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

# Загрузите предобученную модель Xception
xception = Xception(weights="imagenet", include_top=False, input_shape=(img_width, img_height, 3))
callback = ModelCheckpoint(filepath="limb_xception.h5", monitor="val_accuracy", save_best_only=True)
# Добавьте свои слои поверх Xception
x = xception.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation="relu")(x)
x = Dense(128, activation="relu")(x)
output = Dense(1, activation="softmax")(x)

# Создайте модель на базе Xception
model = Model(inputs=xception.input, outputs=output)

# Заморозьте веса предобученных слоев
for layer in xception.layers:
 layer.trainable = False

# Скомпилируйте и обучите модель
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(train_generator, epochs=15, steps_per_epoch=len(train_generator), validation_data=test_generator, validation_steps=len(test_generator),callbacks=[callback])

accuracy = model.evaluate(test_generator)

print("Результат = ", accuracy[1])
