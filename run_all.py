import os, yaml
import numpy as np
from src import (
    raster_thresholding, component_labeling, map_algebra,
    graph_preprocess, road_clipping, dijkstra_multisource, connectivity_bfs
)
from src.utils_io import save_png, save_json

def main():
    cfg = yaml.safe_load(open('config.yaml', encoding='utf-8'))
    out_dir = cfg['paths']['output']

    print('1 Raster Thresholding...')
    mask = raster_thresholding.run(cfg['paths']['flood_depth'], cfg['params']['dcrit'])

    print('2 Connected Components...')
    regions = component_labeling.run(mask, neighbor_rule=cfg['params']['neighbor_rule'])

    print('3 Population Impact Assessment...')
    pop_stats = map_algebra.run(mask, cfg['paths']['population'])

    print('4 Graph Preprocessing & Clipping...')
    G = graph_preprocess.run(cfg['paths']['roads'])
    Gf = road_clipping.run(G, mask)

    print('5 Multi-source Dijkstra...')
    dist = dijkstra_multisource.run(Gf, cfg['paths']['shelters'])

    print('6 BFS Connectivity Validation...')
    isolated = connectivity_bfs.run(Gf, cfg['paths']['shelters'])

    # === 真正落盘输出（占位图/数据）===
    save_png(np.array(mask), os.path.join(out_dir, 'flood_mask.png'), 'Flood Mask')
    save_png(np.array(mask)*2, os.path.join(out_dir, 'affected_population.png'), 'Population (demo)')
    save_png(np.array([[0,1],[1,0]]), os.path.join(out_dir, 'dijkstra_distances.png'), 'Dijkstra (demo)')
    save_png(np.array([[1,1],[1,1]]), os.path.join(out_dir, 'road_clipped.png'), 'Roads Clipped (demo)')
    save_json({"isolated_zones": isolated, "pop_stats": pop_stats, "dist": dist}, os.path.join(out_dir, 'isolated_zones.json'))

    print(' Finished! Results in', out_dir)

if __name__ == '__main__':
    main()
