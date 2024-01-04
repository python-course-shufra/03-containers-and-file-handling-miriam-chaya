classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    if(email==None):
        lowName=""
        for s in name:
            lowName+=s.lower()
        email=lowName+'@example.com'
    classroom.append({'name':name,'email':email,'grades':[]})


def delete_student(name):
    for student in classroom:
        if student['name']==name:
            student.clear()



def set_email(name, email):
    for student in classroom:
        if student['name']==name:
            student['email']=email


def add_grade(name, profession, grade):
    for student in classroom:
        if student['name']==name:
            student['grades']+=((profession,grade),)



def avg_grade(name, profession):
    pass


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    pass
