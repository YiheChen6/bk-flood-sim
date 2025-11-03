from src import graph_preprocess, road_clipping

def test_graph_build_and_clip():
    G = graph_preprocess.run("data/road_network.geojson")
    G2 = road_clipping.run(G, None)
    # 至少有边
    assert len(G2.edges) >= 1
