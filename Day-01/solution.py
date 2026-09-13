def process_scan_events(n, k, events):
    scan_counts = {}

    for op, id in events:
        if op == '+':
            scan_counts[id] = scan_counts.get(id, 0) + 1
        elif op == '-':
            scan_counts[id] = scan_counts.get(id, 0) - 1

    result=[]
    for id in scan_counts:
        if scan_counts[id]>0:
            result.append((id, scan_counts[id]))

    sorted_counts = sorted(result, key=lambda x: x[1], reverse=True)
    return sorted_counts[:k]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    n, k = map(int, data[0].split())
    events = []
    for line in data[1:n+1]:
        op, id_str = line.split()
        events.append((op, int(id_str)))

    result = process_scan_events(n, k, events)

    for id, count in result:
        print(id, count)


if __name__ == "__main__":
    main()
