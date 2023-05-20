import pandas as pd

# 讀取CSV文件
df = pd.read_csv('./turkiye-student-evaluation_generic.csv')

# 儲存要删除的行索引
rows_to_delete = []

# 儲存異常值的行索引
out_of_range_rows = pd.DataFrame(columns=df.columns)

# 儲存缺失值的行索引
rows_with_missing_values = []

for index, row in df.iterrows():
    # 檢查Q1到Q28的每一行是否具有相同数值
    if row['Q1':'Q28'].nunique() == 1:
        rows_to_delete.append(index)
        # print(f"Row {index+1}: All values are the same.")
        # print(out_of_range_rows)
    # 檢查Q1~Q28中是否有異常值（低於1或超過5）
    if not row['Q1':'Q28'].isin(range(0, 6)).all():
        rows_to_delete.append(index)
        out_of_range_rows = out_of_range_rows.append(row)
    # 檢查該行是否有任何缺失值
    if row.isnull().any():
        rows_with_missing_values.append(index)

# 列印具有異常值的行的索引
# if not out_of_range_rows.empty:
#     print("Rows with values out of range (0~5):")
#     print(out_of_range_rows)

# 列印具有缺失值的行的索引
# print(rows_with_missing_values)

# 删除具有相同数值的行
df_filtered = df.drop(rows_to_delete)

# 将筛选后的数据保存为新的CSV文件
df_filtered.to_csv('output2.csv', index=False)