import numpy as np
from src import map_algebra

def test_map_algebra_runs():
    mask = np.array([[0,1],[1,1]])
    stats, heat = map_algebra.run(mask, "data/population.tif")
    assert "affected_cells" in stats
    assert heat.shape == mask.shape
