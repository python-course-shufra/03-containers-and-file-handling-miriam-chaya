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
def index_of_student(name):
    for i in range(len(classroom)) :
        if classroom[i]['name']==name:
            return i



def add_student(name, email=None):
    if email is None:
        email=name.lower()+'@example.com'
    classroom.append({'name':name,'email':email,'grades':[]})
    

def delete_student(name):
    del classroom[index_of_student(name)]



def set_email(name, email):
    classroom[index_of_student(name)]['email']==email


def add_grade(name, profession, grade):
    classroom[index_of_student(name)]['grades']+=((profession,grade),)
    

def avg_grade(name, profession):
    count=0
    sum=0
    s=classroom[index_of_student(name)]
    for sub,grade in classroom[s]['grades']:
        if (sub==profession):
            count+=1
            sum+=grade
        return sum/count

                


def get_professions(name):
    professions=[]
    s=classroom[index_of_student(name)]
    professions=[sub for sub,grade in classroom[s]['grades']]
    for p in professions:
        for sub in professions:
            if(professions[p]==professions[sub]&p!=sub):
                professions[sub].clear()
    return professions
    


            
