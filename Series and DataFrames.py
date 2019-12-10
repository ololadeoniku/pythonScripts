import numpy as np
import pandas as pd

from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2','row 3','row 4','row 5', 'row 6', 'row 7', 'row 8'])
series_obj['row 7']
series_obj[[7]]
series_obj['row 3':'row 7']
series_obj[series_obj > 6]
series_obj['row 1', 'row 5', 'row 8'] = 8
missing = np.nan
series_obj = Series(['row 1', 'row 2', missing, 'row 4','row 5', 'row 6', missing, 'row 8'])
series_obj.isnull()

series_obj = pd.Series(np.arange(6))
series_obj.name = "added_variable"
series_obj


#DATAFRAME
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
print(DF_obj)
DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']]
DF_obj < .2

DF_obj_2 = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj_2.ix[3:5, 0] = missing
DF_obj_2.ix[1:4, 5] = missing
print(DF_obj_2)
DF_obj_2.isnull().sum()
filled_DF = DF_obj_2.fillna(0)
filled_DF
filled_DF = DF_obj_2.fillna({0: 0.1, 5: 1.25})
filled_DF
fill_DF = DF_obj_2.fillna(method='ffill')
fill_DF
DF_no_NaN = DF_obj_2.dropna(axis=1)
DF_no_NaN
DF_obj_2.dropna(how='all')


DF_obj_3 = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
DF_obj_3
DF_obj_3.duplicated()
DF_obj.drop_duplicates()
DF_obj.drop_duplicates(['column 3'])


pd.concat([DF_obj, DF_obj_2], axis =1)
pd.concat([DF_obj, DF_obj_2])
DF_obj.drop([0,2])
DF_obj.drop([0,2], axis=1)

variable_added = DataFrame.join(DF_obj, series_obj)
added_datatable = variable_added.append(series_obj, ignore_index=False)
added_datatable
added_datatable = variable_added.append(variable_added, ignore_index=True)
added_datatable
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
DF_sorted

