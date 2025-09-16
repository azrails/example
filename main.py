from loaders import LOADERS
import json

biker_schema = LOADERS.get("biker").schema_dict()
print(json.dumps(biker_schema, indent=2))

biker_comments = LOADERS.get("biker").schema()
print(json.dumps(biker_comments, indent=2))