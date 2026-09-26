def check_reachability(n, m, q, corridors, scenarios):
    
    corridors.sort(key=lambda x: x[2])

    
    indexed_scenarios = []

    for i, (a, b, budget) in enumerate(scenarios):
        indexed_scenarios.append((budget, a, b, i))

    
    indexed_scenarios.sort()

    
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
            return

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]

    results = ["NO"] * q

    corridor_index = 0

    for budget, a, b, query_index in indexed_scenarios:

        
        while (
            corridor_index < m
            and corridors[corridor_index][2] <= budget
        ):
            u, v, cost = corridors[corridor_index]
            union(u, v)
            corridor_index += 1

        
        if find(a) == find(b):
            results[query_index] = "YES"

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    index = 3
    corridors = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        cost = int(data[index + 2])
        corridors.append((u, v, cost))
        index += 3
    scenarios = []
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        budget = int(data[index + 2])
        scenarios.append((a, b, budget))
        index += 3
    results = check_reachability(n, m, q, corridors, scenarios)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()