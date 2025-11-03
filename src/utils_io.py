import os
import json
import numpy as np
import matplotlib.pyplot as plt

def ensure_dir(path: str):
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def save_png(array: np.ndarray, out_path: str, title: str = ""):
    ensure_dir(os.path.dirname(out_path))
    plt.figure()
    plt.imshow(array)
    if title:
        plt.title(title)
    plt.axis("off")
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()

def save_json(obj, out_path: str):
    ensure_dir(os.path.dirname(out_path))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
