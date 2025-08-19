def gen_turns(n):
    if n == 0:
        return
    yield from gen_turns(n - 1)
    yield 60
    yield from gen_turns(n - 1)
    yield -120
    yield from gen_turns(n - 1)
    yield 60
    yield from gen_turns(n - 1)

def main():
    import sys
    n_line = sys.stdin.readline().strip()
    n = int(n_line)

    for angle in gen_turns(n):
        print(f"turn {angle}")

if __name__ == "__main__":
    main()
