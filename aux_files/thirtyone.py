...
#define the ConvNet
class LeNet:
    @staticmethod
    def build(input_shape, classes):
         model = Sequential()
         # CONV => RELU => POOL
         model.add(Convolution2D(20, kernel_size=5, padding="same",
         input_shape=input_shape))
         model.add(Activation("relu"))
         model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
...
