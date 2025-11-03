import numpy as np
from src import raster_thresholding

def test_thresholding():
    arr = np.array([[0.1, 0.6], [0.4, 0.8]])
    mask = raster_thresholding.threshold_array(arr, dcrit=0.5)
    assert mask.tolist() == [[0, 1], [0, 1]]
