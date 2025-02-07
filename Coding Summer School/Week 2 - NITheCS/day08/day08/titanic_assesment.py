# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:54:23 2025

@author: Lehlo
"""

import numpy as np
from scipy.stats import chi2_contingency

# Give the contingency table with observed counts			

cttitanic = np.array([[122, 203], [167, 118],[528,178], [673,212]])

# Do the test for independence

chi2_contingency(cttitanic) 