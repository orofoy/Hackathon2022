def parse():
    with open('testing.txt') as f:
        lines = f.readlines()
        f.close()
        return lines
