from basicgraph import *
from bfs import *

# return True if there should be an edge between nodes for word1 and word2
# in the word graph. Return False otherwise
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

# ASSUMPTION: (modified) breadth first search has already been executed.
#
# Thus, parent values have been set in all nodes reached by bfs.
# Now, work backwards from endNode (end word) to build a list of words
# representing a ladder between the start word and end word.
#
# For example, if the start word was "cat" and the end word was "dog", after bfs
# we might find that "dog"'s parent was "dot" and then that "dot"'s parent was
# "cot" and finally that "cot"'s parent was "cat" (which has no parent).  Thus,
# a ladder from "cat" to "dog" is ["cat", "cot", "dot", "dog"]
#
# Return [] if the endNode has no parent.  If the end node has no parent, the
# the breadth first search could not reach it from the start node. Thus, there
# is no word ladder between the start and end words.
#
def extractWordLadder(endNode):
    ladder = []
    if endNode == None or endNode.getStatus() == "unseen":
      return []
    current_node = endNode
    ladder.append(current_node)
    while current_node.getParent() != None:
        ladder.append(current_node.getParent())
        current_node = current_node.getParent()
    return ladder 

#wordGraph = buildWordGraph("test2.txt")
#bfs(wordGraph, wordGraph.getNode("cat"))
#print(extractWordLadder(wordGraph.getNode("dog")))


def wordLadders(wordsFile):
    global wordGraph # this is useful for debugging - you can "look" at wordGraph
                     # in the Python shell to determine if it's correct
                     
    # 1. read the words file and build a graph based on the words file
    wordGraph = buildWordGraph(wordsFile)
    print("Created word graph with {} nodes and {} edges".format(
        len(wordGraph.nodes),
        sum(len(adjList) for adjList in wordGraph.adjacencyLists.values())//2))

    # 2. user interaction loop:
    #    - check that the give word or words are in the dictionary
    #    - execute breadth first search from the start word's node
    #      (Note: you need to slightly modify the original bfs in bfs.py
    #      to set and update distance and parent properties of Nodes.  This also
    #      requires modification of the Node class in basicgraph.py to add
    #      those properties.)
    #    - if an end word was given, extract word ladder from
    #      start to that endword
    #    - if an end word was not given, find the node in the graph
    #      with the largest distance value and extract the ladder between
    #      the start node and that node.
    #    - print appropriate information - the extracted ladder and its length
    #
    # 

    userInput = input("Enter start and end words OR start word OR 'q' to quit: ")
    words = userInput.split()
    while (words[0] != 'q'):
        
        # make sure word or words are in the wordsFile (and thus now in graph)
        startNode = wordGraph.getNode(words[0])
        if (startNode is None):
            print("The start word is not in the dictionary.  Please try again.")
        elif (len(words) == 2) and (wordGraph.getNode(words[1]) is None):
            print("The end word is not in the dictionary.  Please try again.")
        elif (len(words) == 2) and (words[0] == words[1]):
            print("The start and end words must be different. Please try again.")
        else:

            # Execute bread-first search from the startNode.  This
            # should set distance properties of all words reachable from start
            # word, and also set "parent" properties appropriately.
            bfs(wordGraph, startNode)
            # If only one word was given, look through all nodes in the graph
            # to find one with max distance property. That word is the one with
            # the maximal "shortest distance" from start word.
            if (len(words) == 1):
                maxDistance = -1
                for node in wordGraph.nodes:
                    dist = node.getDistance()
                    if dist is not None and dist >= maxDistance:
                       endNode = node                   
                       maxDistance = node.getDistance()
                print("{} is maximally distant ({} steps) from {}:".format(endNode.getName(), maxDistance, words[0]))

            # If two words were given, execute extractWordLadder from node for
            # second word, yielding a list of words representing the shortest
            # path between start and end words. 
            else:
                endNode = wordGraph.getNode(words[1])
                if endNode.getParent() == None:
                    print("There is no word ladder from ", startNode.getName(), " to ", endNode.getName())
                else:
                    print("Shortest ladder from {} to {} is length {}:".format(words[0], words[1], endNode.distance))                                 
            ladder = extractWordLadder(endNode) 
            for word in ladder:
                print(word, end=" ")
            print()

        # Finally, ask for new start/end or start words or 'q'
        userInput = input("Enter start and end words OR start word OR 'q' to quit: ")
        words = userInput.split()
                                   
wordLadders("test2.txt")