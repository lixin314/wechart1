import logging
import logging.handlers


def log_init():
    log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
    format = logging.Formatter(log_format_str)
    root = logging.getLogger('my_log')
    # 加入输出流句柄
    s = log_handler = logging.StreamHandler()
    s.setFormatter(format)
    # 加入文件句柄
    h = logging.handlers.RotatingFileHandler("./tmp.log", mode='a', encoding="utf-8")
    h.setFormatter(format)
    root.addHandler(s)
    root.addHandler(h)
    root.setLevel(logging.DEBUG)


log = logging.getLogger('my_log')






