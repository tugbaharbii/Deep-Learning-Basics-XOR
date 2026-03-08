import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([[0],[1],[1],[0]])

weights = np.random.uniform(size=(2, 1)) #tek katman
lr = 0.1 

for epoch in range(10000):
    output = np.dot(X,weights)
    error = Y - output
    weights += np.dot(X.T , error) * lr

print("Tek katman sonuçları  (Beklenen: 0, 1, 1, 0):")
print(output)

