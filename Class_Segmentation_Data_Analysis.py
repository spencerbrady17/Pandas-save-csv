import pandas as pd

excel_data_path = "C:\\Users\\AST-TITAN\\Documents\\Matrox\\Results from Context Runs\\Defect A10\\A10_1_30.csv"

df = pd.read_csv(excel_data_path)

sep = df.iloc[1::2]

#split column into multiple columns by delimiter 
defect_values = sep['Class scores'].str.split(',', expand=True)
defect_values.to_csv('out.csv',index=False)

