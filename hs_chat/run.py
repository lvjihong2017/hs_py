from app import app  # 导入您的Flask应用实例
if __name__ == '__main__':
    app.run(allow_unsafe_werkzeug=True)
