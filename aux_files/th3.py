a, b = T.dmatrices('a', 'b')
diff = a - b
abs_diff = abs(diff)
diff_squared = diff**2
f = theano.function([a, b], [diff, abs_diff, diff_squared])

#Use these inputs.. 
#a =  [[-1,0],[10,14]] 
#b =  [[1,2],[4,6]]
f([[-1, 0], [10, 14]], [[1, 2], [4, 6]])
