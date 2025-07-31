import sys
from src.logger import logging

def error_message_detail(error, exc_tb):
    """
    Returns a detailed error message including the script name and line number.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script: [{file_name}] at line [{line_number}] with message: [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, exc_tb):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_tb)

    def __str__(self):
        return self.error_message

# Test the exception
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        _, _, exc_tb = sys.exc_info()  #  Get traceback here, inside except block
        raise CustomException(e, exc_tb)