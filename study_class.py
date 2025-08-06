# b = {'2' : '이해'}

# print('안녕 %s' % (b))

# class ex(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def prt(self):
#         print('당신의 이름은:', self.name, '당신의 나이는:' , self.age)
        
#     def __str__(self):
#         return '테스트에요'


# n = ex('dohyun', '20')

def tag_func(tag, text):
    text = text
    tag = tag  
    def inner_func():
        return '<{0}>{1}<{0}>'.format(tag, text) 
    
    return inner_func

h1_func = tag_func('title', "This is Python Class")  
p_func = tag_func('p', "Data Academy") 

print(h1_func)