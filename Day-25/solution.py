
import sys

def user_logic(n, m, category, edges):
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    minimum = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total_cost = 0

    edges.sort(key=lambda x: x[2])

    for u, v, cost in edges:
        ru = find(u)
        rv = find(v)

        if ru == rv:
            continue

        if size[ru] < size[rv]:
            ru, rv = rv, ru

        parent[rv] = ru
        size[ru] += size[rv]
        minimum[ru] = min(minimum[ru], minimum[rv])

        total_cost += cost

    best_root = 1

    for i in range(1, n + 1):
        if parent[i] == i:
            if size[i] > size[best_root]:
                best_root = i
            elif size[i] == size[best_root]:
                if minimum[i] < minimum[best_root]:
                    best_root = i

    counts = {}

    for i in range(1, n + 1):
        if find(i) == best_root:
            c = category[i - 1]
            counts[c] = counts.get(c, 0) + 1

    dominant_category = -1
    dominant_count = 0

    for c, count in counts.items():
        if count > dominant_count:
            dominant_category = c
            dominant_count = count
        elif count == dominant_count and c < dominant_category:
            dominant_category = c

    return total_cost, size[best_root], dominant_category, dominant_count


def main():
    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    category = list(map(int, data[2:n + 2]))

    edges = []
    index = n + 2

    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        cost = int(data[index + 2])
        edges.append((u, v, cost))
        index += 3

    result = user_logic(n, m, category, edges)
    print(*result)


if __name__ == "__main__":
    main()
