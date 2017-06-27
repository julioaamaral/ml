from theano import In
from theano import function
x, y = T.dscalars('x', 'y')
z = x + y
f = function([x, In(y, value=1)], z)
...
#try with these inputs 
f(33)
...
f(33,2)

