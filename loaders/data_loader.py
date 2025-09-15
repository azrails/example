from abc import ABC, abstractmethod
from typing import Any
import numpy as np

class DataLoader(ABC):
    """Abstract base class for competition data loading strategies"""
    DEFAULT_SCHEMA = {}

    @classmethod
    def schema_dict(cls, schema_type: type | None = None, expose: bool = False, parent_key: str | None = None) -> dict[str, Any]:
        """Возвращает словарь с типами, рекурсивно разворачивая TypedDict если expose=True.
        Если parent_key содержит 'val', добавляет суффикс '_val' к вложенным полям.
        """
        if schema_type is None:
            schema_type = cls.DEFAULT_SCHEMA

        result = {}
        annotations = getattr(schema_type, "__annotations__", {})
        for k, v in annotations.items():
            key_name = k
            if expose and parent_key and "val" in parent_key.lower():
                key_name = f"{k}_val"

            # Вложенный TypedDict
            if isinstance(v, type) and issubclass(v, dict) and hasattr(v, "__annotations__"):
                nested = cls.schema_dict(v, expose=expose, parent_key=k)
                if expose:
                    for nk, nv in nested.items():
                        result[nk] = nv
                else:
                    result[key_name] = nested
            else:
                module = getattr(v, "__module__", "")
                name = getattr(v, "__name__", str(v))
                if module in ("builtins", ""):
                    type_str = name
                elif module == "pandas.core.frame":
                    type_str = "pd.DataFrame"
                elif module == "numpy":
                    type_str = "np.ndarray"
                else:
                    type_str = f"{module}.{name}"
                result[key_name] = type_str
        return result
