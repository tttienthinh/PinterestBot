from py3pin.Pinterest import Pinterest

pinterest = Pinterest(email='journaldespace@gmail.com',
                      password='iee!NICE150402',
                      username='journaldespace')

print(pinterest.login())

def create_board_section(board_id='', section_name=''):
    return pinterest.create_board_section(board_id=board_id, section_name=section_name)

board_id = '637400222200883506'
for i in range(1996, 2021):
    date = str(i)
    create_board_section(board_id, date)