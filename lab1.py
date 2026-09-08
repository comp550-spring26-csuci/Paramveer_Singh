def fib_iterative(n, path):
    with open(path, "w") as f:
        a, b = 0, 1
        for _ in range(n):
            f.write(f"{a}\n")
            a, b = b, a + b


if __name__ == "__main__":
    fib_iterative(25, "output/fibonacci.txt")
