import logging
import os

current_log_file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "Logs/current_log_file.log")


def get_logs():
    """
    this method used to generate logs and also store the logs in current_log_file file
    :return: logger
    """
    logger = logging.getLogger()
    filehandler = logging.FileHandler(current_log_file_path, mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger
