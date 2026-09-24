def process_events(events):
    """
    Process the list of events.
    
    Parameters:
        events (list): A list of tuples where each tuple is either 
                       ('ADD', code, era) or ('QUERY', prefix, era).
    
    Returns:
        list: A list of integers where each integer corresponds to the 
              result of a 'QUERY' operation.
    """
    
    children = [{}]
    era_count = [{}]

    def new_node():
        children.append({})
        era_count.append({})
        return len(children) - 1

    def add(code, era):
        node = 0

      
        era_count[node][era] = era_count[node].get(era, 0) + 1

        
        for ch in code:
            if ch not in children[node]:
                children[node][ch] = new_node()

            node = children[node][ch]

            era_count[node][era] = era_count[node].get(era, 0) + 1

    def query(prefix, era):
        node = 0

        
        for ch in prefix:
            if ch not in children[node]:
                return 0

            node = children[node][ch]

        
        return era_count[node].get(era, 0)

    results = []

    for event in events:
        event_type, code_or_prefix, era = event

        if event_type == "ADD":
            add(code_or_prefix, era)

        else:  
            results.append(query(code_or_prefix, era))

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    Q = int(data[0])  
    events = []
    
    for i in range(1, Q + 1):
        parts = data[i].split()
        event_type = parts[0]
        code_or_prefix = parts[1]
        era = int(parts[2])
        events.append((event_type, code_or_prefix, era))
    
  
    results = process_events(events)
    
    
    for result in results:
        print(result)


if __name__ == "__main__":
    main()