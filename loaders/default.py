from .data_loader import DataLoader
from typing import TypedDict
import numpy as np
import pandas as pd

class Dataset(TypedDict):
    X_train: pd.DataFrame
    y_train: pd.DataFrame
    X_val: pd.DataFrame


class DefaultDataLoader(DataLoader):
    """Default data loader with hardcoded paths"""
    DEFAULT_SCHEMA = Dataset