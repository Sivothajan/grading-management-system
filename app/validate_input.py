import numpy as np

# allowed semesters
allowed_semester = {"1", "2", "3", "4", "5", "6", "7", "8"}

# allowed course codes
allowed_course_code = {"CSC1002"}

# allowed course credit limits
allowed_credit = {1, 2, 3, 6}

# available GPV/ GPA systems
allowed_gpv_4p0 = {x for x in np.arange(0.00, 4.00, 0.01)}
allowed_gpv_4p2 = {x for x in np.arange(0.00, 4.20, 0.01)}
allowed_gpv_5p0 = {x for x in np.arange(0.00, 5.00, 0.01)}
allowed_gpv_10p0 = {x for x in np.arange(0.00, 10.00, 0.01)}

# allowed GPV/ GPA system
allowed_gpv = allowed_gpv_4p0     

# banned inputs
banned_inputs = {}
