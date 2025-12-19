import pandas as pd

csv_file_names = [
    'pred-1_80.csv',
    'pred-81_160.csv',
    'pred-161_240.csv',
    'pred-241_320.csv',
    'pred-321_370.csv'
]

csv_file_list = ['./output/' + i for i in csv_file_names]

df_list = [pd.read_csv(file) for file in csv_file_list]

combined_df = pd.concat(df_list, ignore_index=True)

combined_df.to_csv("./output/pred.csv", index=False)