class Note(object):
    
    def __init__(self, content = None):
        self.content = content

    def write_content(self, content):
        self.content = content

    def remove_content(self):
        self.content = " "

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content
    

class NoteBook(object):

    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1

            else:
                self.notes = {page : note}
                self.page_number +=1

        else:
            print('page가 가득 찼습니다.')

    
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print('해당 페이지가 존재하지 않습니다.')

    
    def get_number_note_page(self):
        return len(self.notes.keys())
    

n = Note()

NB = NoteBook('test')
new_note = Note('안녕하세요')
NB.add_note(new_note)

a = NB.get_number_note_page()
print(a)
