         # CONV => RELU => POOL
         model.add(Conv2D(50, kernel_size=5, border_mode="same"))
         model.add(Activation("relu"))
         model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
         # Flatten => RELU layers
         model.add(Flatten())
         model.add(Dense(500))
         model.add(Activation("relu"))
...
