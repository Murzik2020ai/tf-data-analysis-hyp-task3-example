import pandas as pd
import numpy as np


chat_id = 1226526788
from scipy.stats import ttest_ind

def solution(x: np.array, y:np.array) -> bool:
  pvalue = ttest_ind(x,y,equal_var=False).pvalue
  return True if pvalue < 0.03 else False
