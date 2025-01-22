def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        pairs = []
        for _ in range(n):
            pairs.append([int(input().strip())])
        for i in range(n):
            pairs[i].append(int(input().strip()))
        pairs.sort()
        results.append(Intersect([x[1] for x in pairs])[1])
    for result in results:
        print(result)

def Intersect(arr):
    if len(arr) <=1:
        return arr, 0
    left, l = Intersect(arr[0 : len(arr)//2])
    right, r = Intersect(arr[len(arr)//2 : len(arr)])
    i = 0
    j = 0
    m = 0
    mid = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mid.append(left[i])
            i += 1
        else:
            mid.append(right[j])
            m += len(left) - i
            j += 1
    while i < len(left):
        mid.append(left[i])
        i += 1
    while j < len(right):
        mid.append(right[j])
        j += 1
    return mid, l + r + m

if __name__ == "__main__":
    main()