"""
CRS 工具的占位。真实 GIS 版本可用：
- rasterio/pyproj 处理 raster 的 CRS
- geopandas.GeoDataFrame.to_crs() 处理矢量数据
"""

def reproject_placeholder(*args, **kwargs):
    return None
