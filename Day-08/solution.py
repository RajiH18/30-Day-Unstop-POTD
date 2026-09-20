def process_entries(n, m, chamber_values, entries):
     
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    dist = [0] * (n + 1)

    
    heap = [0] * (n + 1)

   
    value = [0] + chamber_values

    
    for i in range(1, n + 1):
        if value[i] > 0:
            heap[i] = i
            dist[i] = 1

    def better(a, b):
        
        if value[a] != value[b]:
            return value[a] > value[b]
        return a < b

    def merge(a, b):
        
        if a == 0:
            return b
        if b == 0:
            return a

        if not better(a, b):
            a, b = b, a

        right[a] = merge(right[a], b)

       
        if dist[left[a]] < dist[right[a]]:
            left[a], right[a] = right[a], left[a]

        dist[a] = dist[right[a]] + 1

        return a

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    results = []

    for entry in entries:
        if entry[0] == 'LINK':
            u, v = entry[1], entry[2]

            ru = find(u)
            rv = find(v)

            if ru != rv:
               
                if size[ru] < size[rv]:
                    ru, rv = rv, ru

                parent[rv] = ru
                size[ru] += size[rv]

                
                heap[ru] = merge(heap[ru], heap[rv])

        else:  
            x = entry[1]
            root = find(x)

            h = heap[root]

            if h == 0:
                results.append(("EMPTY",))
            else:
               
                results.append((h, value[h]))

                
                heap[root] = merge(left[h], right[h])

               
                left[h] = 0
                right[h] = 0
                dist[h] = 0

    return results


def main():
    import sys

    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    m = int(data[1])

    chamber_values = list(map(int, data[2:n + 2]))

    entries = []
    index = n + 2

    for _ in range(m):
        entry_type = data[index]
        index += 1

        if entry_type == b'LINK':
            u = int(data[index])
            v = int(data[index + 1])
            entries.append(('LINK', u, v))
            index += 2

        elif entry_type == b'CLAIM':
            x = int(data[index])
            entries.append(('CLAIM', x))
            index += 1

    results = process_entries(n, m, chamber_values, entries)

    for result in results:
        if len(result) == 1:
            print(result[0])
        else:
            print(result[0], result[1])


if __name__ == "__main__":
    main()