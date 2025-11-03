def run(mask, population_path: str): return {"affected_cells": int(getattr(mask,"sum",lambda:0)()) if hasattr(mask,"sum") else 0}
