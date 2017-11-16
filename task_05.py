class HashTable:
    def __init__(self, hash_type, values):
        self.hashMap = eval("HashTable{}(values)".format(hash_type))
        self.valuesArr = values

    def get_collisions_amount(self):
        return self.hashMap.collisions

    def find_sum(self, s):
        for value in self.valuesArr:
            if self.hashMap.search(s - value):
                return value, s - value


class DefaultHasher:
    def __init__(self, values):
        self.collisions = 0
        if len(values) <= 10:
            self.m = 29
        elif len(values) <= 1000:
            self.m = 2999
        elif len(values) <= 100000:
            self.m = 299993
        else:
            self.m = 1610612741
        self.values = [None for _ in range(self.m)]
        self.iter = 0
        for value in values:
            self.add(value)

    def add(self, value):
        raise NotImplementedError

    def hash(self, value):
        raise NotImplementedError

    def search(self, value):
        raise NotImplementedError

    def hash1(self, value):
        return value % self.m

    def hash2(self, value):
        return int((self.m * (value * ((5 ** 0.5 - 1) / 2) % 1)) // 1)

    def __setitem__(self, key, value):
        self.values[key] = value

    def __getitem__(self, key):
        try:
            return self.values[key]
        except:
            return None


class ChainHasher(DefaultHasher):
    def add(self, value):
        key = self.hash(value)
        if self[key]:
            self[key].append(value)
            self.collisions += 1
        else:
            self[key] = [value]

    def search(self, value):
        if self[self.hash(value)] and value in self[self.hash(value)]:
            return self.hash(value)
        else:
            return None


class HashTable1(ChainHasher):
    def hash(self, value):
        return self.hash1(value)


class HashTable2(ChainHasher):
    def hash(self, value):
        return self.hash2(value)


class OpenAdrHasher(DefaultHasher):
    def add(self, value):
        i = 0
        curKey = self.hashi(value, i)
        while (self[curKey] and i < len(self.values)):
            i += 1
            curKey = self.hashi(value, i)
        if i >= len(self.values):
            raise OverflowError("HashTable overload")
        if i > 0:
            self.collisions += 1
        self[curKey] = value
        return curKey

    def search(self, value):
        i = 0
        curKey = self.hashi(value, i)
        while (self[curKey] and i < len(self.values)):
            if self[curKey] == value:
                return curKey
            i += 1
            curKey = self.hashi(value, i)
        return None

    def hashi(self, value, i):
        raise NotImplementedError


class HashTable3(OpenAdrHasher):
    def hashi(self, value, i):
        return (self.hash2(value) + i) % self.m


class HashTable4(OpenAdrHasher):
    def hashi(self, value, i):
        return (self.hash2(value) + 3 * i + i ** 2) % self.m


class HashTable5(OpenAdrHasher):
    def hashi(self, value, i):
        return (self.hash2(value) + i * self.hash1(value)) % self.m
