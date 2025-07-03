import pytest
import pandas as pd
from src.string_utils import clean_strings
@pytest.mark.parametrize("in_strings,out_strings", [
    (pd.Series(["AK!SHAY","Fra_$nk"]), pd.Series(["akshay","frank"])),
    (pd.Series(["AK SHA Y","  Frank%"]),(pd.Series(["akshay","frank"]))),
])
def test_clean_stringpy(in_strings,out_strings):
    assert clean_strings(in_strings).equals(out_strings)