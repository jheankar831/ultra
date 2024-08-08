import pandas as pd
import numpy as np
d={
    "Day":[1,2,3,4,5,6],
    "Steps":[2543,5674,7635,6246,8734,3854]
    }
dp=pd.DataFrame(d)
dp["+1000 Steps"]=dp["Steps"]+1000
fi=dp[dp["+1000 Steps"]>7000]["Day"]
print("DataFrame:\n",dp)
print("\nDays on which Steps were >7000:\n",fi)
