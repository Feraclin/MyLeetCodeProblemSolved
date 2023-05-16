

# задаем входные данные
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        import collections
        # определяем количество вершин в графе
        n = len(colors)
        # создаем пустой граф
        graph = collections.defaultdict(list)
        # создаем список для хранения степеней вершин
        indegree = [0] * n
        # заполняем граф и список степеней вершин
        for u, v in edges:
            graph[v].append(u)
            indegree[u] += 1
        # создаем список для хранения количества цветов в каждой вершине
        count = [collections.defaultdict(int) for _ in range(n)]
        # создаем очередь с вершинами, у которых степень равна 0
        q = collections.deque(filter(lambda i: not indegree[i], range(n)))
        # создаем переменную для хранения количества посещенных вершин
        seen = 0
        # создаем переменную для хранения максимального количества цветов в пути
        ans = 0
        # обходим граф
        while q:
            # извлекаем вершину из очереди
            curr = q.popleft()
            # увеличиваем количество цветов в текущей вершине
            count[curr][colors[curr]] += 1
            # обновляем максимальное количество цветов в пути
            ans = max(ans, count[curr][colors[curr]])
            # увеличиваем количество посещенных вершин
            seen += 1
            # обходим соседей текущей вершины
            for v in graph[curr]:
                for c in count[curr]:
                    count[v][c] = max(count[v][c], count[curr][c])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if seen < n:
            return -1
        return ans


print(Solution().largestPathValue(colors, edges))