from heapq import *
import random
data=[]
heap=[]
for i in range(10):
    data.append(i)
random.shuffle(data)
print(data)
for i in data:
    heappush(heap,i)
print(heap)
print(heappop(heap)) #弹出最小值
print(heap)
heapreplace(heap,1.5) #弹出最小值 并将1.5入堆
print(heap)
l1=[1,3,5,2,5,3,7]
print(nlargest(1,l1))

