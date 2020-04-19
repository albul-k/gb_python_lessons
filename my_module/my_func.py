from random import randint


def get_randomint_list(num: int, rand_from: int, rand_to: int) -> list:
    """[summary]

    Arguments:
        num {int} -- [description]
        rand_from {int} -- [description]
        rand_to {int} -- [description]

    Returns:
        list -- [description]
    """
    random_list = []
    for i in range(0, num):
        random_list.append(randint(rand_from, rand_to))
    return random_list
