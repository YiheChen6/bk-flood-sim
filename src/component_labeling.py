import numpy as np
from collections import deque

def _neighbors(r, c, H, W, k=8):
    if k == 4:
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    else:
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W:
            yield nr, nc

def connected_components(mask: np.ndarray, neighbor_rule: int = 8):
    """
    对 0/1 掩膜做连通分量标记，返回 labels, n_labels
    labels 与 mask 同形状，分量编号从 1..n
    """
    H, W = mask.shape
    labels = np.zeros((H, W), dtype=int)
    comp_id = 0
    for r in range(H):
        for c in range(W):
            if mask[r, c] == 1 and labels[r, c] == 0:
                comp_id += 1
                # BFS 填充
                q = deque([(r, c)])
                labels[r, c] = comp_id
                while q:
                    cr, cc = q.popleft()
                    for nr, nc in _neighbors(cr, cc, H, W, neighbor_rule):
                        if mask[nr, nc] == 1 and labels[nr, nc] == 0:
                            labels[nr, nc] = comp_id
                            q.append((nr, nc))
    return labels, comp_id

def run(mask: np.ndarray, neighbor_rule: int = 8):
    return connected_components(mask, neighbor_rule)
