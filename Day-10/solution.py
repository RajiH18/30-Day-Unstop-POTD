def process_log_entries(M, log_entries):
    import heapq

    MAX_BIT = 19

    # Trie children
    children = [[-1, -1]]

    # Each node stores (station_id, code) in a min-heap
    heaps = [[]]

    # Currently active station -> code
    active = {}

    def new_node():
        children.append([-1, -1])
        heaps.append([])
        return len(children) - 1

    def insert(station_id, code):
        node = 0

        heapq.heappush(heaps[node], (station_id, code))

        for bit in range(MAX_BIT, -1, -1):
            b = (code >> bit) & 1

            if children[node][b] == -1:
                children[node][b] = new_node()

            node = children[node][b]
            heapq.heappush(heaps[node], (station_id, code))

    def clean(node):
        # Remove stale entries.
        while heaps[node]:
            station_id, code = heaps[node][0]

            if active.get(station_id) == code:
                break

            heapq.heappop(heaps[node])

    def check(code):
        node = 0
        deviation = 0

        for bit in range(MAX_BIT, -1, -1):
            b = (code >> bit) & 1
            opposite = 1 - b

            # Prefer opposite bit to maximize XOR
            nxt = children[node][opposite]

            if nxt != -1:
                clean(nxt)

                if heaps[nxt]:
                    deviation |= (1 << bit)
                    node = nxt
                    continue

            # Otherwise take same bit
            nxt = children[node][b]
            node = nxt

        # At this point, every station in this node
        # produces the same maximum XOR.
        clean(node)

        station_id, _ = heaps[node][0]

        return deviation, station_id

    results = []

    for entry in log_entries:

        if entry[0] == 'ON':
            station_id = entry[1]
            code = entry[2]

            active[station_id] = code
            insert(station_id, code)

        elif entry[0] == 'OFF':
            station_id = entry[1]

            # Lazy deletion.
            # Old entries remain in heaps but are ignored by clean().
            del active[station_id]

        else:  # CHECK
            code = entry[1]

            deviation, witness = check(code)
            results.append((deviation, witness))

    return results


def main():
    import sys

    data = sys.stdin.read().strip().split('\n')

    M = int(data[0])

    log_entries = []

    for line in data[1:M + 1]:
        parts = line.split()

        if parts[0] == 'ON':
            log_entries.append(
                ('ON', int(parts[1]), int(parts[2]))
            )

        elif parts[0] == 'OFF':
            log_entries.append(
                ('OFF', int(parts[1]))
            )

        elif parts[0] == 'CHECK':
            log_entries.append(
                ('CHECK', int(parts[1]))
            )

    results = process_log_entries(M, log_entries)

    for deviation, witness in results:
        print(deviation, witness)


if __name__ == "__main__":
    main()