from datetime import datetime


class LogManage:

    def __init__(self):
        self.f = None
        self.time = datetime.now().strftime(" %d/%m/%Y %H:%M:%S ")

    def open_file(self):
        """Author: Maor Maharizi,
                Created: 04.02.2023,
                Detail: open log file
                Return: Null"""
        try:
            self.f = open('C:\\Users\\User\\PycharmProjects\\Shape2\\shapes\\log', 'a')
            return 1
        except FileExistsError:
            print('')

    def write_to_log(self, dictionary):
        """Author: Maor Maharizi,
                Created: 04.02.2023,
                Detail: write to log file
                Return: Null"""
        self.f.write("\n{")
        self.f.write(f"\n{dictionary}\n" + self.time)
        self.f.write("\n}")
        self.f.flush()

    def close_log_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: close logs file
                Return: Null"""
        self.f.close()
