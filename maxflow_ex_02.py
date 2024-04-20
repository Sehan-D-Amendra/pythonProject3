import networkx as nx

G = nx.DiGraph()

G.add_edge("1","2", capacity = 1)
G.add_edge("1","3", capacity = 4)
G.add_edge("2","3", capacity = 2)
G.add_edge("2","4", capacity = 3)
G.add_edge("3","4", capacity = 2)

flow_value, flow_dict = nx.maximum_flow(G, "1","4")

print("Maximum Flow :", flow_value)

for key_i, inner_dict in flow_dict.items():
    for key_j, inner_val in inner_dict.items():
        print(f' {key_i} -> {key_j} \t Flow : {inner_val}')


#using the maximum flow minimum cut theorem

cut_value, partition = nx. minimum_cut(G, "1","4")

print("Capacity of minimum cut :" , cut_value)
print("Partitions: ", partition)

reachabel, non_reachabel = partition

#forward cut
forwardcut = set()
for u, nbrs in((n, G[n]) for n in reachabel) : forwardcut.update((u,v) for v in nbrs if v in non_reachabel)
print("Forward cut set: ", sorted(forwardcut))


#revers cut
reverscut = set()
for u, nbrs in((n, G[n]) for n in non_reachabel) : reverscut.update((u,v) for v in nbrs if v in reachabel)


print("Revers cut set: ", sorted(reverscut))


