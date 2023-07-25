import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

values = data['whoAmI'].unique()

for i in values:

   data[i] = (data['whoAmI'] == i).astype(int)

data.drop('whoAmI', axis=1, inplace=True)

print(data)