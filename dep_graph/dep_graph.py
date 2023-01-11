import json
import logging
from typing import Dict


class DependencyHandler:
    def __init__(self, dep_filepath: str):
        """
        Constructor for the DependencyHandler class requires a file path to a json file.

        Parameters
        ----------
        dep_filepath: str
            File path to the dependency json file.

        """
        self.dep_filepath = dep_filepath
        self.dependency_dict: Dict[str, list] = {}
        # Tree level is only used for string formatting when printing.
        self.tree_level = 0

    def _print_single_package_dependencies(self, package_name: str) -> None:
        """
        Formats and prints the provided dependency data.
        """
        self.tree_level += 1
        for dependency in self.dependency_dict[package_name]:
            print(self.tree_level * 2 * " " + f"- {dependency}")
            self._print_single_package_dependencies(dependency)
        self.tree_level -= 1

    def print_dependencies(self) -> None:
        """
        Formats and prints the provided dependency data.
        """
        package_list = self.dependency_dict.keys()
        for package_name in package_list:
            print(f"- {package_name}")
            self._print_single_package_dependencies(package_name)

    def load_dependencies(self) -> Dict[str, list]:
        """
        Function to load dependency data from the json file.

        Returns
        ----------
        dictionary
            A dictionary where each key is a package name and its value is a list of dependency names.
        """
        try:
            with open(self.dep_filepath) as dep_file:
                dependency_dict = json.load(dep_file)
            self.dependency_dict = dependency_dict
        except Exception as e:
            logging.warning("Dependency list could not be loaded.")
            logging.warning(e)

        return self.dependency_dict
