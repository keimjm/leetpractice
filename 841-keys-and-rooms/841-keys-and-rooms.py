class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:        
        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()
            if room in visited: continue
            visited.add(room)
            stack.extend(rooms[room])
                
        return len(visited) == len(rooms)
            
        