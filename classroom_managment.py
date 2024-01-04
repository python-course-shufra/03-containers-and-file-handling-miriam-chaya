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
    """Delete a student from the classroom"""
    pass


def set_email(name, email):
    """Sets the email of the student"""
    pass


def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    pass


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    pass


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    pass
