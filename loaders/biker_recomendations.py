from .data_loader import DataLoader
from typing import TypedDict, Annotated
import pandas as pd


class BikersData(TypedDict):
    bikers: Annotated[pd.DataFrame, 'Biker demographic information (training-filtered)']
    tours: Annotated[pd.DataFrame, 'Tour features and word counts (training-filtered)']
    tour_convoy: Annotated[pd.DataFrame, 'Tour participation lists (training-filtered)']
    bikers_network: Annotated[pd.DataFrame, 'Social network connections (training-filtered)']

class BikersTrain(BikersData):
    train: Annotated[pd.DataFrame, 'Training interactions with like/dislike labels']

class Dataset(TypedDict):
    data: Annotated[BikersData, '']

class BikerRecommenderDataLoader(DataLoader):
    """Data loader for biker tour recommendation system with multiple tables."""
    DEFAULT_SCHEMA = Dataset