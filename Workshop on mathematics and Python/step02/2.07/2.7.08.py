def convert(L):
    return [int(x) for x in L]

def maxId(L):
  L = convert(L)
  return L.index(max(L))
