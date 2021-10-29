class Graph:
    def __init__(self,data,edges,instruction=""):
        self.data = data
        self.edges = edges
        self.instruction = instruction

def construct_graph(instruction_set):
    graph_map = {}
    for i in instruction_set:
        words = i.split(" ")
        source_regs = words[1].split(",")
        key = words[3]
        try:
            node = graph_map[key]
        except KeyError:
            node = Graph(key,[])
            graph_map[key] = node
            node.instruction = i

        for v in source_regs:
                if v in graph_map.keys():
                    # append that node to the edges of existing node
                    node.edges.append(graph_map[v])
                else:
                    new_node = Graph(v,[])
                    node.edges.append(new_node)
                    graph_map[v] = new_node
            
    return graph_map
        
def traverse_graph(instruction_set,item):
    stack = []
    graph_map = construct_graph(instruction_set)
    node = graph_map[item]
    if node.instruction:
        stack.append(node.instruction)
    for edge in node.edges:
        if edge.instruction:
            if edge.instruction not in stack:
                stack.append(edge.instruction)
    for i in range(len(stack)):
        print(stack.pop())



# Test Case 1
# instruction_set = [
#     "add r0,r1 => r2",
#     "add r1,r2 => r3",
#     "add r0,r0 => r4"
# ]

# registry = ["r3"]

# Test Case 2
instruction_set = [
    "add r0,r1 => r2",
    "add r1,r2 => r3",
    "add r0,r0 => r4",
    "add r3,r4 => r1"
]

registry = ["r0"]

for r in registry:
    traverse_graph(instruction_set,r)






