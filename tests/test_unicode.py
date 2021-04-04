from containers.unicode import NormalizedStr
import pytest



strings = [
    'César Chávez',                             # spanish, NFD normalized
    'César Chávez',                             # spanish, NFC normalized
    'César Chávez',                             # spanish, unnormalized
    ]


def test_repr_0():
    assert repr(NormalizedStr(strings[0])) == "NormalizedStr('César Chávez', 'NFC')"

def test_repr_1():
    assert repr(NormalizedStr(strings[1])) == "NormalizedStr('César Chávez', 'NFC')"

def test_repr_2():
    assert repr(NormalizedStr(strings[2])) == "NormalizedStr('César Chávez', 'NFC')"


def test_repr_NFD_0():
    assert repr(NormalizedStr(strings[0], 'NFD')) == "NormalizedStr('César Chávez', 'NFD')"

def test_repr_NFD_1():
    assert repr(NormalizedStr(strings[1], 'NFD')) == "NormalizedStr('César Chávez', 'NFD')"

def test_repr_NFD_2():
    assert repr(NormalizedStr(strings[2], 'NFD')) == "NormalizedStr('César Chávez', 'NFD')"


def test_str_0():
    assert str(NormalizedStr(strings[0])) == 'César Chávez'

def test_str_1():
    assert str(NormalizedStr(strings[1])) == 'César Chávez'

def test_str_2():
    assert str(NormalizedStr(strings[2])) == 'César Chávez'


def test_len_0():
    assert len(NormalizedStr(strings[0])) == 12

def test_len_1():
    assert len(NormalizedStr(strings[1])) == 12

def test_len_2():
    assert len(NormalizedStr(strings[2])) == 12


def test_len_NFD_0():
    assert len(NormalizedStr(strings[0], 'NFD')) == 14

def test_len_NFD_1():
    assert len(NormalizedStr(strings[1], 'NFD')) == 14

def test_len_NFD_2():
    assert len(NormalizedStr(strings[2], 'NFD')) == 14


def test_contains_0():
    assert strings[0] in NormalizedStr(strings[0])

def test_contains_1():
    assert strings[0] in NormalizedStr(strings[1])

def test_contains_2():
    assert strings[0] in NormalizedStr(strings[2])

def test_contains_3():
    assert strings[0] in NormalizedStr(strings[0], 'NFD')

def test_contains_4():
    assert strings[0] in NormalizedStr(strings[1], 'NFD')

def test_contains_5():
    assert strings[0] in NormalizedStr(strings[2], 'NFD')

def test_contains_6():
    assert strings[1] in NormalizedStr(strings[0])

def test_contains_7():
    assert strings[1] in NormalizedStr(strings[1])

def test_contains_8():
    assert strings[1] in NormalizedStr(strings[2])

def test_contains_9():
    assert strings[1] in NormalizedStr(strings[0], 'NFD')

def test_contains_10():
    assert strings[1] in NormalizedStr(strings[1], 'NFD')

def test_contains_11():
    assert strings[1] in NormalizedStr(strings[2], 'NFD')

def test_contains_12():
    assert strings[2] in NormalizedStr(strings[0])

def test_contains_13():
    assert strings[2] in NormalizedStr(strings[1])

def test_contains_14():
    assert strings[2] in NormalizedStr(strings[2])

def test_contains_15():
    assert strings[2] in NormalizedStr(strings[0], 'NFD')

def test_contains_16():
    assert strings[2] in NormalizedStr(strings[1], 'NFD')

def test_contains_17():
    assert strings[2] in NormalizedStr(strings[2], 'NFD')

def test_contains_18():
    assert 'Cesar' not in NormalizedStr(strings[0], 'NFD')

def test_contains_19():
    assert 'Cesar' not in NormalizedStr(strings[1], 'NFD')

def test_contains_20():
    assert 'Cesar' not in NormalizedStr(strings[2], 'NFD')

def test_contains_21():
    assert 'Cesar' not in NormalizedStr(strings[0], 'NFC')

def test_contains_22():
    assert 'Cesar' not in NormalizedStr(strings[1], 'NFC')

def test_contains_23():
    assert 'Cesar' not in NormalizedStr(strings[2], 'NFC')


def test_getitem_0():
    assert NormalizedStr(strings[0], 'NFC')[0] == 'C'

def test_getitem_1():
    assert NormalizedStr(strings[0], 'NFC')[1] == 'é'

def test_getitem_2():
    assert NormalizedStr(strings[0], 'NFC')[9] == 'v'

def test_getitem_3():
    assert NormalizedStr(strings[0], 'NFD')[0] == 'C'

def test_getitem_4():
    assert NormalizedStr(strings[0], 'NFD')[1] == 'e'

def test_getitem_5():
    assert NormalizedStr(strings[0], 'NFD')[9] == 'a'


def test_lower_0():
    assert str(NormalizedStr(strings[0], 'NFD').lower()) == 'césar chávez'

def test_lower_1():
    assert str(NormalizedStr(strings[0], 'NFC').lower()) == 'césar chávez'

def test_lower_2():
    assert str(NormalizedStr(strings[1], 'NFD').lower()) == 'césar chávez'

def test_lower_3():
    assert str(NormalizedStr(strings[1], 'NFC').lower()) == 'césar chávez'

def test_lower_4():
    assert str(NormalizedStr(strings[2], 'NFD').lower()) == 'césar chávez'

def test_lower_5():
    assert str(NormalizedStr(strings[2], 'NFC').lower()) == 'césar chávez'

def test_lower_6():
    x = NormalizedStr(strings[0])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'

def test_lower_7():
    x = NormalizedStr(strings[1])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'

def test_lower_8():
    x = NormalizedStr(strings[2])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'


def test_upper_0():
    assert str(NormalizedStr(strings[0], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_1():
    assert str(NormalizedStr(strings[0], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_2():
    assert str(NormalizedStr(strings[1], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_3():
    assert str(NormalizedStr(strings[1], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_4():
    assert str(NormalizedStr(strings[2], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_5():
    assert str(NormalizedStr(strings[2], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_6():
    x = NormalizedStr(strings[0])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_upper_7():
    x = NormalizedStr(strings[1])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_upper_8():
    x = NormalizedStr(strings[2])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_add_0():
    x = NormalizedStr(strings[0])
    y = NormalizedStr(strings[1])
    z = NormalizedStr(strings[2])
    assert str(x + y + z) == str(y + x + z)
    assert str(x) == str(NormalizedStr(strings[0], 'NFC')) 
    assert str(y) == str(NormalizedStr(strings[1], 'NFC')) 
    assert str(z) == str(NormalizedStr(strings[2], 'NFC')) 

def test_add_1():
    x = NormalizedStr(strings[0], 'NFD')
    y = NormalizedStr(strings[1], 'NFD')
    z = NormalizedStr(strings[2], 'NFD')
    assert str(x + y + z) == str(y + x + z)
    assert str(x) == str(NormalizedStr(strings[0], 'NFD')) 
    assert str(y) == str(NormalizedStr(strings[1], 'NFD')) 
    assert str(z) == str(NormalizedStr(strings[2], 'NFD')) 

def test_add_2():
    x = NormalizedStr(strings[0], 'NFD')
    y = NormalizedStr(strings[1], 'NFD')
    z = NormalizedStr(strings[2], 'NFD')
    assert str(x + strings[1] + strings[2]) == str(y + x + z)
    assert str(x) == str(NormalizedStr(strings[0], 'NFD')) 
    assert str(y) == str(NormalizedStr(strings[1], 'NFD')) 
    assert str(z) == str(NormalizedStr(strings[2], 'NFD')) 

def test_add_3():
    x = NormalizedStr(strings[0], 'NFC')
    y = NormalizedStr(strings[1], 'NFC')
    z = NormalizedStr(strings[2], 'NFC')
    assert str(x + strings[1] + strings[2]) == str(y + x + z)
    assert str(x) == str(NormalizedStr(strings[0], 'NFC')) 
    assert str(y) == str(NormalizedStr(strings[1], 'NFC')) 
    assert str(z) == str(NormalizedStr(strings[2], 'NFC')) 


def test_add_3():
    x = '\u0301'
    y = 'a'
    assert str(NormalizedStr(x)) + y == str(NormalizedStr(x+y))

def test_add_4():
    x = '\u0301'
    y = 'a'
    assert str(NormalizedStr(x,'NFD')) + y == str(NormalizedStr(x+y,'NFD'))

def test_add_5():
    x = '\u0302'
    y = 'a'
    assert str(NormalizedStr(x)) + y == str(NormalizedStr(x+y))

def test_add_6():
    x = '\u0302'
    y = 'a'
    assert str(NormalizedStr(x,'NFD')) + y == str(NormalizedStr(x+y,'NFD'))


def test_iter_0():
    x = NormalizedStr(strings[0], 'NFC')
    assert list(x) == list(strings[0])

def test_iter_1():
    x = NormalizedStr(strings[0], 'NFD')
    assert list(x) == list(strings[1])

def test_iter_2():
    x = NormalizedStr(strings[0], 'NFC')
    assert len(list(x)) == 12

def test_iter_3():
    x = NormalizedStr(strings[2], 'NFC')
    assert len(list(x)) == 12
