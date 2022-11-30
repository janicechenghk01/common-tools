import redis

redis_host = 'localhost'
redis_port = 6379


def get_connection():
	conn = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
	return conn


class TestString(object):
	def __init__(self):
        self.r = get_connection()

    def test_set(self):
        res = self.r.set('user1','juran-1')
        print(res)

	def test_get(self):
        res = self.r.get('user1')
        print(res)

    def test_mset(self):
        d = {
            'user2':'juran-2',
            'user3':'juran-3'
        }
        res = self.r.mset(d)

    def test_mget(self):
        l = ['user2','user3']
        res = self.r.mget(l)
        print(res)

	def test_del(self):
        self.r.delete('user2')



class TestList(object):
    def __init__(self):
        self.r = get_connection()

    def test_push(self):
        res = self.r.lpush('common','1')
        res = self.r.rpush('common','2')
        # res = self.r.rpush('jr','123')

    def test_pop(self):
        res = self.r.lpop('common')
        res = self.r.rpop('common')

    def test_range(self):
        res = self.r.lrange('common',0,-1)
        print(res)



class TestSet(object):
    def __init__(self):
        self.r = get_connection()

    def test_sadd(self):
        res = self.r.sadd('set01','1','2')
        lis = ['Cat','Dog']
        res = self.r.sadd('set02',lis)

    def test_del(self):
        res = self.r.srem('set01',1)

    def test_pop(self):
        res = self.r.spop('set02')



class TestHash(object):
    def __init__(self):
        self.r = get_connection()
	
    def test_hset(self):
        dic = {
            'id':1,
            'name':'huawei'
        }
        res = self.r.hmset('mobile',dic)

    def test_hgetall(self):
        res = self.r.hgetall('mobile')

    def test_hexists(self):
        res = self.r.hexists('mobile','id')
        print(res)



class TestPinItemSet(object):    
    def __init__(self):
        self.r = get_connection()
        self.hash_key = 'pinItems'
        
    def test_hset(self):
        pinItemsDict = {
            '1': '["833756", "832878"]',
            '3': '["832732", "833032"]',
            '5': '["832420", "833801"]',
            '7': '["831886", "833692"]',
            '9': '["832417", "832986"]'
        }
        for pinPos in pinItemsDict:
            pinItemsArray = pinItemsDict.get(pinPos)
            self.r.hset(self.hash_key, pinPos, pinItemsArray)

    def test_hgetall(self):
        res = self.r.hgetall(self.hash_key)
        return {i.decode(): eval(res.get(i).decode()) for i in res}

    def test_hexists(self, idx='1'):
        res = self.r.hexists(self.hash_key, idx)
        return res
        
    def test_hdel(self, delete_all=False, idx='1'):
        if delete_all:
            for k in self.test_hgetall():
                self.r.hdel(self.hash_key, k)
            print(f'Deleted All {self.hash_key} Done!')
        else:
            res = self.r.hdel(self.hash_key, idx)
            print(f'Delete {self.hash_key} with key={idx} Done!')

