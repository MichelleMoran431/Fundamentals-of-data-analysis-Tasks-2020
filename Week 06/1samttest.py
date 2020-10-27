# One sample t-test using Midwest results
#reference : https://www.youtube.com/watch?v=8uUfHx3M0Jw
import numpy as np
from scipy import stats as st
results=([19.63139, 11.24331 ,17.03382, 17.27895, 14.47600, 18.90462, 11.91739,16.19712, 14.10765, 41.29581])
Mean=([32])
ttest=st.ttest_1samp(results,Mean)
print ('t-test independent', ttest)