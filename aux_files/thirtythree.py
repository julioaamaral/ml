...
         # a softmax classifier
         model.add(Dense(classes))
         model.add(Activation("softmax"))
    return model
