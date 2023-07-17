# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class MarkError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Оценка выходит за диапозон используемой шкалы оценивания"


class BigNameError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Значение {self.string} должно начинаться с заглавной буквы, а остальные символы должны быть строчными"


class LetterNameError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Значение {self.string} должно содерджать только буквы"


class Fullname:
    def __init__(self):
        self

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")

    def validate(self, value):
        if value.isalpha():
            if not value.istitle():
                raise ValueError(f"{value}")

        else:
            raise ValueError(f"{value}")


class Mark:

    def __init__(self, min_mark, max_mark):
        self.min_mark = min_mark
        self.max_mark = max_mark

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"Значение {value} должно быть числовым")
        if value < 2 or value > 5:
            raise MarkError("")


class Score:
    def __init__(self, min_mark, max_mark):
        self.min_mark = min_mark
        self.max_mark = max_mark

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство '{self.param_name}' нельзя удалить")

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f"Значение {value} должно начинастя с заглавной буквы, а остальные символы должны быть строчными")
        if value < 0 or value > 100:
            raise ValueError("Итоговый результат должен быть в диапозоне от 0 до 100 баллов")


class Student:
    first_name = Fullname()
    second_name = Fullname()
    last_name = Fullname()
    _mark = Mark(2, 10 )
    _score = Score(0, 100)
    _subjects = []
    _subject_score = {}
    _subject_mark = []
    _student_list = []

    def __init__(self, first_name="New", second_name="New",
                 last_name="New", list_of_subjects=[],
                 sub_mark=[], sub_score=[]):

        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self._subjects = list_of_subjects
        self._subject_mark = sub_mark
        self._subject_score = sub_score

    def get_s_t(self):
        return self._student_list

    def get_s_s(self):
        return self._subject_score

    @property
    def mark(self):
        return self._mark

    @property
    def score(self):
        return self._score

    @mark.setter
    def mark(self, value):
        if 2 <= value < 6:
            self._subject_mark.append(value)
        elif value < 2:
            self._subject_mark.append(2)
        else:
            self._subject_mark.append(5)

    @score.setter
    def score(self, subject, score):
        if subject not in self._subject_score:
            self._subject_score[subject] = []
        if 0 <= score < 101:
            self._subject_score[subject].append(score)
        elif score < 0:
            self._subject_score[subject].append(0)
        else:
            self._subject_score[subject].append(100)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.last_name}"

    def __enter__(self):
        new_file = open("students_data.csv", "r", encoding="utf-8", newline="")
        csv_file = csv.reader(new_file, dialect="excel", delimiter=" ")
        new_dict = {}
        for line in csv_file:

            key = f"{line[0]} {line[1]} {line[2]}"
            if key not in new_dict:
                new_dict[key] = [[], [], {}]
            if line[3] not in new_dict[key][0]:
                new_dict[key][0].append(line[3])
                new_dict[key][2][line[3]] = []
            try:
                new_dict[key][1].append(int(line[4]))
            except Exception:
                continue
            try:
                new_dict[key][2][line[3]].append(int(line[5]))
            except Exception:
                continue

        for n_key, value in new_dict.items():
            if n_key.split()[0] != "first_name":
                student = Student(n_key.split()[0], n_key.split()[1], n_key.split()[2], value[0], value[1], value[2])
                self._student_list.append(student)
        return self
        new_file.close()

    def avg_score(self):
        new_dict = {}
        for key, i in self._subject_score.items():
            new_dict[key] = sum(i) / len(i)
        return new_dict

    def avg_mark(self):
        return round(sum(self._subject_mark) / len(self._subject_mark), 2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


stt_one = Student()

with stt_one as st:
    for i in st.get_s_t():
        print(i.avg_mark())