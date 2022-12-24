class Course:
    def __init__(self, name, start_date, number_of_lectures, teacher):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        self.lectures = list()
        # generator of lectures
        for i in range(1, number_of_lectures + 1):
            self.lectures.append(Lecture('Lecture ' + str(i), i, teacher, self))
        # generator of homeworks
        self.homeworks = {i: Homework('Homework ' + str(i), None) for i in range(1, number_of_lectures + 1)}
        self.enrolled = list()
        teacher.all_lectures.append(self.lectures)
        teacher.all_courses.append(self)

    # назв-ие курса + стартовая дата
    def __str__(self):
        return f"{self.name} ({self.start_date})"

    # список студентов
    def enrolled_by(self):
        return self.enrolled

    # вывод лекции по номеру
    def get_lecture(self, number):
        if number > self.number_of_lectures:
            raise AssertionError('Invalid lecture number')
        return self.lectures[number-1]

    # все домашки
    def get_homeworks(self):
        return_list = list()
        for i in self.homeworks:
            if self.homeworks.get(i).description is not None:
                return_list.append(self.homeworks.get(i))
        return return_list


class Lecture:
    def __init__(self, name, number, teacher, course_name):
        self.number = number
        self.teacher = teacher
        self.name = name
        self.course_name = course_name

    # номер домашки
    def get_homework(self):
        if self.course_name.homeworks.get(self.number).description is not None:
            return self.course_name.homeworks.get(self.number)
        return None

    # назначить домашку на лекцию
    def set_homework(self, assignment):
        self.course_name.homeworks[self.number] = assignment
        for stud in self.course_name.enrolled:
            stud.assigned_homeworks.append(assignment)

    # добавить преподавателя на лекцию
    def new_teacher(self, new_teacher):
        self.teacher = new_teacher
        self.teacher.all_courses.append(self.course_name)
        self.teacher.all_lectures.append(self)
        self.teacher.lectures.append(self)


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.homeworks_for_check = dict()

    # название домашки+описание
    def __str__(self):
        return f"{self.name}: {self.description}"

    # непроверенные домашки
    def done_by(self):
        return self.homeworks_for_check


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self._last_name = last_name
        self.assigned_homeworks = list()
        self.course = None

    # фио ученика
    def __str__(self):
        return f"Student: {self.first_name} {self._last_name}"

    # зачисление на курс
    def enroll(self, course_name):
        course_name.enrolled.append(self)
        self.course = course_name

    # сделать домашку
    def do_homework(self, task):
        for i in self.assigned_homeworks:
            if i == task:
                task.homeworks_for_check.setdefault(self, None)
                self.course.teacher.homeworks_to_check.append(task)
                self.assigned_homeworks.remove(i)

    # для определения методов в классе , которые действуют как атрибуты
    @property
    def last_name(self):
        return self._last_name


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.all_courses = list()
        self.all_lectures = list()
        self.lectures = list()
        self.homeworks_to_check = list()

    # фио учителя
    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"

    # лекции учителя
    def teaching_lectures(self):
        for element in self.all_courses:
            index = 0
            while index != element.number_of_lectures:
                for i in element.lectures:
                    if i.teacher == self and i not in self.lectures:
                        self.lectures.append(i)

                    elif i.teacher != self and i in self.lectures:

                        self.lectures.remove(i)
                    index += 1
        return self.lectures

    # домашки на проверку
    def check_homework(self, homework, inc_student, grade):
        if 0 > grade > 100:
            raise AssertionError('Invalid mark')
        elif inc_student not in homework.homeworks_for_check:
            raise ValueError('Student never did that homework')
        elif homework.homeworks_for_check[inc_student] is not None:
            raise ValueError('You already checked that homework')
        for i in homework.homeworks_for_check:
            if i == inc_student:
                homework.homeworks_for_check[inc_student] = grade
                self.homeworks_to_check.remove(homework)
        return None


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'

    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures

    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)

    assert python_basic.enrolled_by() == students

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'

    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        assert student.assigned_homeworks == [functions_homework]

    assert main_teacher.homeworks_to_check == []
    students[0].do_homework(functions_homework)
    assert students[0].assigned_homeworks == []
    assert students[1].assigned_homeworks == [functions_homework]

    assert functions_homework.done_by() == {students[0]: None}
    assert main_teacher.homeworks_to_check == [functions_homework]

    for mark in (-1, 101):
        try:
            main_teacher.check_homework(functions_homework, students[0], mark)
        except AssertionError as error:
            assert error.args == ('Invalid mark',)

    main_teacher.check_homework(functions_homework, students[0], 100)
    assert main_teacher.homeworks_to_check == []
    assert functions_homework.done_by() == {students[0]: 100}

    try:
        main_teacher.check_homework(functions_homework, students[0], 100)
    except ValueError as error:
        assert error.args == ('You already checked that homework',)

    try:
        main_teacher.check_homework(functions_homework, students[1], 100)
    except ValueError as error:
        assert error.args == ('Student never did that homework',)

    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher

    fourth_lecture.new_teacher(substitute_teacher)
    assert fourth_lecture.teacher == substitute_teacher
    assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    assert substitute_teacher.homeworks_to_check == []
