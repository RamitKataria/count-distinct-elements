with open('data.csv', 'r') as file:
    s_set = set(file)
print(len(s_set))



import math
import sys
alpha = 0.0165
l = 9731

class DistinctElements:
    Z = []
    
    def __init__(self, stream):
        self.Z = [1] * l
        t = 0
        while True:
            a_t = stream.readline()
            if not a_t:
                break
                
            for i in range(l):
                self.Z[i] = min(self.Z[i], self.hash(i, a_t))
                
    def hash(self, l, string):
        orig_hash = hash(f'{l}:{string}')
        if orig_hash < 0:
            norm_hash = orig_hash / (sys.maxsize + 1)
        else:
            norm_hash = orig_hash / sys.maxsize
        return (norm_hash + 1) / 2

    def estimate_cardinality(self):
        Z_sorted = sorted(self.Z)
        M = Z_sorted[len(Z_sorted)//2]
        d_min = math.log(0.5+alpha)/math.log(1-M)
        d_max = math.log(0.5-alpha)/math.log(1-M)
        return (d_min, d_max)
    
with open('data.csv', 'r') as file:
    DE_estimator = DistinctElements(file)
print(DE_estimator.estimate_cardinality())



import hyperloglog
hll = hyperloglog.HyperLogLog(0.01)
with open('data.csv', 'r') as file:
    for line in file:
        hll.add(line)
print(len(hll))
