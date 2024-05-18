import osmnx as ox
import networkx as nx

# Path to your OSM file
osm_file = "/map.osm"


graph = ox.graph_from_xml(osm_file)

import matplotlib.pyplot as plt
ox.plot_graph(graph)
plt.show()


print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

node_lat = 36.7487091
node_lon = 5.06812744

node_lat2 = 36.7476306
node_lon2 = 5.0685588

ox.plot_graph(graph, bgcolor='w', node_color='b', edge_color='k', node_alpha=0.5, edge_linewidth=0.5, figsize=(10, 10))


plt.plot(node_lon, node_lat, 'go', markersize=10)
plt.plot(node_lon2, node_lat2, 'go', markersize=10)



# Plot the graph with all nodes in blue and display node labels
fig, ax = ox.plot_graph(graph, bgcolor='w', node_color='r', edge_color='k', node_alpha=0.8, edge_linewidth=0.8, figsize=(25, 20), show=False, close=False)

# Add latitude and longitude labels to each node
for node, data in graph.nodes(data=True):
    ax.text(data['x'], data['y'], f"({data['y']:.6f}, {data['x']:.6f})", fontsize=8, color='blue', ha='center', va='center')

# Show the plot
plt.show()


start_node = ox.distance.nearest_nodes(graph, node_lon, node_lat)

# Coordinates of the end node
end_node = ox.distance.nearest_nodes(graph, node_lon2, node_lat2)

# Find the shortest path using astra's algorithm
shortest_path = nx.astar_path(graph, start_node, end_node, weight='length')

# Plot the graph with all nodes in blue
ox.plot_graph(graph, bgcolor='w', node_color='b', edge_color='k', node_alpha=0.5, edge_linewidth=0.5, figsize=(10, 10))

# Highlight the shortest path with a different color
ox.plot_graph_route(graph, shortest_path, route_color='r', route_linewidth=2)
