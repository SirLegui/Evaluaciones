import random

class Student:
    def __init__(self, name, email, id_, phone):
        self.name = name
        self.email = email
        self.id_ = id_
        self.phone = phone

    def toXml(self):
        return '<student name="{}" email="{}@gmail.com" id="{}" phone="{}" />'.format(
            self.name, self.email, self.id_, self.phone)

class StudentGenerator:
    def __init__(self, syl):
        self.nextId = 20180016
        self.syl = syl

    def genSyl(self):
        return random.choice(self.syl)

    def genName(self):
        n = random.randint(2, 4)

        name = ""

        for i in range(n):
            name += self.genSyl()

        return name[0].upper() + name[1:]

    def genEmail(self, name):
        return (name + "{}").format(random.randint(55, 99))

    def genFullName(self):
        return self.genName() + " " + self.genName()

    def genId(self):
        temp = self.nextId
        self.nextId += 1
        return temp

    def genStudent(self):
        name = self.genFullName()
        return Student(name, self.genEmail(name), self.genId(), self.genPhone())

    def genPhone(self):
        return random.randint(22000000, 88999999)

def genSyllables(consonants, vowels, loners):
    syls = []

    for c in consonants:
        for v in vowels:
            syls.append(c + v)

    for l in loners:
        syls.append(l)
    
    return syls

def main(args):
    consonants = "bcdfghjklmnpqrstvwxyz"
    loners = "aosrnml"
    vowels = "aeiouy"
    syl = genSyllables(consonants, vowels, loners)
    g = StudentGenerator(syl)

    for i in range(80):
        s = g.genStudent()
        print(s.toXml())

if __name__ == "__main__":
    import sys
    main(sys.argv)

