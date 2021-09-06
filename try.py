import heapq
def reduce_sum(lst):
    heapq.heapify(lst)
    s = 0
    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        s += first + second
        heapq.heappush(lst, first + second)
    return s

a = [1,2,4,5]

print(reduce_sum(a))