
import sys
import heapq


def user_logic(n, events):
    totals = {}
    versions = {}
    heap = []
    results = []

    for event in events:
        if event[0] == 'BUY':
            ticker_id = event[1]
            units = event[2]

            totals[ticker_id] = totals.get(ticker_id, 0) + units
            versions[ticker_id] = versions.get(ticker_id, 0) + 1

            heapq.heappush(
                heap,
                (-totals[ticker_id], ticker_id, versions[ticker_id])
            )

        elif event[0] == 'PEAK':
            # Remove outdated heap entries
            while heap:
                neg_total, ticker_id, version = heap[0]

                if (versions.get(ticker_id) == version
                        and totals.get(ticker_id, 0) == -neg_total):
                    break

                heapq.heappop(heap)

            neg_total, ticker_id, version = heapq.heappop(heap)
            total = -neg_total

            results.append((ticker_id, total))

            # Reset the settled ticker
            totals[ticker_id] = 0
            versions[ticker_id] += 1

    return results


def main():
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])
    events = []
    i = 1

    for _ in range(n):
        command = data[i]
        i += 1

        if command == 'BUY':
            ticker_id = int(data[i])
            units = int(data[i + 1])
            i += 2
            events.append(('BUY', ticker_id, units))
        else:
            events.append(('PEAK',))

    result = user_logic(n, events)

    output = []
    for ticker_id, units in result:
        output.append(f"{ticker_id} {units}")

    print("\n".join(output))


if __name__ == "__main__":
    main()
