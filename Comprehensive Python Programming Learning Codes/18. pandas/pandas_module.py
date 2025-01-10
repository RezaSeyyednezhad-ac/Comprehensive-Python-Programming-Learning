# Pandas in Python پانداس در پایتون
# Install pandas: نصب پانداس 
#           pip install pandas

# import pandas as pd
# """
# pandas.read_csv(filepath, *, sep=<no_default>, 
#                 header='infer', names=<no_default>, index_col=None, 
#                 usecols=None, dtype=None)
# """
# filepath = "C:/Users/Reza Seyyednezhad/Desktop/python/python example/pandas/scores.csv"
# read_data = pd.read_csv(filepath)
# print(read_data.head())

# # -------------------------------------- # 

# Pandas in Python پانداس در پایتون
import pandas as pd

# Read Files
filepath = "C:/Users/Reza Seyyednezhad/Desktop/python/python example/pandas/scores.csv"
read_file = pd.read_csv(filepath, usecols=['id', 'first_name', 'last_name', 'gender', 
                                           'physics_score', 'chemistry_score', 'biology_score',
                                           'english_score', 'geography_score'])[:40]
# print(read_file)

average_list = []

for i in range(len(read_file.values)):
    fullName = read_file.loc[i]['first_name'] + " " + read_file.loc[i]['last_name']
    avrage_Score = read_file.loc[i][4:].mean()
    res = {
        "id": int(read_file.loc[i]['id']),
        "Full Name": fullName,
        "Score": float(avrage_Score)
    }
    average_list.append(res)

newDf = pd.DataFrame(average_list)
newDf.set_index('id', inplace=True)
newDf.to_csv('./newFile.csv')
print(newDf)