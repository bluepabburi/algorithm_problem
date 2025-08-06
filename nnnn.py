class Note(object):
    def __init__(self, note = 0):
        self.note = note

    def writing_note(self, note):
        self.note = note
    
    def erase_note(self):
        self.note = ''

    def __str__(self):
        return '노트에 적힌 내용입니다: %s' .format('self.note')

class NoteBook(object):
    
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def insert_note(self, note):
        if self.page_number < 300:
            if self.page_number == 0:
                self.notes[self.page_number] = note
                self.page_number += 1

            else:
                self.notes[self.page_number] = note

        else:
            print('페이지가 가득 찼습니다')


    def erase_notebook(self):
        if self.page_number in self.notes.keys():
            return self.notes.pop()
        
    def get_number_page(self):
        return len(self.notes.keys)

My_notes = NoteBook('My_note')
note1 = Note('안녕하세요')

My_notes.insert_note(note1)
note1
print(My_notes)