students = [*range(1, 31)]
good = [*map(int, open(0).read().split())]
bad = [x for x in students if x not in good]
print(' '.join(str(x) for x in bad))
