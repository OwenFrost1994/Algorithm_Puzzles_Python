import random, math

def main():
    n = int(input().strip())
    m = int(input().strip())
    clauses = []
    for _ in range(m):
        clause = list(map(int, input().split()))
        clauses.append([abs(x) for x in clause] + [int(x/abs(x)) for x in clause])
    print(' '.join(map(str, max3sat(n, m, clauses))))

def max3sat(n, m, clauses):
    satisfied = 0
    while satisfied < math.floor(7*m/8):
        assignment = [random.choice([-1, 1]) for _ in range(n)]
        satisfied = 0
        for a, b, c, e, f, g in clauses:
            clause = [e*assignment[a-1], f*assignment[b-1], g*assignment[c-1]]
            if 1 in clause:
                satisfied += 1
    return assignment

if __name__ == "__main__":
    main()