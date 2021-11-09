from basicgraph import *

# CS1210 Fall 2021. Discussion section 9 assignment.
#
# The last function in the file - testWordGraph - will do a basic test of your
# buildWordGraph function.  It's not at all a thorough test but is a start.
#
# Complete steps 1, 2.1, 2.2, and 2.3 so that
# buildWordGraph(somefilename) will return a graph with words from somefilename as Nodes
# and an edge between each pair of Nodes that represents two words that differ in exactly
# one position.
#
# Test on a small file first - wordsTest.txt
# You should draw the graph for wordsTest.txt on paper by hand, and then look at the result
# of buildWordGraph("wordsTest.txt") to see if they match
#
# Test also on large file - words5.txt.
# The file contains 2415 words. It should take several seconds to build this
# graph (but not several minutes)
#


# return True if there should be an edge between nodes for word1 and word2
# in the word graph. That is, if the two words are the same length and differ
# at exactly one position.  Return False otherwise (including when the two words
# don't differ at all!)
#
def shouldHaveEdge(word1, word2):
    if len(word1) != len(word2):
        return False
    num_differences = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            num_differences += 1
    if num_differences == 1:
        return True
    return False


# Give a file of words, return a graph with
# - one node for each word
# - an edge for every pair of words, w1 and w2,
#      where shouldHaveEdge(w1, w2) is True.
#
def buildWordGraph(wordsFile):
    wordGraph = Graph()
    instream = open(wordsFile,"r")
    for line in instream:
        word_node = Node(line.strip())
        wordGraph.addNode(word_node)
    nodes_list = wordGraph.nodes
    for node1 in nodes_list:
        for node2 in nodes_list:
            if node1 != node2 and not wordGraph.hasEdge(node1, node2) and shouldHaveEdge(node1.getName(), node2.getName()):
                wordGraph.addEdge(node1, node2)
    return wordGraph

def testWordGraph():
    print("*** testing buildWordGraph('wordsTest.txt') ***")
    g = buildWordGraph('wordsTest.txt')
    numNodes = len(g.nodes)
    numEdges = sum(len(v) for v in g.adjacencyLists.values()) / 2
    print("returned graph has {} nodes and {} edges".format(numNodes, numEdges))
    if (numNodes != 8):
        print("Number of nodes is incorrect. Should be 8.")
    else:
        print("Number of nodes is correct.")
    if (numEdges != 11):
        print("Number of edges is incorrect. Should be 11.")
    else:
        print("Number of edges is correct.")
        
    print("*** testing buildWordGraph('words5.txt') ***")         
    g = buildWordGraph('words5.txt')
    numNodes = len(g.nodes)
    numEdges = sum(len(v) for v in g.adjacencyLists.values()) / 2
    print("returned graph has {} nodes and {} edges".format(numNodes, numEdges))
    if (numNodes != 2415):
        print("Number of nodes is incorrect. Should be 2415.")
    else:
        print("Number of nodes is correct.")
    if (numEdges != 2740):
        print("Number of edges is incorrect. Should be 2740.")
    else:
        print("Number of edges is correct.")

#testWordGraph()