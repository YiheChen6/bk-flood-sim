# src/raster_thresholding.py
import numpy as np

def threshold_array(arr: np.ndarray, dcrit: float):
    return (arr >= dcrit).astype(int)

def run(flood_depth_path: str, dcrit: float):
    # 占位：生成一个小样本数组来演示
    arr = np.array([[0.1, 0.6],[0.4, 0.8]])
    return threshold_array(arr, dcrit)
