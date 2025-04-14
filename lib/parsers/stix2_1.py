import requests
import json
from collections import defaultdict
from .base_parser import StixBaseParser

class Stix2_1(StixBaseParser):
    def __init__ (self ):
        url = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            # Read the stream in chunks and decode it as a string
            chunks = []
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    chunks.append(chunk.decode("utf-8"))
            raw_data = "".join(chunks)
            self.data = json.loads(raw_data)  # parse entire content once it's streamed in
            # Predefine containers
            self.tactic_map = {}
            self.technique_map = defaultdict(list)     # {tactic_shortname: [techniques]}
            self.subtechnique_map = defaultdict(list)  # {technique_id: [sub-techniques]}
            self.extract_pending = True

    def get_template_name(self):
        """
        Get the name of the Markdown template.
        """
        return "stix2.1.md"
    

    def extract_data(self):
        """
        Extracts the data from 
        """
        self.extract_pending = False 
        # Extract data
        for obj in self.data["objects"]:
            obj_type = obj.get("type")

            # Tactics
            if obj_type == "x-mitre-tactic":
                shortname = obj.get("x_mitre_shortname")
                self.tactic_map[shortname] = {
                    "id": obj.get("id"),
                    "name": obj.get("name"),
                    "description": obj.get("description", ""),
                }

            # Techniques and sub-techniques
            elif obj_type == "attack-pattern":
                ext_refs = obj.get("external_references", [])
                mitre_ref = next((ref for ref in ext_refs if ref.get("source_name") == "mitre-attack"), {})
                ext_id = mitre_ref.get("external_id")
                if not ext_id:
                    continue

                item = {
                    "id": obj.get("id"),
                    "external_id": ext_id,
                    "name": obj.get("name"),
                    "description": obj.get("description", ""),
                }

                if obj.get("x_mitre_is_subtechnique", False):
                    # Extract parent technique from external_id (e.g., T1059.001 → T1059)
                    parent_id = ext_id.split(".")[0]
                    self.subtechnique_map[parent_id].append(item)
                else:
                    for phase in obj.get("kill_chain_phases", []):
                        if phase.get("kill_chain_name") == "mitre-attack":
                            tactic = phase["phase_name"]
                            self.technique_map[tactic].append(item)

    
    def print_markdown(self):
        """
        Print the MITRE ATT&CK Kill Chain Hierarchy in Markdown format.
        """
        # Extract data if not already extracted
        # TODO This data can be potentially cached and the mardown can be generated for a specific tactic
        if self.extract_pending:
            self.extract_data()
        # Generate Markdown
        mark_down = self.template().render(tactics=self.tactic_map, techniques=self.technique_map, subtechniques=self.subtechnique_map)
        print(mark_down)

