from numpy import ndarray as GridType
from typing import NamedTuple

class Segments(NamedTuple):
    rows: GridType
    columns: GridType
    blocks: GridType