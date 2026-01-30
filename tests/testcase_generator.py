import random

def generate_test(n, filename):
    with open(filename, "w") as f:
        f.write(f"{n}\n")

        # Hospital preferences
        for _ in range(n):
            prefs = list(range(1, n + 1))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

        # Student preferences
        for _ in range(n):
            prefs = list(range(1, n + 1))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

def main():
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    for n in sizes:
        filename = f"test_n_{n}.in"
        generate_test(n, filename)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
