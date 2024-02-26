def search(n, k=0, subset=[]):
    if k==n:
        return subset
    else:
        res1 = search(n, k+1, subset)
        res2 = search(n, k+1, subset+[k])

        return [res1, res2]


print(list(search(3)))

