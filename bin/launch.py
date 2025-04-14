import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.join(os.environ.get("MITRE_HOME", ""), "lib"))

from factory.stix_parser_factory import StixParserFactory

class LaunchScript:
    """
    Launch script for generating Markdown output from STIX data.
    This script serves as the entry point for the application.
    It initializes the parser factory and retrieves the appropriate
    parser based on the specified version.
    The script then generates the Markdown output using the parser.
    """
    def __init__(self):
        """
        Initialize the launch script.
        """
        self.parser_factory = StixParserFactory()

    def run(self, parser_version=None):
        """
        Run the launch script.
        Args:
            parser_version (str): The version of the parser to use.
        """
        # Get the appropriate parser instance
        self.parser = self.parser_factory.get_parser(parser_version)
        # Generate Markdown output
        self.parser.print_markdown()

if __name__ == "__main__":
    # Create an instance of the launch script
    launch_script = LaunchScript()
    
    # Run the script with the specified parser version
    launch_script.run(parser_version="2.1")
