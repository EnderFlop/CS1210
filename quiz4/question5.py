#def needsEdge(i,j):
#  return i > j

def q4(n):
  node_dict = {}
  nodes = [i+1 for i in range(n)]
  for n in nodes:
    node_dict[n] = []
  #Right now we have {1:[], 2:[], 3:[]}
  #Fill the empty lists with every node that passes the check.
  for key in node_dict.keys():
    for node in nodes:
      if needsEdge(key, node):
        node_dict[key].append(node)
  return node_dict 

#happy thanksgiving!