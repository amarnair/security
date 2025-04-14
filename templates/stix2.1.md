# MITRE ATT&CK Kill Chain Hierarchy


{% for tactic_key, tactic in tactics.items() %}
## {{ tactic.id }} {{ tactic_key }}


{{ tactic.description }}


{% for technique in techniques.get(tactic_key, []) %}
### {{ technique.id }} {{ technique.name }}


Technique external id {{ technique.external_id }}
{{ technique.description }}


{% for sub in subtechniques.get(technique.external_id, []) %}
#### {{ sub.id }} {{ sub.name }}


Sub technique external id {{ sub.external_id }}
{{ sub.description }}


{% endfor %}
{% endfor %}
{% endfor %}
