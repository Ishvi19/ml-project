import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ..exception import CustomException
from ..logger import logging
import pandas as pd

from sklearn.model_selection import tain_test_split
from dataclasses import dataclass
