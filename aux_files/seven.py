...
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy']))
targets = keras.utils.to_categorical(labels, num_classes=10)
model.fit(data, targets, epochs=10, batch_size=32)
...
