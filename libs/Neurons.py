import random

import numpy as np
import libs.Dataset

def f(x):
    return 1/(1+np.exp(-x))

def df(x):
    f(x)*(1-f(x))

W1 = np.array([[random.random() for i in range(25)] for j in range(14)])
W2 = np.array([[random.random() for i in range(14)] for j in range(10)])

def run_network(matr):
    x = np.array(matr)
    x = x.reshape(-1)
    (y, out) = go_forward(x)
    return y

def go_forward(inp):
    sum = np.dot(W1, inp)
    out = np.array([f(x) for x in sum])
    sum = np.dot(W2, out)
    y = np.array([f(x) for x in sum])
    return (y, out)

def go_forward_all(inps):
    inps.reshape(25, -1)
    sum = np.dot(W1, inps)
    out = np.array([f(x) for x in sum])
    sum = np.dot(W2, out)
    y = np.array([f(x) for x in sum])
    return (y, out)


def numberToArr(num):
    answer = []
    for i in range(num):
        answer.append(0)
    answer.append(1)
    for i in range(num+1, 10):
        answer.append(0)
    return answer

def getError(costArr, resArr):
    totalSum = 0
    for i in range(len(costArr)):
        el_list = np.array(costArr[i])
        el_list = el_list.reshape(-1)
        (y, out) = go_forward(el_list)
        res = numberToArr(resArr[i])
        error = y - np.array(res)
        error = [y*y for y in error]
        sum = 0
        for el in error:
            sum = el + sum
        totalSum = sum / len(error) + totalSum
    return totalSum

def singleTrain(matr, answer):
    global W2, W1
    lmd = 0.5
    x = np.array(matr)
    x = x.reshape(-1)
    (y, out) = go_forward(x)
    e = numberToArr(answer) - y
    d = [y[i] * (1 - y[i]) * e[i] for i in range(len(W2))]
    for i in range(len(W2)):
        # for j in range(len(W2[0])):
        #     W2[i][j] = W2[i][j] + lmd * d[i] * out[j]
        W2[i] = W2[i] + lmd * d[i] * out
    sigma = []
    for i in range(len(W1)):
        sigma.append(out[i] * (1 - out[i]))
        sum = 0
        for k in range(len(W2)):
            sum = sum + d[k] * W2[k][i]
        sigma[i] = sigma[i] * sum
        # for j in range(len(W1[0])):
        #     W1[i][j] = W1[i][j] + lmd * sigma[i] * x[j]
        W1[i] = W1[i] + lmd * sigma[i] * x



def train(trainArr, answerArr):
    global W2, W1
    lmd = 0.2
    epoch = 100
    count = len(trainArr)
    for k in range(epoch):
        for k2 in range(0, len(trainArr)):
            index = k2
            x = trainArr[index]
            x = np.array(x)
            x = x.reshape(-1)
            y, out = go_forward(x)
            e = numberToArr(answerArr[index]) - y
            d = [y[i]*(1-y[i])*e[i] for i in range(len(W2))]
            for i in range(len(W2)):
                # for j in range(len(W2[0])):
                #     W2[i][j] = W2[i][j] + lmd * d[i] * out[j]
                W2[i] = W2[i] + lmd * d[i] * out
            sigma = []
            for i in range(len(W1)):
                sigma.append(out[i]*(1-out[i]))
                sum = 0
                for k in range(len(W2)):
                    sum = sum + d[k]*W2[k][i]
                sigma[i] = sigma[i] * sum
                # for j in range(len(W1[0])):
                #     W1[i][j] = W1[i][j] + lmd*sigma[i]*x[j]
                W1[i] = W1[i] + lmd * sigma[i] * x