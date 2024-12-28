import logging

# 配置日志
logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    # 你的代码逻辑
    1 / 0
except Exception as e:
    # 记录错误日志
    logging.error('An error occurred', exc_info=True)
