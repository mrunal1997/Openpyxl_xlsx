import logging

class LogClass:
    def __init__(self, name='root', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        # ch = logging.StreamHandler()
        # ch.setLevel(level)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s : %(message)s', datefmt="%d-%m-%Y : %H:%M:%S")
        # ch.setFormatter(formatter)

        # Add the handler to the logger
        # self.logger.addHandler(ch)
        file = logging.FileHandler("Logs/logs.log", mode="w")
        file.setFormatter(formatter)
        self.logger.addHandler(file)

    def get_logger(self):
        return self.logger
# class LogClass:
#     def getLogs(self):
#         logger = logging.getLogger()
#         file = logging.FileHandler("Logs/logs.log", mode="w")
#         formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s : %(message)s', datefmt="%d-%m-%Y : %H:%M:%S")
#         file.setFormatter(formatter)
#         logger.addHandler(file)
#         logger.setLevel(logging.INFO)
