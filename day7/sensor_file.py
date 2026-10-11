values = []

with open("sensor_data.txt","r")as f:
    for line in f:
        line = line.strip()
        try:
            v = float(line)
        except ValueError:
            print(f"跳过无效：{line}")
            continue
        if v > 5.0:
            print(f"超量程，丢弃：{line}")
            continue
        values.append(v)

with open("clean_data.txt","w") as f:
    for v in values:
        f.write(f"{v}\n")

print(f"有效数据{len(values)}个，平均值{sum(values)/len(values):.3f}")
