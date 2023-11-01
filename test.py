import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Get user input for web pages and links
while True:
    page = input("Enter a web page (or press Enter to finish): ")
    if not page:
        break
    G.add_node(page)
    links = input(f"Enter links from {page} (comma-separated, or press Enter for no links): ")
    if links:
        links = links.split(',')
        for link in links:
            G.add_edge(page, link.strip())

# Compute PageRank
pagerank = nx.pagerank(G, alpha=0.85)

# Print the PageRank values
for page, rank in pagerank.items():
    print(f"{page}: {rank}")
