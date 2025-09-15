from .default import DefaultDataLoader
from .biker_recomendations import BikerRecommenderDataLoader

LOADERS = {
    "default": DefaultDataLoader,
    "biker": BikerRecommenderDataLoader
}