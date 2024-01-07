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
    return

def delete_student(name):
    for student in classroom:
        if student['name']==name:
            student.clear()
        return 



def set_email(name, email):
    for student in classroom:
        if student['name']==name:
            student['email']=email
        return 


def add_grade(name, profession, grade):
    for student in classroom:
        if student['name']==name:
            student['grades']+=((profession,grade),)
        return 



def avg_grade(name, profession):
    count=0
    sum=0
    for student in classroom:
        if(student['name']==name):
            for sub,grade in student['grades']:
                if (sub==profession):
                    count+=1
                    sum+=grade
            return sum/count

                


def get_professions(name):
    professions=[]
    for student in classroom:
        if(student['name']==name):
            professions=[sub for sub,grade in student['grades']]
        for p in professions:
            for sub in professions:
                if(professions[p]==professions[sub]&p!=sub):
                    professions[sub].clear()
        return professions
    return None


            
