import numpy
import theano.tensor as T
from theano import function
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y #build an expression
f = function([x, y], z)
...
...
#use as input: 

f([[1, 2], [3, 4]], [[10, 20], [30, 40]])
