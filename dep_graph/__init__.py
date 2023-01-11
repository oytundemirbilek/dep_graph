import argparse
from dep_graph.dep_graph import DependencyHandler


def main():
    parser = argparse.ArgumentParser(
        description="dep_graph prints out the dependency graph of a package."
    )
    parser.add_argument("-f", "--filepath", help="File path to a dependency json file.")
    args = parser.parse_args()
    handler = DependencyHandler(args.filepath)
    handler.load_dependencies()
    handler.print_dependencies()
