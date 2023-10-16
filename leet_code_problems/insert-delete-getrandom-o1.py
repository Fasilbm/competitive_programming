class RandomizedSet(object):

    def __init__(self):
        self.store=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.store:
            self.store.append(val)
            return True
        return False
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.store:
            self.store.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        idx = random.randint(0,len(self.store)-1 )
        return self.store[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
