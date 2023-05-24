class FormatString:

    def __init__(self):
        pass

    def iterate(self, argument):
        list = []
        for string in argument:
            string = str(string)
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")
            string = string.strip("'")

            list.append(string)

        return list

    def iterate_first_value(self, argument):
        list = []
        for value in argument:
            value1, value2 = value
            list.append(value1)
        return list

    def iterate_second_value(self, argument):
        list = []
        for value in argument:
            value1, value2 = value
            list.append(value2)

        return list

    def format(self, string, level):
        string = str(string)
        if level == 1:
            string = string.strip("[]")
        elif level == 2:
            string = string.strip("[]")
            string = string.strip("()")

        elif level == 3:
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")

        elif level == 4:
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")
            string = string.strip("'")

        elif level == 5:
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")
            string = string.strip("'")
            if string[-1] == '3':
                string = string[:-4]

        return string
