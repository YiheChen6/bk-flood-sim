from src import graph_preprocess, connectivity_bfs

def test_connectivity_bfs_runs():
    G = graph_preprocess.run("data/road_network.geojson")
    iso = connectivity_bfs.run(G, "data/shelters.csv")
    # 返回一个列表（可能为空）
    assert isinstance(iso, list)
