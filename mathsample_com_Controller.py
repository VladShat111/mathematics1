import time
#from mathsample_com_learning import CountCorrect

def benchmark(func):
    """ Декоратор, выводящий время, которое заняло выполнение декорируемой функции """

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print()
        func.__name__, time.clock() - t

        return res

    return wrapper


def logging(func):
    """ Декоратор, логирующий работу кода. (хорошо, он просто выводит вызовы, но тут могло быть и логирование!) """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print()
        func.__name__, args, kwargs
        return res

    return wrapper


def CounterOfShowQuantityOfSamles(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} Номер примера: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


def СounterOfUnswers(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} Количество ответов: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


def generalCountCorrect(answer):
    def counterOfCorrectUnswers(func):
        def wrapper(*args, **kwargs):
            if answer:
                wrapper.count += 1
                res = func(*args, **kwargs)
                print("{0} Количество правильных ответов: {1}x".format(func.__name__, wrapper.count))
                return res

        wrapper.count = 0
        return wrapper