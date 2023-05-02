# get n percent of user for A/B Testing
# [0, 17, 22, 26, 48, 63, 81, 91, 93, 97]
def get_n_buckets(n=10):
    import random
    seq = [i for i in range(100)]
    buckets = random.sample(seq, n)
    buckets.sort()
    return buckets


def generate_mock_data(item_list):
    """
    item_list = [841385, 841760, 841167, 841494, 841046, 841478, 841768, 841061, 841253, 841524]
    generate_mock_data(item_list)
    >> {'1': '["841091", "840966"]', '3': '["841370", "841609"]'}
    """
    
    import json
    import numpy as np
    
    pinItemsDict = {}
    np.random.shuffle(item_list)
    
    pinPosList = [1,3,5]
    
    for i in pinPosList:
        arr = []
        for _ in range(2):
            arr.append(str(item_list.pop(1)))
        pinItemsDict[str(i)] = json.dumps(arr)

    return pinItemsDict


def get_feed_from_seldon(
    url: str = 'localhost',
    uid: str = '',
    aid: int = -1,
    ingress_id: str = '',
    type: str = 'article'
) -> dict:
    """
    uid = '37241C51-30C0-42E0-B4A7-000676BE99FD'
    response = get_feed_from_seldon(url, uid)
    """
    
    import requests

    instance = {
        'uid': uid
    }
    if aid != -1:
        instance['aid'] = aid
        
    payload = {
        'jsonData': {
            'instances': [instance],
            'config': {'top_n': 10}
        }
    }
    headers = {'Content-Type': 'application/json'}
    if ingress_id:
        headers[REQUEST_ID_HEADER] = ingress_id

    res = {}

    response = requests.post(url, json=payload, headers=headers, timeout=0.5)
    return response
