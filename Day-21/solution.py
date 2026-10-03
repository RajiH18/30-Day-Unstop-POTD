def process_stream(n, C, commands):
    """
    Write your logic here.
    Parameters:
        n (int): Number of stream entries
        C (int): Snapshot size
        commands (list): List of tuples where each tuple is either ('S', name) or ('R',)
    Returns:
        list: A list of strings, each string contains species names separated by single spaces for each 'R' command
    """
    import heapq

    frequency = {}
    heap = []
    results = []

    for command in commands:

        if command[0] == 'S':
            name = command[1]

            frequency[name] = frequency.get(name, 0) + 1

            heapq.heappush(
                heap,
                (-frequency[name], name)
            )

        else:  
            selected = []

            while heap and len(selected) < C:
                neg_count, name = heapq.heappop(heap)

               
                if -neg_count != frequency[name]:
                    continue

                selected.append(name)

            
            for name in selected:
                heapq.heappush(
                    heap,
                    (-frequency[name], name)
                )

            results.append(" ".join(selected))

    return results


def main():
    import sys
    input = sys.stdin.read

    
    data = input().strip().split('\n')

    n, C = map(int, data[0].split())

    commands = []

    for i in range(1, n + 1):
        line = data[i].strip().split()

        if line[0] == 'S':
            commands.append(('S', line[1]))

        elif line[0] == 'R':
            commands.append(('R',))

    results = process_stream(n, C, commands)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()