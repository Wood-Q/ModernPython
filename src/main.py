from rich.traceback import install

install()


# 下面这段代码会故意触发一个错误
def faulty_function():
    result = 1 / 0
    return result


faulty_function()
