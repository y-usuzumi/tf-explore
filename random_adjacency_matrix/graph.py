import math
import numpy
import random


class GenGraphException(Exception):
    pass


def _calc_fill_pos(nodes, idx):
    total_cnt = (nodes/2) * (nodes-1)
    if idx >= total_cnt:
        raise GenGraphException("Index out of node count")
    d2 = math.floor((-1 + math.sqrt(1 + 8 * idx)) / 2)
    return int(idx - (d2+1)/2*d2), d2+1


def _rand_connect(edges, adj_mat, directed=False):
    if adj_mat.ndim != 2 or adj_mat.shape[0] != adj_mat.shape[1]:
        raise GenGraphException("Invalid adj_mat shape")

    nodes = adj_mat.shape[0]
    all_possible_edges_cnt = int(nodes * (nodes-1))
    if not directed:
        undirected_possible_edges_cnt = all_possible_edges_cnt
    else:
        undirected_possible_edges_cnt = all_possible_edges_cnt // 2
    print("Matrix shape: %s" % (adj_mat.shape,))
    print("Asking for %d random edges; Maximum possible edges: %d" % (edges, all_possible_edges_cnt))
    edges = min(all_possible_edges_cnt, edges)
    fill_indices = random.sample(range(all_possible_edges_cnt), edges)
    for connection in fill_indices:
        if directed:
            if connection >= undirected_possible_edges_cnt:
                connection = connection-undirected_possible_edges_cnt
                d2, d1 = _calc_fill_pos(nodes, connection)
            else:
                d1, d2 = _calc_fill_pos(nodes, connection)
            adj_mat[d1][d2] = 1
        else:
            d1, d2 = _calc_fill_pos(nodes, connection)
            adj_mat[d1][d2] = 1
            adj_mat[d2][d1] = 1
    print("Result: \n%s" % adj_mat)
    return adj_mat


def gen_graph(nrange, erange, directed=True):
    nodes = random.randint(nrange[0], nrange[1])
    edges = random.randint(erange[0], erange[1])
    adj_mat = numpy.zeros((nodes, nodes), dtype=numpy.int8)
    _rand_connect(edges, adj_mat, directed=directed)
    return (nodes, adj_mat)
