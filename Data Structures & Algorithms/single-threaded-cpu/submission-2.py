class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue = []
        processQueue = []

        for i, item in enumerate(tasks):
            enqueue.append([item[0], item[1], i])

        heapq.heapify(enqueue)
        
        res = []
        count = 0
        wait = 0
        while processQueue or enqueue:
            while (enqueue and enqueue[0][0] <= count) or not processQueue:
                enqTime, processTime, index = heapq.heappop(enqueue)
                heapq.heappush(processQueue, [processTime, index, enqTime])

            if processQueue:
                processTime, ind, eTime = heapq.heappop(processQueue)
                res.append(ind)
                if count < eTime:
                    count = eTime
                count += processTime

        return res

            

            
        

        