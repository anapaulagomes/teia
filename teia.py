import csv
import networkx as nx


G = nx.MultiGraph()

with open('/home/ana/Downloads/Investigação - Relações.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    header = next(reader)
    for row in reader:
        attributes = {}
        for position in range(2, len(row)):
            attributes[header[position]] = row[position]

        edge_key = f'{row[0]} - {row[1]}'
        G.add_edge(row[0], row[1], key=edge_key, **attributes)

nx.write_gml(G, 'Investigação - Relações.gml')
