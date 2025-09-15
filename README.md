#Пример вызовов:


Базовый вариант
```python
from loaders import LOADERS
import json

biker_schema = LOADERS.get("biker").schema_dict()
print(json.dumps(biker_schema, indent=2))

{
  "X_train": {
    "train": "pd.DataFrame",
    "bikers": "pd.DataFrame",
    "tours": "pd.DataFrame",
    "tour_convoy": "pd.DataFrame",
    "bikers_network": "pd.DataFrame"
  },
  "y_train": "pd.DataFrame",
  "X_val": {
    "train": "pd.DataFrame",
    "bikers": "pd.DataFrame",
    "tours": "pd.DataFrame",
    "tour_convoy": "pd.DataFrame",
    "bikers_network": "pd.DataFrame"
  }
}
```


Расширеный вариант:

```python
from loaders import LOADERS
import json

biker_schema = LOADERS.get("biker").schema_dict(expose=True)
print(json.dumps(biker_schema, indent=2))

{
  "train": "pd.DataFrame",
  "bikers": "pd.DataFrame",
  "tours": "pd.DataFrame",
  "tour_convoy": "pd.DataFrame",
  "bikers_network": "pd.DataFrame",
  "y_train": "pd.DataFrame",
  "train_val": "pd.DataFrame",
  "bikers_val": "pd.DataFrame",
  "tours_val": "pd.DataFrame",
  "tour_convoy_val": "pd.DataFrame",
  "bikers_network_val": "pd.DataFrame"
}
```