# get n percent of user for A/B Testing
# [0, 17, 22, 26, 48, 63, 81, 91, 93, 97]
def get_n_buckets(n=10):
    seq = [i for i in range(100)]
    buckets = random.sample(seq, n)
    buckets.sort()
    return buckets
