'''
假設你想要紀錄一些學生的成績，但事先並不知道他們的姓名。
你可以定義一個類別來將那些名字儲存在一個字典中，而非為每個學生使用一個預先定義的屬性
'''
class SimpleGradebook(object):
    def __init__(self):
        self._grades={}

    def add_student(self, name):
        self._grades[name]=[]

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        # print(grades)
        return sum(grades) / len(grades)

book = SimpleGradebook()

book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)

print(book.average_grade('Isaac Newton'))

print('--------------------------------------------------------------')

'''
假設你想要擴充SimpleGradebook類別，讓他維護一個串列來記錄以科目區分的成績，
而非只有整體成績。你可以修改_grades字典來將學生姓名(也就是鍵值)映射到另一個字典中(存放那些值)。
最內層的字典會將科目(鍵值)映射到成績(值)
'''

class BySubjectGradebook(object):
    def __init__(self):
        self._grades={}
    
    def add_student(self, name):
        self._grades[name]={}
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        print(type(by_subject))
        grade_list = by_subject.setdefault(subject, [])
        # setdefault前面必須是個字典，後面的參數(key,default)，key是找尋的鍵值，defult是當鍵值不存在時，設定的默認鍵值
        print(type(grade_list))
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))
