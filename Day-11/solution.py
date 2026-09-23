def calculate_min_fuel_cost(n, m, R, legs, requests):
    import heapq

    graph = [[] for _ in range(n + 1)]
    for u, v, fuel, turb in legs:
        graph[u].append((v, fuel, turb))

    INF = 10**30
    dist = [[INF] * (R + 1) for _ in range(n + 1)]
    dist[1][0] = 0
    pq = [(0, 1, 0)]

    while pq:
        fuel, node, turb = heapq.heappop(pq)

        if fuel != dist[node][turb]:
            continue

        for nxt, edge_fuel, edge_turb in graph[node]:
            new_turb = turb + edge_turb

            if new_turb > R:
                continue

            new_fuel = fuel + edge_fuel

            if new_fuel < dist[nxt][new_turb]:
                dist[nxt][new_turb] = new_fuel
                heapq.heappush(
                    pq,
                    (new_fuel, nxt, new_turb)
                )

    best = [[INF] * (R + 1) for _ in range(n + 1)]

    for node in range(1, n + 1):
        current = INF

        for t in range(R + 1):
            current = min(current, dist[node][t])
            best[node][t] = current

    results = []

    for dest, tol in requests:
        answer = best[dest][tol]

        if answer == INF:
            results.append(-1)
        else:
            results.append(answer)

    return results


def main():
    import sys

    data = sys.stdin.read().strip().split()

    index = 0

    n = int(data[index])
    m = int(data[index + 1])
    R = int(data[index + 2])
    index += 3

    legs = []

    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        fuel = int(data[index + 2])
        turb = int(data[index + 3])

        legs.append((u, v, fuel, turb))
        index += 4

    q = int(data[index])
    index += 1

    requests = []

    for _ in range(q):
        dest = int(data[index])
        tol = int(data[index + 1])

        requests.append((dest, tol))
        index += 2

    results = calculate_min_fuel_cost(
        n, m, R, legs, requests
    )

    for result in results:
        print(result)


if __name__ == "__main__":
    main()