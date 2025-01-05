import json5


# 文件不存在就创建
def file_exists_create(file_path):
    if not file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            json5.dump({}, f)
