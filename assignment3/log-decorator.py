import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

logger.log(logging.INFO,"string to be logged")

def logger_decorator(func):
    def wrapper(*args,**kwargs):
        logger.log(logging.INFO,f"function: {func.__name__}")
        logger.log(logging.INFO,f"positional parameters: {args}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        result = func(*args,**kwargs)
        logger.log(logging.INFO,f"return: {result}")
        return result
    return wrapper

@logger_decorator
def no_params():
    print("Hello Sunshine!")

@logger_decorator
def test_arguements(*args):
    return True
@logger_decorator
def test_other_arguements(**kwargs):
    return logger_decorator

no_params()
test_arguements(7,11,9)
test_other_arguements(word1="sunshine",word2="hot")

#Task2
