from src.exception import CustomException
import sys

try:
    x = 10 / 0
except Exception as e:
    _, _, exc_tb = sys.exc_info()
    custom_error = CustomException(e, exc_tb)
    print(custom_error)