def process_requests(q, operations):
    import heapq

    heap = []
    active = {}

    arrival_order = 0
    results = []

    for operation in operations:
        parts = operation.split()
        command = parts[0]

        if command == "ADD":
            request_id = int(parts[1])
            priority = int(parts[2])

            active[request_id] = (priority, arrival_order)

            heapq.heappush(
                heap,
                (-priority, arrival_order, request_id)
            )

            arrival_order += 1

        elif command == "UPDATE":
            request_id = int(parts[1])
            new_priority = int(parts[2])

            if request_id in active:
                _, order = active[request_id]

                active[request_id] = (new_priority, order)

                heapq.heappush(
                    heap,
                    (-new_priority, order, request_id)
                )

        elif command == "CANCEL":
            request_id = int(parts[1])

            if request_id in active:
                del active[request_id]

        elif command == "DISPATCH":
           
            while heap:
                neg_priority, order, request_id = heap[0]

                if request_id not in active:
                    heapq.heappop(heap)
                    continue

                current_priority, current_order = active[request_id]

                if current_priority != -neg_priority:
                    heapq.heappop(heap)
                    continue

                if current_order != order:
                    heapq.heappop(heap)
                    continue

                break

            if not heap:
                results.append(-1)
            else:
                _, _, request_id = heapq.heappop(heap)

                del active[request_id]

                results.append(request_id)

    for result in results:
        print(result)


def main():
    import sys
    input = sys.stdin.read

  
    data = input().strip().split('\n')

    q = int(data[0].strip())
    operations = []

    for line in data[1:q + 1]:
        operations.append(line)

    process_requests(q, operations)


if __name__ == "__main__":
    main()