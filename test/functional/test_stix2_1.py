import unittest
import sys
import os
sys.path.append(os.path.join(os.environ.get("MITRE_HOME", ""), "lib"))
from parsers.stix2_1 import Stix2_1

class TestStix2_1ParserFunctional(unittest.TestCase):
    def setUp(self):
        # Initialize the parser
        self.parser = Stix2_1()

        # Set up real data for tactics, techniques, and subtechniques
        self.parser.tactic_map = {
            "tactic1": {"name": "Tactic 1", "id": "TA0001"},
            "tactic2": {"name": "Tactic 2", "id": "TA0002"},
        }
        self.parser.technique_map = {
            "tactic1": [{"name": "Technique 1", "id": "T1001"}],
            "tactic2": [{"name": "Technique 2", "id": "T1002"}],
        }
        self.parser.subtechnique_map = {
            "T1001": [{"name": "Subtechnique 1.1", "id": "T1001.001"}],
        }

        # Set extract_pending to False to skip data extraction
        self.parser.extract_pending = False

        # Set up the template directory and template name
        self.template_dir = os.path.join(os.environ.get("MITRE_HOME", ""), "templates")
        self.template_name = "stix2.1.md"

    def test_print_markdown_with_real_template(self):
        # Ensure the template exists
        template_path = os.path.join(self.template_dir, self.template_name)
        self.assertTrue(os.path.exists(template_path), f"Template not found: {template_path}")

        # Set the template method to use the real template
        from jinja2 import Environment, FileSystemLoader
        env = Environment(loader=FileSystemLoader(self.template_dir))
        self.parser.template = lambda: env.get_template(self.template_name)

        # Call the method to generate Markdown
        try:
            self.parser.print_markdown()
        except Exception as e:
            self.fail(f"print_markdown raised an exception: {e}")

    def test_empty_data(self):
        # Test behavior when all maps are empty
        self.parser.tactic_map = {}
        self.parser.technique_map = {}
        self.parser.subtechnique_map = {}

        # Call the method to generate Markdown
        try:
            self.parser.print_markdown()
        except Exception as e:
            self.fail(f"print_markdown raised an exception with empty data: {e}")

if __name__ == "__main__":
    unittest.main()