from random import randint


class RandomPassword:
    def __init__(self):
        pass

    @staticmethod
    def generate():
        password = ""
        for _ in range(randint(14, 20)):
            password += chr(randint(32, 126))
        return password



if __name__ == '__main__':

    pass_1 = RandomPassword()

    print(pass_1.generate())
