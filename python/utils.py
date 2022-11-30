# get n percent of user for A/B Testing
# [0, 17, 22, 26, 48, 63, 81, 91, 93, 97]
def get_n_buckets(n=10):
    seq = [i for i in range(100)]
    buckets = random.sample(seq, n)
    buckets.sort()
    return buckets

# item_list = 841385, 841760, 841167, 841494, 841046, 841478, 841768, 841061, 841253, 841524]
# {'1': '["841091", "840966"]', '3': '["841370", "841609"]'}
def generate_mock_data(item_list):
    
    import json
    import numpy as np
    
    pinItemsDict = {}
    np.random.shuffle(item_list)
    
    pinPosList = [1,3,5,7,9]
    
    for i in pinPosList:
        arr = []
        for j in range(2):
            arr.append(str(item_list.pop(1)))
        pinItemsDict[str(i)] = json.dumps(arr)

    return pinItemsDict