import numpy as np

n, m, l = map(int, input().split())
np.random.seed(42)
Z = np.random.rand(n, m, l)
