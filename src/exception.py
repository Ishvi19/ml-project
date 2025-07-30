import sys
from src.logger import logging

def error_message_detail(error):
    """
    Returns a detailed error message including the script name and line number.
    """
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script: [{0}] at line [{1}] with message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message

# Test the exception
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e)