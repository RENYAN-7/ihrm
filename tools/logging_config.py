import logging


def logging_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 创建处理器
    # 控制台
    ahl = logging.StreamHandler()
    # 文件
    fhl = logging.FileHandler('./log/log.log',encoding='utf-8')
    # 创建格式化器
    fmt = logging.Formatter(fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")
    # 处理器添加格式化器
    ahl.setFormatter(fmt)
    fhl.setFormatter(fmt)
    # 日志器添加处理器
    logger.addHandler(ahl)
    logger.addHandler(fhl)