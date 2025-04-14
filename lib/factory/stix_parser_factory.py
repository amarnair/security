import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.join(os.environ.get("MITRE_HOME", ""), "lib"))
from parsers.stix2_1 import Stix2_1
class StixParserFactory():
    """
    Factory class for creating STIX parsers.
    This class is responsible for creating instances of the appropriate
    parser based on the specified version.
    Currently, it supports the following versions:
    - 2.1: STIX 2.1 parser
    """
    def __init__(self):
        """
        Initialize the factory.
        """
        pass

    def get_parser(self, stix_version=None):
        """
        Get the appropriate parser based on the specified version.
        This method creates an instance of the specified parser and
        returns it.
        Args:
            stix_version (str): The version of the parser to use.
                Supported versions: "2.1".
        Returns:
            object: An instance of the specified parser.
        Raises:
            ValueError: If the specified parser version is not supported.
        """

        if stix_version is None:
            raise ValueError("Stix version must be specified.")
        elif stix_version == "2.1":
            print("Using parser v16")
            return Stix2_1()
        else:
            raise ValueError(f"Unsupported Stix version: {stix_version}")


        