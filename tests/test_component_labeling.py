import numpy as np
from src import component_labeling

def test_component_labeling_basic():
    mask = np.array([
        [1, 0, 1],
        [1, 1, 0],
        [0, 0, 1],
    ])
    labels, n = component_labeling.run(mask, neighbor_rule=4)
    assert n >= 2
    assert labels.shape == mask.shape
