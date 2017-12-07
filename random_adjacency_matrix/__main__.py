import argparse
from . import gen_graph


def _comma_split(type_):
    def _converter(s):
        vals = s.split(',')
        try:
            return [type_(v) for v in vals]
        except ValueError as ex:
            raise argparse.ArgumentTypeError(str(ex))

    return _converter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Gen", description="Generate sample data")
    parser.add_argument(
        "-n", "--nodes-range",
        required=True,
        type=_comma_split(int),
        dest="nodes_range",
        help="Number of vertices(nodes) in the form of 'min,max'"
    )
    parser.add_argument(
        "-e", "--edges-range",
        required=True,
        type=_comma_split(int),
        dest="edges_range",
        help="Number of edges in the form of 'min,max'"
    )
    parser.add_argument(
        "-d", "--directed",
        dest="directed",
        action="store_true",
        help="Controls whether the graph is directed or not"
    )
    args = parser.parse_args()
    nodes_range = args.nodes_range if len(args.nodes_range) > 1 else (args.nodes_range[0], args.nodes_range[0])
    edges_range = args.edges_range if len(args.edges_range) > 1 else (args.edges_range[0], args.edges_range[0])
    g = gen_graph(nodes_range, edges_range, directed=args.directed)
