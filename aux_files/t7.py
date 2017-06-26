import theano
import theano.tensor as T
x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = theano.function([x], s)
...
...
#Let's evaluate it ...
logistic([[0, 1], [-1, -2]])
...
#Are the results correct? - Verify!
