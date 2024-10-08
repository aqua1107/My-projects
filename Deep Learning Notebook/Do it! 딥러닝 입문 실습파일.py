#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:47:54 2024

@author: aidall
"""

#sklearn에 있는 당뇨병 데이터 불러오기
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

#당뇨병 데이터의 모양과 목표 데이터의 모양 (회귀: 지도학습)
print(diabetes.data.shape, diabetes.target.shape)

#처음부터 3열까지의 데이터를 표시
diabetes.data[0:3]

#목표 데이터 3열까지 표시
diabetes.target[:3]

#산점도로 데이터 시각화
import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,2], diabetes.target)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#산점도에 있는 데이터를 변수에다 저장하기
x = diabetes.data[:,2]
y = diabetes.target

#경사하강법 실시 (초기값)
w = 1.0
b = 1.0

#선형회귀와 비슷한 원리(예측값 약 1.06)
y_hat = x[0]*w+b
print(y_hat)

#하지만 목표물까지 거리가 멀다
print(y[0])

#기울기를 조금 더 가파르게 해보자(아까보다는 예측값이 조금 더 근접했다.)
w_inc = w + 0.1
y_hat_inc = x[0]*w_inc + b
print(y_hat_inc)

#기울기에 따른 예측값의 변화율
w_rate = (y_hat_inc - y_hat)/(w_inc - w)
print(w_rate)

#기존 방법으로 계속 고수하면 효율성이 극소화되고 입력변수가 많아져 한번에 학습시켜보자
for x_i, y_i in zip(x, y):
    y_hat = x_i * w + b
    err = y_i - y_hat
    w_rate = x_i
    w = w + w_rate * err
    b = b + 1 * err
print(w, b)

#산점도로 그려보니 회귀직선이 아까보단 확실히 나아졌다. 그러나 아직 뭔가 부족하다. 
plt.scatter(x, y)
pt1 = (-0.1, -0.1 * w + b)
pt2 = (0.15, 0.15 * w + b)
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#for 반복문을 사용하여 회귀직선을 더 근사시켜보자.
for i in range(1,101):
    for x_i, y_i in zip(x, y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i
        w = w + w_rate * err
        b = b + 1 * err
print(w, b)

#for문으로 학습시키니 산점도 플롯에서 더 근사됐다는 것을 알 수 있다.
plt.scatter(x, y)
pt1 = (-0.1, -0.1 * w + b)
pt2 = (0.15, 0.15 * w + b)
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#딥러닝 실습인 만큼 class함수를 이용하여 선형회귀의 신경망의 작동원리를 알아보자.
class Neuron:
    def __init__(self):
        self.w = 1.0
        self.b = 1.0
    def forpass(self, x):
        y_hat = x * self.w + self.b
        return y_hat
    def backprop(self, x, err):
        w_grad = x * err
        b_grad = 1 * err
        return w_grad, b_grad
    def fit(self, x, y, epochs = 100):
        for i in range(epochs):
            for x_i, y_i in zip(x, y):
                y_hat = self.forpass(x_i)
                err = -(y_i - y_hat)
                w_grad, b_grad = self.backprop(x_i, err)
                self.w -= w_grad
                self.b -= b_grad

neuron = Neuron()
neuron.fit(x,y)
#for문으로 학습한 것과 유사하다
plt.scatter(x, y)
pt1 = (-0.1, -0.1 * neuron.w + neuron.b)
pt2 = (0.15, 0.15 * neuron.w + neuron.b)
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#이상 딥러닝 당뇨병 데이터를 이용한 실습이었습니다.