from abc import ABC, abstractmethod
from typing_extensions import get_type_hints, get_args
from typing import Any
import numpy as np

class DataLoader(ABC):
    """Abstract base class for competition data loading strategies"""
    DEFAULT_SCHEMA = {}

    @classmethod
    def schema_dict(cls, schema_type: type | None = None, expose: bool = False, parent_key: str | None = None) -> dict[str, Any]:
        """Возвращает словарь с типами без комментариев"""
        if schema_type is None:
            schema_type = cls.DEFAULT_SCHEMA

        result = {}
        annotations = get_type_hints(schema_type, include_extras=True)

        for k, v in annotations.items():
            # если Annotated
            if get_args(v):
                base_type, *_ = get_args(v)
            else:
                base_type = v

            key_name = k
            if expose and parent_key and "val" in parent_key.lower():
                key_name = f"{k}_val"

            if isinstance(base_type, type) and issubclass(base_type, dict) and hasattr(base_type, "__annotations__"):
                nested = cls.schema_dict(base_type, expose=expose, parent_key=k)
                if expose:
                    result.update(nested)
                else:
                    result[key_name] = nested
            else:
                result[key_name] = cls._normalize_type(base_type)

        return result

    @classmethod
    def schema(cls, schema_type: type | None = None, expose: bool = False, parent_key: str | None = None) -> dict[str, Any]:
        """Возвращает словарь с типами и комментариями отдельно"""
        if schema_type is None:
            schema_type = cls.DEFAULT_SCHEMA

        result = {}
        annotations = get_type_hints(schema_type, include_extras=True)

        for k, v in annotations.items():
            if get_args(v):
                base_type, *meta = get_args(v)
                comment = meta[0] if meta else ""
            else:
                base_type, comment = v, ""

            key_name = k
            if expose and parent_key and "val" in parent_key.lower():
                key_name = f"{k}_val"

            if isinstance(base_type, type) and issubclass(base_type, dict) and hasattr(base_type, "__annotations__"):
                nested = cls.schema(base_type, expose=expose, parent_key=k)
                if expose:
                    result.update(nested)
                else:
                    result[key_name] = nested
            else:
                result[key_name] = {
                    "type": cls._normalize_type(base_type),
                    "comment": comment
                }

        return result

    @staticmethod
    def _normalize_type(tp: type) -> str:
        """Упрощаем строковое представление типов"""
        module = getattr(tp, "__module__", "")
        name = getattr(tp, "__name__", str(tp))
        if module == "pandas.core.frame":
            return "pd.DataFrame"
        elif module == "numpy":
            return "np.ndarray"
        elif module in ("builtins", ""):
            return name
        return f"{module}.{name}"