import pandas as pd

# Assuming df1 and df2 are your two dataframes
df1 = pd.DataFrame({'Value': ['A', 'B', 'C'], 'Hola': ['R', 'J', 'X']})
df2 = pd.DataFrame({'Value': ['C', 'D', 'E'], 'Hola': ['X', 'J', 'X']})

# Concatenate the dataframes
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Drop duplicates based on all columns
result_df = concatenated_df.drop_duplicates()

# Display the result
print(result_df)
