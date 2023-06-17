import matplotlib.pyplot as plt

# x = [39, 40, 41, 42, 41]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [13, 46, 19, 7, 50, 68, 74, -98, -99]
# y = [2 * t for t in x]
print("X", x, "Y", y)
n = len(x)
meanx = sum(x) / n
meany = sum(y) / n
print(meanx, meany)
dx = [meanx - x for x in x]
dy = [meany - y for y in y]
print("DX", dx, "Dy", dy)
dx2 = [x * x for x in dx]
# print(dx2)
dxdy = [dx[i] * dy[i] for i in range(n)]
# print(dxdy)
r = (sum(dxdy) - sum(dx) * sum(dy) / n) / (sum(dx2) - sum(dx) * sum(dx) / n)
print("R", r)


def predict(x, xmean, ymean, r):
    y = ymean + r * (x - xmean)
    return y


valueofx = 30
predictedy = predict(valueofx, meanx, meany, r)
print("X=", valueofx, "Y", predictedy)

plt.plot(x, y)
plt.scatter(x, y)
# plt.show()
py = [predict(t, meanx, meany, r) for t in x]

plt.plot(x, py)
plt.scatter(x, py)
plt.show()
