from collections import deque

def dfs(graph, start, search):
    stack = []
    stack.extend(graph[start])

    while len(stack) > 0:
        node = stack.pop()
        print(node)
        if node == search:
            return True
        if node in graph:
            stack.extend(graph[node])

    return False


def bfs(graph, start, search):
    queue = deque()
    queue.extend(graph[start])

    while len(queue) > 0:
        node = queue.popleft()
        print(node)
        if node == search:
            return True
        if node in graph:
            queue.extend(graph[node])

    return False

graph = { 0: [1, 2], 1: [3], 2: [4], 3: [5], 4: [], 5: []}

print(dfs(graph, 0, 5))
print("\n\n")
print(bfs(graph, 0, 5))
