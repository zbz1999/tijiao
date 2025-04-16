import pandas as pd
import os
from scipy import stats

# 设置文件夹路径
folder_path = r'H:\1_合并RQ3.7\all_leave_Matched_Results_With_Label'

# 创建一个空的DataFrame来存储所有数据
all_data = pd.DataFrame()

# 遍历文件夹中的所有CSV文件
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)

        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, encoding='gbk')
            except UnicodeDecodeError:
                df = pd.read_csv(file_path, encoding='latin1')

        all_data = pd.concat([all_data, df], ignore_index=True)

# 提取两组数据
leave_data = all_data[all_data['leave'] == 1]['Created Files Ratio'].dropna()
stay_data = all_data[all_data['leave'] == 0]['Created Files Ratio'].dropna()

# 初始化结果
method_used = ""
test_result = {}

# 步骤1：正态性检验（D'Agostino-Pearson，适合大样本）
_, p_leave = stats.normaltest(leave_data)
_, p_stay = stats.normaltest(stay_data)
normal_leave = p_leave > 0.05
normal_stay = p_stay > 0.05

# 步骤2：方差齐性检验（Levene）
levene_p = stats.levene(leave_data, stay_data)[1]
equal_var = levene_p > 0.05

# 步骤3：选择合适的检验方法
if normal_leave and normal_stay:
    if equal_var:
        method_used = "Independent t-test"
        t_stat, p_value = stats.ttest_ind(leave_data, stay_data, equal_var=True)
    else:
        method_used = "Welch's t-test"
        t_stat, p_value = stats.ttest_ind(leave_data, stay_data, equal_var=False)
else:
    method_used = "Mann-Whitney U test (non-parametric)"
    t_stat, p_value = stats.mannwhitneyu(leave_data, stay_data, alternative='two-sided')

# 结果展示
print(f"使用的检验方法: {method_used}")
print(f"p-value: {p_value}")
if p_value <= 0.05:
    print("✅ 有显著差异：离开与未离开开发者的 Created Files Ratio 不相等")
else:
    print("❌ 没有显著差异：离开与未离开开发者的 Created Files Ratio 相等")

# 保存原始数据
output_path = r'H:\1_合并RQ3.7\1修改正态分布检验max_leave_analysis_result.csv'
all_data.to_csv(output_path, index=False)

# 保存检验统计结果
result = {
    'Test Method': [method_used],
    't-statistic or U-statistic': [t_stat],
    'p-value': [p_value],
    'Mean (leave==1)': [leave_data.mean()],
    'Mean (leave==0)': [stay_data.mean()],
    'D\'Agostino p (leave)': [p_leave],
    'D\'Agostino p (stay)': [p_stay],
    'Levene p-value': [levene_p]
}
result_df = pd.DataFrame(result)
result_output_path = r'H:\1_合并RQ3.7\1修改正态分布检验max_leave_analysis_t_test_result.csv'
result_df.to_csv(result_output_path, index=False)

print(f"分析结果已保存到: {result_output_path}")