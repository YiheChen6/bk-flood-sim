import networkx as nx
from collections import deque
from typing import List

def bfs_isolated_nodes(G: nx.Graph, sources) -> List[int]:
    """
    从 sources 出发做 BFS，返回不可达的节点列表。
    """
    if not sources:
        return list(G.nodes)
    visited = set()
    q = deque(sources)
    visited.update(sources)
    while q:
        u = q.popleft()
        for v in G.neighbors(u):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return [n for n in G.nodes if n not in visited]

def run(G: nx.Graph, shelters_path: str):
    """
    演示版：以 0 号节点作为避难点。
    """
    sources = [0] if 0 in G.nodes else list(G.nodes)[:1]
    return bfs_isolated_nodes(G, sources)
