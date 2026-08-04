import pandas as pd
import numpy as np
data = {
"Name": [" Alice ", "BOB", None, "charlie", "Alice"],
"Age": [25, "unknown", 35, -5, 25],
"Salary": [50000, 60000, "n/a", 80000, 50000],
"City": ["NYC", "LA", "Chicago", "NYC", "NYC"]
}
#df = pd.DataFrame(data)
#

df1 = pd.DataFrame({
"Product": ["Widget", "Gadget", "Widget", "Doohickey"],
"Price": [10.99, -5.00, 10.99, 1500.00],
"Rating": [4.5, 3.2, 4.5, 6.1]
})
df1.drop_duplicate()
print(df1)