import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Function to load the graph from an OSM file
def load_graph(osm_file):
    return ox.graph_from_xml(osm_file)

# Function to plot the graph
def plot_graph(graph, node_color='b', edge_color='k', node_alpha=0.5, edge_linewidth=0.5, figsize=(10, 10)):
    fig, ax = ox.plot_graph(graph, bgcolor='w', node_color=node_color, edge_color=edge_color, 
                            node_alpha=node_alpha, edge_linewidth=edge_linewidth, figsize=figsize)
    plt.show()
    return fig, ax

# Function to plot points of interest on the graph
def plot_points(ax, points, color='go', markersize=10):
    for lon, lat in points:
        ax.plot(lon, lat, color, markersize=markersize)
    plt.show()

# Function to add latitude and longitude labels to each node
def add_node_labels(graph, ax):
    for node, data in graph.nodes(data=True):
        ax.text(data['x'], data['y'], f"({data['y']:.6f}, {data['x']:.6f})", fontsize=8, color='blue', ha='center', va='center')
    plt.show()

# Function to find the nearest node given a point
def find_nearest_node(graph, lon, lat):
    return ox.distance.nearest_nodes(graph, lon, lat)

# Function to calculate the shortest path using A* algorithm
def calculate_shortest_path(graph, start_node, end_node, weight='length'):
    return nx.astar_path(graph, start_node, end_node, weight=weight)

# Function to highlight the shortest path on the graph
def plot_shortest_path(graph, shortest_path):
    ox.plot_graph_route(graph, shortest_path, route_color='r', route_linewidth=2)
    plt.show()

# Main function to execute the workflow
def main():
    osm_file = "/map.osm"
    
    # Load and plot the graph
    graph = load_graph(osm_file)
    plot_graph(graph)
    
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    
    # Prompt user to enter coordinates for start and end points
    node_lat1 = float(input("Enter the latitude for the start point: "))
    node_lon1 = float(input("Enter the longitude for the start point: "))
    node_lat2 = float(input("Enter the latitude for the end point: "))
    node_lon2 = float(input("Enter the longitude for the end point: "))

    # Plot graph with points of interest
    fig, ax = plot_graph(graph, node_color='r', edge_color='k', node_alpha=0.8, edge_linewidth=0.8, figsize=(25, 20))
    plot_points(ax, [(node_lon1, node_lat1), (node_lon2, node_lat2)])
    
    # Add node labels
    add_node_labels(graph, ax)

    # Find nearest nodes for the start and end points
    start_node = find_nearest_node(graph, node_lon1, node_lat1)
    end_node = find_nearest_node(graph, node_lon2, node_lat2)
    
    # Calculate the shortest path
    shortest_path = calculate_shortest_path(graph, start_node, end_node)
    
    # Plot the graph and highlight the shortest path
    plot_graph(graph)
    plot_shortest_path(graph, shortest_path)

if __name__ == "__main__":
    main()