class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        adj_list={}
        n=len(rooms)
        for i,j in enumerate(rooms):
            adj_list[i]=j

        queue=deque(rooms[0])
        visited=set()
        while queue:
            size=len(queue)
            for i in range(size):
                key=queue.popleft()
                visited.add(key)
                for node in adj_list[key]:
                    if node not in visited:
                        queue.append(node)
        for i in range(1,n):
            if i not in visited:
                return False
        return True
