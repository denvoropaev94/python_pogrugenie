# Задание No3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_lowercase
import unittest


class TestFunc(unittest.TestCase):
    def test_1(self):
        self.assertTrue(removal_chars('denvoropaev') == 'denvoropaev')

    def test_2(self):
        self.assertTrue(removal_chars('d!e,n.v-o_r^o&p*a#e!v') == 'denvoropaev')
    def test_3(self):
        self.assertFalse(removal_chars('DEN') == 'DEN')
    def test_4(self):
        self.assertEqual(removal_chars('DEN крутMen'), 'den men')


def removal_chars(text):
    result = ''
    for i in text.lower():
        if i in ascii_lowercase + ' ':
            result += i
    return result


if __name__ == "__main__":
    unittest.main(verbosity=2)