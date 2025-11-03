import numpy as np

def threshold_array(arr: np.ndarray, dcrit: float) -> np.ndarray:
    """数组阈值化：>= dcrit -> 1，否则 0"""
    return (arr >= dcrit).astype(int)

def run(flood_depth_path: str, dcrit: float) -> np.ndarray:
    """
    演示版：不读取 TIF，直接用固定小数组。
    后续替换为 rasterio.open(...).read(1) 的真实实现即可。
    """
    arr = np.array([[0.1, 0.6], [0.4, 0.8]], dtype=float)
    return threshold_array(arr, dcrit)
