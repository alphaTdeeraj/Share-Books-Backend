def branchChoices():
    branches = [
        ('Mechanical', 'Mechanical'),
        ('Computer Science', 'Computer Science'),
        ('Information science', 'Information science'),
        ('Electrical', 'Electrical'),
        ('Civil', 'Civil'),
        ('Biotechnology', 'Biotechnology'),
        ('Chemical', 'Chemical'),
        ('Electronics and Communication', 'Electronics and Communication'),
        ('Industrial and Management', 'Industrial and Management'),
        ('Medical Electronics', 'Medical Electronics'),
        ('All', 'All'),
    ]

    return branches


def yearChoice():
    semester = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),


    ]
    return semester


def imageUpload(instance, filename):
    branch = instance.branch
    semester = instance.semester
    img_path = f'{branch}/{semester}/{filename}'
    return img_path



def updateBook(instance, new_data):
    instance.author = new_data.get('author')
    instance.available = new_data.get('available')
    instance.book_name = new_data.get('book_name')
    instance.branch = new_data.get('branch')
    instance.semester = new_data.get('semester')
    instance.cost = new_data.get('cost')
    instance.save()
    return 
