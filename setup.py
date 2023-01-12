from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="dep_graph",
        description="dep_graph - printing the dependency graphs",
        author="Oytun Demirbilek",
        author_email="oytun1996@gmail.com",
        version="0.0.1",
        packages=find_packages(exclude=("tests")),
    )
