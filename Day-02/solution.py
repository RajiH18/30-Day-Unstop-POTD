def count_sensor_pairs(n, D, edges):
    # User logic goes here
    # Parameters:
    # n: Number of sensors
    # D: Lag tolerance
    # edges: List of tuples representing the connections (u, v, w)
    # Return the number of unordered sensor pairs with total path lag at most D
    graph=[[] for _ in range(n+1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    removed = [False] * (n + 1)

    def find_centroid(start):
        parent = {start: 0}
        order = [start]

        for node in order:
            for neighbor, weight in graph[node]:
                if neighbor != parent[node] and not removed[neighbor]:
                    parent[neighbor] = node
                    order.append(neighbor)

        size = {}

        for node in reversed(order):
            size[node] = 1

            for neighbor, weight in graph[node]:
                 if not removed[neighbor] and parent.get(neighbor) == node:
                        size[node] += size[neighbor]
        total = len(order)

        for node in order:
            largest_part = total - size[node]


            for neighbor, weight in graph[node]:
                if not removed[neighbor] and parent.get(neighbor) == node:
                    largest_part = max(largest_part, size[neighbor])

            if largest_part <= total // 2:
                return node

        return start

    def count_pairs(distances):
        distances.sort()

        left = 0
        right = len(distances) - 1
        count = 0

        while left < right:
            if distances[left] + distances[right] <= D:
                count += right - left
                left += 1
            else:
                right -= 1

        return count

    def collect_distances(start, parent, initial_distance):
        distances = []

        stack = [(start, parent, initial_distance)]

        while stack:
            node, parent, distance = stack.pop()

            distances.append(distance)

            for neighbor, weight in graph[node]:
                if neighbor != parent and not removed[neighbor]:
                    stack.append(
                        (neighbor, node, distance + weight)
                    )

        return distances

    answer = 0
    def decompose(start):
        nonlocal answer

        centroid = find_centroid(start)
        all_distances = [0]
        subtrees = []

        for neighbor, weight in graph[centroid]:

            if removed[neighbor]:
                continue

            distances = collect_distances(
                neighbor,
                centroid,
                weight
            )
            subtrees.append(distances)
            all_distances.extend(distances)
        answer += count_pairs(all_distances)
        for distances in subtrees:
            answer -= count_pairs(distances)
        removed[centroid] = True
        for neighbor, weight in graph[centroid]:

            if not removed[neighbor]:
                decompose(neighbor)

    decompose(1)    
    return answer  # Placeholder return; replace with actual logic


if __name__ == "__main__":
    n, D = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    # Call the user logic function and print the result
    result = count_sensor_pairs(n, D, edges)
    
    print(result)
