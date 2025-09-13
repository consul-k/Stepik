import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    try:
        n = int(data[0].strip())
    except:
        n = 0

    vampires = []
    for i in range(1, 1 + n):
        if i >= len(data):
            break
        line = data[i]
        if ':' in line:
            name, rest = line.split(':', 1)
            name = name.strip()
            weaknesses = [w.strip().lower() for w in rest.split(',') if w.strip()]
        else:
            name = line.strip()
            weaknesses = []
        vampires.append((name, set(weaknesses)))

    if len(data) > 1 + n:
        weapons_line = data[1 + n]
        weapon_traits = {w.strip().lower() for w in weapons_line.split(',') if w.strip()}
    else:
        weapon_traits = set()

    for name, weaknesses in vampires:
        if weaknesses & weapon_traits:
            print(f"Вампир {name} уязвим для оружия!")
        else:
            print(f"Вампир {name} не уязвим для оружия!")

if __name__ == "__main__":
    main()
