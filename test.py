import numpy as np 

w = np.zeros((15,15))
b = np.zeros((1,1))
'''
b = 16
for i in range(15):
	for j in range(15):
		w[i][j] = j

np.save('model.npy',w)
np.save('bias.npy',b)
'''
w = np.load('model.npy')
b = np.load('bias.npy')
for i in range(15):
	for j in range(15):
		print(w[i][j]) 

print("bias: ", b)