def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        results.append(inversion(arr)[1])
    for result in results:
        print(result)

def inversion(arr):
    if len(arr) <=1:
        return arr, 0
    left, l = inversion(arr[0 : len(arr)//2])
    right, r = inversion(arr[len(arr)//2 : len(arr)])
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