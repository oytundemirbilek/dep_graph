from dep_graph.dep_graph import DependencyHandler


def main():
    handler = DependencyHandler()
    handler.load_dependencies()
    handler.print_dependencies()
