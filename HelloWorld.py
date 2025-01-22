def main():
    n = int(input().strip())
    names = []
    for _ in range(n):
        names.append(input().strip())
    for name in names:
        print(f"Hello, {name}!")
    
if __name__ == "__main__":
    main()