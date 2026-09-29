def compute_notable_readings(n, k, v, s):
    from collections import deque

    frequency = {}
    max_deque = deque()

    results = []

    for i in range(n):
        species = s[i]
        frequency[species] = frequency.get(species, 0) + 1

      
        while max_deque and v[max_deque[-1]] <= v[i]:
            max_deque.pop()

        max_deque.append(i)

        
        window_start = i - k + 1

        while max_deque and max_deque[0] < window_start:
            max_deque.popleft()

        if i >= k:
            old_species = s[i - k]
            frequency[old_species] -= 1

            if frequency[old_species] == 0:
                del frequency[old_species]

        
        if i >= k - 1:
            distinct_count = len(frequency)

            if 2 * distinct_count >= k:
                results.append(v[max_deque[0]])
            else:
                results.append(-1)

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  
    k = int(data[1]) 
    
    v = list(map(int, data[2:n+2]))  
    s = list(map(int, data[n+2:2*n+2])) 
    
    
    result = compute_notable_readings(n, k, v, s)
    
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()