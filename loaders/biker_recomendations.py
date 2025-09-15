from .data_loader import DataLoader
from typing import TypedDict
import pandas as pd

class BikersData(TypedDict):
    train: pd.DataFrame
    bikers: pd.DataFrame
    tours: pd.DataFrame
    tour_convoy: pd.DataFrame
    bikers_network: pd.DataFrame

class Dataset(TypedDict):
    X_train: BikersData
    y_train: pd.DataFrame
    X_val: BikersData

class BikerRecommenderDataLoader(DataLoader):
    """Data loader for biker tour recommendation system with multiple tables."""
    DEFAULT_SCHEMA = Dataset