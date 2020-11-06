import random

def rand_dict(n):
    return {random.randint(0,21) : random.randint(0,21) for _ in range(n)}


def reverse_dict(dictionary):
    return {val : key for (key, val) in dictionary.items()}


if __name__ == "__main__":
    di = rand_dict(14)
    print(di)
    print(reverse_dict(di))