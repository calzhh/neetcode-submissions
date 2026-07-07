import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        helper = [0] * 26
        for letter in tasks:
            helper[ord(letter) - ord('A')] -= 1

        schedule = []
        for element in helper:
            if element < 0:
                schedule.append(element)
        queue = deque()
        heapq.heapify(schedule)
        print(schedule)
        while len(schedule) > 0 or len(queue) > 0:
            cycles += 1
            if schedule:
                cnt = 1 + heapq.heappop(schedule)
                if cnt != 0:
                    queue.append([cnt, n+cycles])
            if queue and queue[0][1] == cycles: 
                heapq.heappush(schedule, queue.popleft()[0])
        return cycles

