import sys
import os
from jinja2 import Environment, FileSystemLoader

class StixBaseParser:
    """
    Base class for all Stix version parsers.
    """

    def __init__(self, data: dict):
        self.data = data
    
    def print_markdown(self):
        """
        Print the Markdown representation of the parsed data.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    
    def get_template_name(self):
        """
        Get the name of the Markdown template.
        """
        raise NotImplementedError("Template is not defined.")
    
    def template(self):
        """
        Get the Jinja2 template for rendering Markdown.
        This method loads the template from the templates directory
        and returns it for rendering.
        Returns:
            Jinja2 Template: The loaded Jinja2 template.
        Raises:
            FileNotFoundError: If the template file is not found.
        """
        # Load the Jinja2 template
        # from the templates directory
        # The templates directory is expected to be in the MITRE_HOME environment variable
        # or in the same directory as this script.
        # The template name is defined in the get_template_name method
        # and is expected to be a Markdown file.
        template_path = os.path.join(os.environ.get("MITRE_HOME", ""), "templates")
        env = Environment(loader=FileSystemLoader(template_path))
        template = env.get_template(self.get_template_name())
        return template