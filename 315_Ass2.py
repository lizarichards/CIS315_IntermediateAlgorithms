
import sys

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edges(self, v1, v2, weight):
        self.graph.append([v1, v2, weight])

    def print_array(self, dist):
        for i in range(self.V):
            print(i, dist[i])


def init_single_source(g, source):
    dist = {}
    prev = {}
    for vertex in g:
        dist[vertex] = float("-Inf")
        prev[vertex] = None
    dist[source] = 0
    return dist, prev


def relax(g, vertex, neighbour, dist, prev):
    if dist[neighbour] > dist[vertex] + g[vertex][neighbour]:
        dist[neighbour] = dist[vertex] + g[vertex][neighbour]
        prev[neighbour] = vertex


def bellman_ford(g, source):
    distance, previous = init_single_source(g, source)
    for i in range(len(g) - 1):
        for v in g:
            for neighbour in g[v]:
                relax(v, neighbour, g, distance, previous)

    for v in g:
        for neighbour in g[v]:
            if distance[neighbour] > distance[v] + g[v][neighbour]:
                return False
    return True


def main():
    #open the file? how do I obtain that file in the shell? How do I use stdin?
    first = sys.stdin.readline()
    nums = first.split(" ")
    num_vertices = int(nums[0])
    num_edges = int(nums[1])

    num_lines = 0
    g = Graph(num_vertices)
    while num_lines < num_edges:
        line = sys.stdin.readline()
        line_list = line.split(" ")
        v1 = int(line_list[0])
        v2 = int(line_list[1])
        weight = int(line_list[2])
        g = g.add_edges(v1, v2, weight)
        num_lines += 1

    print("longest path: " + str(bellman_ford(g, 0)))
    print("number of longest paths: " + str())

'''
# how do I actually import the files to use
with open(input_file, "r") as file:
    first = file.readline()
    nums = first.split(" ")

'''
