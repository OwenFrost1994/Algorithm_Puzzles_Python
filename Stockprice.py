def maxProfit(prices):
    n = len(prices)
    maxv = 0
    buy = 0
    sell = 0
    a = 0
    b = 0
    while a < n and b < n:
        if prices[b] < prices[a]:
            a = b
        else:
            if abs(prices[b] - prices[a]) >= maxv:
                buy = a
                sell = b
                maxv = abs(prices[b] - prices[a])
        b += 1
    if maxv == 0:
        retun 
    return buy + 1, sell + 1, maxv
print(maxProfit([7,1,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))