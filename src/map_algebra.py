import numpy as np

def run(mask: np.ndarray, population_path: str):
    """
    演示版：生成与 mask 同形状的“人口热力”，并统计受影响像元数量。
    真实实现中，应读取 population.tif 并与 mask 做逐像元相乘/求和。
    """
    H, W = mask.shape
    # 生成一个简单的人口热力（随便构造个梯度）
    y = np.linspace(0, 1, H).reshape(H, 1)
    x = np.linspace(0, 1, W).reshape(1, W)
    pop = (x + y)  # 0..2 的浮点
    affected = pop * (mask > 0)
    stats = {
        "affected_cells": int((mask > 0).sum()),
        "heat_sum": float(affected.sum()),
    }
    return stats, affected
