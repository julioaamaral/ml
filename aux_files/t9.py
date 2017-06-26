from theano import shared
state = shared(0)
inc = T.iscalar('inc')
accumulator = function([inc], state, updates=[(state, state+inc)])
...
#give an real use to this function 
...
#Let's try it out! 
print(state.get_value())
accumulator(1)
print(state.get_value())
accumulator(300)
print(state.get_value())
