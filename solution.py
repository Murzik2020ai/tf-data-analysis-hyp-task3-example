import pandas as pd
import numpy as np


chat_id = 1226526788

from scipy.stats import wilcoxon
def solution(x: np.array, y:np.array) -> bool:
    pvalue = wilcoxon(x,y).pvalue
    return True if pvalue < 0.03 else False
