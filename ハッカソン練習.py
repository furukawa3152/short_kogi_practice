import numpy as np
from keras.layers import Activation, Dense
from keras.models import Sequential

model = Sequential()
model.add(Dense(3, input_dim=2))
model.add(Activation("sigmoid"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

# model.summary()

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["accuracy"])

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
model.fit(x, y, epochs=10)

result = model.predict(x)
print(result)