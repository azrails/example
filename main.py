from loaders import LOADERS
import json

default_schema = LOADERS.get("default").schema_dict()
print(json.dumps(default_schema, indent=2))
print("\n\n")
biker_schema = LOADERS.get("biker").schema_dict(expose=True)
print(json.dumps(biker_schema, indent=2))