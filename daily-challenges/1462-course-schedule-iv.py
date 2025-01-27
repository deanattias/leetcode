class Solution:
    def is_prerequisite(
        self, adj_list: dict, visited: list[bool], src: int, target: int
    ) -> bool:
        visited[src] = True

        if src == target:
            return True

        for adj in adj_list.get(src, []):
            if not visited[adj]:
                if self.is_prerequisite(adj_list, visited, adj, target):
                    return True

        return False

    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj_list = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        result = []

        for query in queries:
            # Reset the visited array for each query
            visited = [False] * numCourses
            result.append(self.is_prerequisite(adj_list, visited, query[0], query[1]))

        return result
