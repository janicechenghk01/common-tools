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
        
    def test_hset(self):
        pinItemsDict = {
            '1': "['123456','456789']",
            '2': "['123456','456789']",
            '3': "['123456','456789']"
        }
        for pinPos in pinItemsDict:
            pinItemsArray = pinItemsDict.get(pinPos)
            self.r.hset('pinItems', pinPos, pinItemsArray)

    def test_hgetall(self):
        res = self.r.hgetall('pinItems')
        return {i.decode(): eval(res.get(i).decode()) for i in res}

    def test_hexists(self):
        res = self.r.hexists('pinItems','1')
        print(res)

