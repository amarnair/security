# MITRE ATT&CK Markdown Generator

This project downloads the MITRE ATT&CK Enterprise framework (STIX 2.1 format) and generates a Markdown hierarchy of Tactics, Techniques, and Sub-techniques using Jinja2 templates.

## 🛠 Requirements

- Python 3.7+
- `requests`
- `Jinja2`

## 📦 Setup


pip install -r requirements.txt

## 🔧 Environment Configuration
Before running the program, ensure the MITRE_HOME environment variable is set. This variable should point to the root directory of the project. For example:


export MITRE_HOME=<project_folder>/security

## 🏗️ Architecture
The implementation is structured as follows:

Launch Script (bin/launch.py):

Entry point for the application.
Initializes the parser factory and retrieves the appropriate parser based on the specified version.
Generates Markdown output using the selected parser.
Parser Factory (factory/stix_parser_factory.py):

Responsible for returning the appropriate parser instance based on the requested version (e.g., v2.1).
Supports extensibility for future parser versions.
Parsers (parsers/):

Contains specific parser implementations for different versions of the MITRE ATT&CK framework.
Example: Stix2_1 parses the STIX 2.1 format and extracts Tactics, Techniques, and Sub-techniques.
Templates (templates):

Jinja2 templates used to generate Markdown output.
Example: mitre-v16.md defines the structure of the Markdown output.
Data Extraction:

Each parser extracts data from the MITRE ATT&CK framework (e.g., Tactics, Techniques, Sub-techniques).
Data is stored in maps (tactic_map, technique_map, subtechnique_map) for rendering.
Markdown Generation:

The extracted data is passed to a Jinja2 template for rendering.
The print_markdown method in each parser handles the rendering process.

## 🚀 How to Launch
To run the program, use the following command:
PYTHONPATH=$MITRE_HOME/lib $MITRE_HOME/.venv/bin/python $MITRE_HOME/bin/launch.py

Example
export MITRE_HOME=/Users/projects/security
PYTHONPATH=$MITRE_HOME/lib $MITRE_HOME/.venv/bin/python $MITRE_HOME/bin/launch.py

This will generate the Markdown output based on the MITRE ATT&CK framework.