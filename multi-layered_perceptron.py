import numpy as np

def sigmoid(x): #aktivasyon fonskiyonu
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]]) #girişler
Y = np.array([[0],[1],[1],[0]]) #çıkışlar

#mimari
weightshiddenlayer = np.random.uniform(size=(2,2)) 
biashiddenlayer = np.random.uniform(size=(1,2))
weightsoutputlayer =  np.random.uniform(size=(2,1)) 
biasoutputlyer = np.random.uniform(size=(1,1))

for i in range(20000):
    hidden_input = np.dot(X,weightshiddenlayer) + biashiddenlayer
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weightsoutputlayer) + biasoutputlyer
    final_output = sigmoid(final_input)

    error = Y -final_output
    d_final = error + sigmoid_derivative(final_output)

    error_hidden = d_final.dot(weightsoutputlayer.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    weightsoutputlayer += hidden_output.T.dot(d_final)* 0.1
    weightshiddenlayer += X.T.dot(d_hidden) *0.1

    print("çok katmanlı sonuçlar (Başarılı):")
    print(np.round(final_output,2))