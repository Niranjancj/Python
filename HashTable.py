class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % (len(self.data_map))
        return my_hash
    
    def print_hashtable(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
        print('\n')

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index] [i] [0] == key:
                    return self.data_map[index] [i] [1] 
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i] [j] [0])
        return all_keys
    
def two_sum(nums: list, target: int):
    num_map = {}
    
    for i, val in enumerate(nums):
        complement = target - val
        if complement in num_map:
            return [num_map[complement], i]
        num_map[val] = i
    return[]

def subarray_sum(nums, target):
    sum_index  = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return


my_hashtable = HashTable()
my_hashtable.set_item('test', 100)
my_hashtable.set_item('test2', 200)
my_hashtable.set_item('test3', 200)
my_hashtable.print_hashtable()
print(my_hashtable.keys())
