from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if w1 != w2 and w1.startswith(w2):
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break

    queue = deque([c for c in indegree if indegree[c] == 0])
    order = []

    while queue:
        c = queue.popleft()
        order.append(c)
        for neighbor in graph[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(order) if len(order) == len(indegree) else ""

def test_alien_dictionary():
    print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
    print(alien_order(["z", "x"]))
    print(alien_order(["z", "x", "z"]))
    print(alien_order(["abc", "ab"]))
    print(alien_order(["baa", "abcd", "abca", "cab", "cad"]))

if __name__ == "__main__":
    test_alien_dictionary()
