topology = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}

path_data = {("A", "B"): {"size": 100, "used": 30}, ("A", "C"): {"size": 100, "used": 50}, ("B", "D"): {"size": 100, "used": 20}, ("C", "D"): {"size": 100, "used": 70}}

flows = {("A", "D"): [("flow1", ["A", "B", "D"]), ("flow2", ["A", "C", "D"])]}

def shortest_path(source, destination):
    if source == destination:
        return [source]

    distances = {node: float('inf') for node in topology}
    distances[source] = 0
    previous = {node: None for node in topology}
    visited = set()

    while len(visited) < len(topology):
        current = None
        current_distance = float('inf')
        for node in topology:
            if node not in visited and distances[node] < current_distance:
                current = node
                current_distance = distances[node]

        if current is None or current == destination:
            break

        visited.add(current)

        for connected_node in topology[current]:
            if connected_node not in visited:
                new_distance = distances[current] + 1
                if new_distance < distances[connected_node]:
                    distances[connected_node] = new_distance
                    previous[connected_node] = current

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path if path[0] == source else None

print("Network Topology")
for node, connected_nodes in topology.items():
    print(f"{node} -> {', '.join(connected_nodes)}")

print("Active Paths")
for (source, destination), list in flows.items():
    print(f"Source: {source}, Destination: {destination}")
    for id, path in list:
        print(f"Path ID: {id}, Path: {' -> '.join(path)}")

print("Shortest Path")
for (source, destination), list in flows.items():
    shortest_path = shortest_path(source, destination)
    if shortest_path:
        print(f"Shortest path from {source} to {destination}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path found from {source} to {destination}.")