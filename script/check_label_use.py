import os

# ラベルフォルダのあるフォルダ名
folder = input("フォルダ名：")

# そのフォルダへ移動
os.chdir(f"../src/{folder}")

# ラベルフォルダを1行ずつリストに格納（空白は除去）
with open("label.txt") as f:
    labels = ["".join(s.split()) for s in f.readlines() if "".join(s.split())][0:100]
print(labels)

# サブフォルダに移動
os.chdir("sub")

# サブフォルダ以下のファイルのリストを取得
file_paths = []
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        file_paths.append(file_path)

# ラベルに一致する文字列が file_paths 内のファイルにあるか確認
bool_no_used_label = True
for label in labels:
    for file in file_paths:
        with open(file, encoding="utf-8") as f:
            file_content = f.read()
            if label in file_content:
                print(f"ラベル{label}は使用済みです．")
                bool_no_used_label = False

if bool_no_used_label:
    print("安全です．")
