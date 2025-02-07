# CHPC Summer School 2025
# Probability & Statistics: Categorical Data & Probability
# Example: Jerusalema

# Import packages and functions

import numpy as np
from scipy.stats import chi2_contingency

# Give the contingency table with observed counts			

ctJerusalema = np.array([[28, 12], [16, 24]])

# Do the test for independence

chi2_contingency(ctJerusalema) 
#chi2_contigency is from the scipy.stats package
