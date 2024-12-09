import random
import string

# ラベルファイルあたりのラベル数
num_labels_per_file = 5000

# ラベルファイル作成先フォルダ名
folder = input("フォルダ名：")


# ラベルを num_labels_per_file 個生成
new_labels: set[str] = set()
while len(new_labels) < num_labels_per_file:
    new_label = "".join(random.choices(string.ascii_letters + string.digits, k = 5))
    new_labels.add(new_label)

# ラベルファイルを生成
file_name = f"../src/{folder}/label.txt"
with open(file_name, 'w') as f:
    f.write("\n".join(new_labels) + "\n")
print(f"フォルダ '{folder}' にラベルファイルを生成しました．")
