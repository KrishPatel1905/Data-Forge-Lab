def marks(**kwargs):
    for item in kwargs.keys():
        print(f"{item} marks is {kwargs[item]}")
    
marks(krish=90,heet=85,jack=78)