import numpy
import theano.tensor as T
from theano import function
...
#The first steps is to instantiate two symbols (variables)
#representing the quantities that you want to add. 
...
x = T.dmatrix('x')
y = T.dmatrix('y')
...
z = x + y #build an expression

f = function([x, y], z)
