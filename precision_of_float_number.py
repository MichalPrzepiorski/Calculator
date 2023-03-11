class precision_of_float_number():

    def __init__(self, number):
        self.number = number

    def check_precision(self):
        return(len(str(self.number).split('.')[1]))

# if __name__ == "__main__":
#     precision_of_float_number(1.987567435).check_precision()

