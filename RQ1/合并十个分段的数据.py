import csv

# 定义每个文件的数据
data = {
    "0-99": {
        "0-10%": 2, "10-20%": 0, "20-30%": 0, "30-40%": 4, "40-50%": 3, "50-60%": 17, "60-70%": 13, "70-80%": 16, "80-90%": 12, "90-100%": 7
    },
    "100-199": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 1, "50-60%": 6, "60-70%": 18, "70-80%": 29, "80-90%": 38, "90-100%": 2
    },
    "200-299": {
        "0-10%": 1, "10-20%": 0, "20-30%": 1, "30-40%": 0, "40-50%": 1, "50-60%": 3, "60-70%": 5, "70-80%": 15, "80-90%": 33, "90-100%": 6
    },
    "300-399": {
        "0-10%": 0, "10-20%": 0, "20-30%": 1, "30-40%": 0, "40-50%": 1, "50-60%": 1, "60-70%": 8, "70-80%": 20, "80-90%": 24, "90-100%": 2
    },
    "400-499": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 0, "50-60%": 4, "60-70%": 4, "70-80%": 7, "80-90%": 12, "90-100%": 3
    },
    "500-599": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 0, "50-60%": 0, "60-70%": 2, "70-80%": 8, "80-90%": 9, "90-100%": 2
    },
    "600-699": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 0, "50-60%": 1, "60-70%": 6, "70-80%": 4, "80-90%": 7, "90-100%": 0
    },
    "700-799": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 0, "50-60%": 1, "60-70%": 2, "70-80%": 8, "80-90%": 5, "90-100%": 0
    },
    "800-899": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 1, "40-50%": 0, "50-60%": 0, "60-70%": 2, "70-80%": 1, "80-90%": 3, "90-100%": 0
    },
    "900-999": {
        "0-10%": 0, "10-20%": 0, "20-30%": 0, "30-40%": 0, "40-50%": 0, "50-60%": 2, "60-70%": 5, "70-80%": 3, "80-90%": 6, "90-100%": 2
    }
}

# CSV文件头部
headers = ["Percentage Range"] + list(data.keys())

# 写入CSV文件
with open('H:/1_合并RQ2/percentage_distribution.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  # 写入头部

    # 写入每个百分比区间的数据
    for percentage, value in data["0-99"].items():
        row = [percentage]
        for key in data.keys():
            row.append(data[key].get(percentage, 0))
        writer.writerow(row)

print("CSV文件已保存为 'percentage_distribution.csv'")