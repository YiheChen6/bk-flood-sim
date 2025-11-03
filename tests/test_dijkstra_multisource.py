from src import graph_preprocess, dijkstra_multisource

def test_dijkstra_multi_source_runs():
    G = graph_preprocess.run("data/road_network.geojson")
    dist = dijkstra_multisource.run(G, "data/shelters.csv")
    # 至少能给若干节点算出距离
    assert isinstance(dist, dict)
    assert len(dist) >= 1
