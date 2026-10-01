def process_events(n, district_data, q, events):
    """
    Write your logic here.
    Parameters:
        n (int): Number of districts
        district_data (list): List of tuples [(district_code, initial_rating), ...]
        q (int): Number of events
        events (list): List of events ["LINK X Y", "BOOST X V", "QUERY X"]
    Returns:
        list: List of results for each QUERY event
    """

    
    district_id = {}

    ratings = [0] * n

    for i, (code, rating) in enumerate(district_data):
        district_id[code] = i
        ratings[i] = rating

    
    parent = list(range(n))
    size = [1] * n

    
    component_max = ratings[:]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return

       
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]

        
        component_max[root_a] = max(
            component_max[root_a],
            component_max[root_b]
        )

    results = []

    for event in events:
        parts = event.split()
        operation = parts[0]

        if operation == "LINK":
            x = district_id[parts[1]]
            y = district_id[parts[2]]

            union(x, y)

        elif operation == "BOOST":
            x = district_id[parts[1]]
            value = int(parts[2])

            ratings[x] += value

            root = find(x)

            if ratings[x] > component_max[root]:
                component_max[root] = ratings[x]

        elif operation == "QUERY":
            x = district_id[parts[1]]

            root = find(x)
            results.append(component_max[root])

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])  
    district_data = []
    
    for i in range(1, n + 1):
        district_code, initial_rating = data[i].split()
        district_data.append((district_code, int(initial_rating)))
    
    q = int(data[n + 1])  
    events = data[n + 2:n + 2 + q]  
    
   
    results = process_events(n, district_data, q, events)
    
   
    for result in results:
        print(result)

if __name__ == "__main__":
    main()