import networkx as nx

def run(roads_path: str):
    """
    演示版：构造一个小图（2 个节点 1 条边）
    真实实现中，应该把 roads geojson 读进来转为图。
    """
    G = nx.Graph()
    G.add_edge(0, 1, length=1.0)
    return G
