# 2 sample t-test using Midwest results
#reference : https://www.youtube.com/watch?v=8uUfHx3M0Jw
import numpy as np
from scipy import stats as st
a=min

MI  = int(19.42)
OH  = int(16.89)
#ttest=st.ttest_ind(MIDMeanresults,OHMeanresults)
t2, P2 =st.ttest_ind( MI ,OH ,equal_var=False)
print (t2, P2)