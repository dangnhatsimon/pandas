import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players.axes[0]), len(players.axes[1])]