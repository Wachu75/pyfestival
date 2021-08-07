
class Person:
    def __init__(self, first_name: str, sure_name: str):
        self.first_name = first_name
        self.sure_name = sure_name

    @classmethod
    def from_row(cls, data: str):
        #person = cls(data)
        first_name, sure_name = data.strip().split(';')
        return cls(first_name, sure_name)


p = Person('asdf','eeeee')
print(p.sure_name)
print(p.first_name)

q = Person.from_row('aaaaa;sssss')
print(q.first_name)
print(q.sure_name)