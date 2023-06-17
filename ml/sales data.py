testscores = [40, 70, 50, 60, 80, 50, 90, 40, 60, 60]
sales = [2.5, 6.0, 4.5, 5.0, 4.5, 2.0, 5.5, 3.0, 4.5, 3.0]
n = len(testscores)
meanx = sum(testscores) / n
meany = sum(sales) / n
print(meanx, meany)
dx = [meanx - x for x in testscores]
dy = [meany - y for y in sales]
print(dx, dy)
dx2 = [x * x for x in dx]
print(dx2)
dxdy = [dx[i] * dy[i] for i in range(n)]
print(dxdy)
r = (sum(dxdy) - sum(dx) * sum(dy) / n) / (sum(dx2) - sum(dx) * sum(dx) / n)
print(r)