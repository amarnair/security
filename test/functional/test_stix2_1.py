import unittest
from unittest.mock import MagicMock
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.join(os.environ.get("MITRE_HOME", ""), "lib"))
from parsers.stix2_1 import Stix2_1

class TestStix2_1Parser(unittest.TestCase):
    def setUp(self):
        # Initialize the parser
        self.parser = Stix2_1()

        # Mock the template method to avoid dependency on actual templates
        self.parser.template = MagicMock()
        self.parser.template().render = MagicMock(return_value="Mocked Markdown Output")

        # Mock data for tactics, techniques, and subtechniques
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

    def test_print_markdown(self):
        # Call the method
        self.parser.print_markdown()

        # Assert that the template's render method was called with the correct arguments
        self.parser.template().render.assert_called_once_with(
            tactics=self.parser.tactic_map,
            techniques=self.parser.technique_map,
            subtechniques=self.parser.subtechnique_map,
        )

        # Assert that the output is as expected
        self.assertEqual(self.parser.template().render.return_value, "Mocked Markdown Output")

if __name__ == "__main__":
    unittest.main()