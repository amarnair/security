import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.join(os.environ.get("MITRE_HOME", ""), "lib"))

from factory.stix_parser_factory import StixParserFactory
from parsers.stix2_1 import Stix2_1

class TestStixParserFactory(unittest.TestCase):
    def setUp(self):
        # Initialize the factory
        self.factory = StixParserFactory()

    def test_get_parser_v2_1(self):
        # Test that the factory returns the correct parser for version "v2.1"
        parser = self.factory.get_parser("2.1")
        self.assertIsInstance(parser, Stix2_1)

    def test_get_parser_default(self):
        # Test that the factory returns the default parser when no version is specified
        with self.assertRaises(ValueError) as context:
            self.factory.get_parser(None)
        self.assertEqual(str(context.exception), "Stix version must be specified.")

    def test_get_parser_invalid_version(self):
        # Test that the factory raises an exception for an unsupported version
        with self.assertRaises(ValueError) as context:
            self.factory.get_parser("invalid_version")
        self.assertEqual(str(context.exception), "Unsupported Stix version: invalid_version")

if __name__ == "__main__":
    unittest.main()