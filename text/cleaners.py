# from phonemizer.phonemize import phonemize
from text.symbols import phonemes_set

""" from https://github.com/keithito/tacotron """

'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
    1. "english_cleaners" for English text
    2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
         the Unidecode library (https://pypi.python.org/pypi/Unidecode)
    3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
         the symbols in symbols.py to match your data).
'''

import re
import unicodedata
from vn_numbers import vn_convert_numbers


# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, ' ', text)

def basic_cleaners(text):
    text = to_phonemes(text)
    text = collapse_whitespace(text)
    text = text.strip()
    return text

# Vietnamese text cleaner
def norm_text(text):
    return unicodedata.normalize('NFC', text)


def vn_cleaners(text):
    text = norm_text(text)
    text = lowercase(text)
    text = vn_convert_numbers(text)
    text = ''.join([t for t in text if t in phonemes_set])
    text = text.strip()
    return text

