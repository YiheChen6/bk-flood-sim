import networkx as nx
from typing import Dict, Iterable

def multi_source_dijkstra_distances(G: nx.Graph, sources: Iterable) -> Dict:
    """
    计算多源到所有节点的最短距离（简单加权 = edge length 或 1）
    """
    # 如果没有权重就当每条边长度 1
    return nx.multi_source_dijkstra_path_length(G, sources, weight="length")

def run(G: nx.Graph, shelters_path: str):
    """
    演示版：把 0 号节点当作避难点。
    真实实现应从 shelters.csv 读取对应节点/坐标映射。
    """
    sources = [0] if 0 in G.nodes else list(G.nodes)[:1]
    return multi_source_dijkstra_distances(G, sources)
