#Author : Mohit Chhabra

import os
import timeit
import numpy as np
import theano
import theano.tensor as T
from theano import function
from theano.tensor.shared_randomstreams import RandomStreams
from theano.printing import pp
start_time = timeit.default_timer()


x_value = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]],dtype='float32')

y_value = np.array([[1],
			[0],
			[0],
			[1]])
learning_rate=T.fscalar('learning_rate')
y_desired=T.fvector('y_desired')
y_desired=theano.shared(value=y_value,name='y_desired',borrow=True)
index=T.lscalar('index')
rng=np.random.RandomState(1234)
W_l12_values=np.asarray(rng.uniform(-1,1,(3,4)),dtype='float32')
W_l23_values=np.asarray(rng.uniform(0,1,(4,1)),dtype='float32')
b_l2_values=np.asarray(rng.uniform(0,1,(1,4)),dtype='float32')
b_l3_values=np.asarray(rng.uniform(0,1,(1,1)),dtype='float32')
W_l12=theano.shared(value=W_l12_values,name='W_l12',borrow=True)
W_l23=theano.shared(value=W_l23_values,name='W_l23',borrow=True)
b_l2=theano.shared(value=b_l2_values,name='b_l2',borrow=True)
b_l3=theano.shared(value=b_l3_values,name='b_l3',borrow=True)
params=[W_l12,W_l23,b_l2,b_l3]
x=T.fvector('x')
y=T.nnet.sigmoid(T.dot(T.nnet.sigmoid(T.dot(x,W_l12)+b_l2),W_l23)+b_l3)
cost=T.sqr(y-y_desired[index]).sum()	
# for i in xrange(10):
# 	for t in x_value:
# 		gparams=[T.grad(cost,gf) for gf in params]
# 		updates=[(params,params-learning_rate*gparams) for gf,gp in zip(params,gparams)]
# 		f=function([x],y,givens={W_l12:W_l12_values,W_l23:W_l23_values,b_l2:b_l2_values,b_l3:b_l3_values})	
# 		f(t)
# print f([1,0,0])
gparams=[T.grad(cost,param) for param in params]
updates=[(param,param-learning_rate*gparam) for param,gparam in zip(params,gparams)]
train=function([x,learning_rate,index],cost,givens={W_l12:W_l12,W_l23:W_l23,b_l2:b_l2,b_l3:b_l3},updates=updates,allow_input_downcast=True)
for i in xrange(60000):
	for j in xrange(x_value.shape[0]):
		train(x_value[j],0.1,j)


end_time = timeit.default_timer()
test=function([x],y,givens={W_l12:W_l12,W_l23:W_l23,b_l2:b_l2,b_l3:b_l3})
print test([0,0,1])
print '\n'
print test([0,1,1])
print '\n'
print test([1,0,1])
print '\n'
print test([1,1,1])
print "Execution time is",end_time-start_time



















# W_l1=2*srng.uniform((3,4))-1
# W_l2=2*srng.uniform((4,1))-1

# Z_l1=T.dot(X,W_l1)
# Y_l1=T.nnet.sigmoid(Z_l1)
# Z_l2=T.dot(Y_l1,W_l2)
# Y_l2=T.nnet.sigmoid(Z_l2)

# forward_pass=function([],Y_l2)
# #print forward_pass()	

# e_l2=y-Y_l2
# c=0.5 * T.sqr(e_l2)

# #l2_delta = theano.gradient.jacobian(c,Z_l2).sum(axis=1)

# #error=function([],l2_delta)
# #print error()


# # a = T.fscalar('a')
# # b = T.nnet.sigmoid(a)
# # check=function([a],b)
# # gy = T.grad(b,a)
# # mcheck=function([a],gy)
# # print check(0)
# # print mcheck(0)










end_time = timeit.default_timer()
print "Execution time is ", (end_time-start_time)
