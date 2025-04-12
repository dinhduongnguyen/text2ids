import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from large_number import n2w_float_number, n2w_large_number
from single import process_n2w_single
import re

def pre_process_n2w(number: str):
    """Hàm tiền xữ lý dữ liệu đầu vào.

    Args:
        number (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi số sau khi được tiền xữ lý.
    """
    char_to_replace = {
        ' ': '',
        '.': '',
    }

    for key, value in char_to_replace.items():
        number = number.replace(key, value)

    number_pattern = r'^-?[0-9]\d*[,]{0,1}[\d]*$'
    # Kiểm tra tính hợp lệ của đầu vào
    if not re.match(number_pattern, number):
        raise ValueError('Đầu vào không hợp lệ!')

    return number


pre_process_n2w('-112')

def n2w(number: str):
    clean_number = pre_process_n2w(number)
    if (clean_number.find(',') != -1):
        return n2w_float_number(clean_number)
    return n2w_large_number(clean_number)


def n2w_single(number: str):
    if number[0:3] == '+84':
        number = number.replace('+84', '0')

    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
