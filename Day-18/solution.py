def compute_worst_corridor(n, m, corridors, q, queries):
    
    corridors.sort(key=lambda x: x[2])

   
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]

        return True


    tree = [[] for _ in range(n + 1)]

    edges_used = 0

    for u, v, w in corridors:
        if union(u, v):
            tree[u].append((v, w))
            tree[v].append((u, w))

            edges_used += 1

            if edges_used == n - 1:
                break

    
    LOG = n.bit_length()

    up = [[0] * (n + 1) for _ in range(LOG)]
    max_edge = [[0] * (n + 1) for _ in range(LOG)]
    depth = [-1] * (n + 1)

    
    for start in range(1, n + 1):
        if depth[start] != -1:
            continue

        depth[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()

            for v, w in tree[u]:
                if depth[v] != -1:
                    continue

                depth[v] = depth[u] + 1
                up[0][v] = u
                max_edge[0][v] = w

                stack.append(v)

    
    for j in range(1, LOG):
        for v in range(1, n + 1):
            ancestor = up[j - 1][v]

            up[j][v] = up[j - 1][ancestor]

            max_edge[j][v] = max(
                max_edge[j - 1][v],
                max_edge[j - 1][ancestor]
            )

    
    def get_answer(a, b):
        
        if find(a) != find(b):
            return -1

        answer = 0

      
        if depth[a] < depth[b]:
            a, b = b, a

        difference = depth[a] - depth[b]

        for j in range(LOG - 1, -1, -1):
            if difference & (1 << j):
                answer = max(answer, max_edge[j][a])
                a = up[j][a]

        
        if a == b:
            return answer

       
        for j in range(LOG - 1, -1, -1):
            if up[j][a] != up[j][b]:
                answer = max(answer, max_edge[j][a])
                answer = max(answer, max_edge[j][b])

                a = up[j][a]
                b = up[j][b]

       
        answer = max(answer, max_edge[0][a])
        answer = max(answer, max_edge[0][b])

        return answer

    results = []

    for a, b in queries:
        results.append(get_answer(a, b))

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n, m = int(data[index]), int(data[index + 1])
    index += 2

    corridors = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        corridors.append((u, v, w))
        index += 3

    q = int(data[index])
    index += 1

    queries = []
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        queries.append((a, b))
        index += 2

    results = compute_worst_corridor(n, m, corridors, q, queries)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()