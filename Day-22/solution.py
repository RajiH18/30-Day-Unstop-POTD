def user_logic(n, q, collections, stretches):
    import math

    
    values = sorted(set(collections))
    value_id = {value: i for i, value in enumerate(values)}

    arr = [value_id[value] for value in collections]

    
    block_size = int(math.sqrt(n)) + 1

    
    queries = []

    for i, (l, r) in enumerate(stretches):
        l -= 1
        r -= 1
        queries.append((l, r, i))

    queries.sort(
        key=lambda x: (
            x[0] // block_size,
            x[1] if (x[0] // block_size) % 2 == 0 else -x[1]
        )
    )

    frequency = [0] * len(values)

    
    frequency_count = [0] * (n + 1)

    results = [0] * q

    current_left = 0
    current_right = -1
    current_max = 0

    for left, right, query_index in queries:

       
        while current_left > left:
            current_left -= 1

            value = arr[current_left]
            old_frequency = frequency[value]

            if old_frequency > 0:
                frequency_count[old_frequency] -= 1

            new_frequency = old_frequency + 1
            frequency[value] = new_frequency
            frequency_count[new_frequency] += 1

            if new_frequency > current_max:
                current_max = new_frequency

      
        while current_right < right:
            current_right += 1

            value = arr[current_right]
            old_frequency = frequency[value]

            if old_frequency > 0:
                frequency_count[old_frequency] -= 1

            new_frequency = old_frequency + 1
            frequency[value] = new_frequency
            frequency_count[new_frequency] += 1

            if new_frequency > current_max:
                current_max = new_frequency

        
        while current_left < left:

            value = arr[current_left]
            old_frequency = frequency[value]

            frequency_count[old_frequency] -= 1

            new_frequency = old_frequency - 1
            frequency[value] = new_frequency

            if new_frequency > 0:
                frequency_count[new_frequency] += 1

            current_left += 1

            while current_max > 0 and frequency_count[current_max] == 0:
                current_max -= 1

        
        while current_right > right:

            value = arr[current_right]
            old_frequency = frequency[value]

            frequency_count[old_frequency] -= 1

            new_frequency = old_frequency - 1
            frequency[value] = new_frequency

            if new_frequency > 0:
                frequency_count[new_frequency] += 1

            current_right -= 1

            while current_max > 0 and frequency_count[current_max] == 0:
                current_max -= 1

        results[query_index] = current_max

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    q = int(data[1])
    
    collections = list(map(int, data[2:n+2]))
    
    stretches = []
    index = n + 2
    for _ in range(q):
        l = int(data[index])
        r = int(data[index+1])
        stretches.append((l, r))
        index += 2
    
    results = user_logic(n, q, collections, stretches)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()