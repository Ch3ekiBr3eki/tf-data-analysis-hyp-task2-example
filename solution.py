import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ks_2samp

chat_id = 323297403  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, critical_values, significance_level = stats.anderson_ksamp([x, y])
    return statistic > critical_values[2]
