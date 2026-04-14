class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        visited = set()

        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                d = int(state[i])
                neighbors.append(state[:i] + str((d + 1) % 10) + state[i+1:])
                neighbors.append(state[:i] + str((d - 1) % 10) + state[i+1:])
            return neighbors

        def bfs(lock): 
            queue = collections.deque()
            queue.append((0,lock))
            while queue: 
                lock = queue.popleft()
                priority = lock[0]
                comb = lock[1]

                if comb in visited or comb in deadends: 
                    continue
                if comb == target: 
                    return priority

                visited.add(comb)
                neighbors = get_neighbors(comb)
                for neighbor in neighbors: 
                    queue.append((priority+1, neighbor))
            return -1
        
        
        return bfs("0000") if "0000" not in deadends else -1




