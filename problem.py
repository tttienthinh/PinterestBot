problem = ['2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12',
           '2020-01-13',
           '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-21',
           '2020-01-22',
           '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29',
           '2020-01-30',
           '2020-01-31', '2020-02-01', '2020-02-02', '2020-02-03', '2020-02-04', '2020-02-05', '2020-02-06',
           '2020-02-07',
           '2020-02-08', '2020-02-10', '2020-02-11', '2020-02-12', '2020-02-13', '2020-02-14', '2020-02-15',
           '2020-02-16',
           '2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22', '2020-02-23',
           '2020-02-24',
           '2020-02-25', '2020-02-28', '2020-02-29', '2020-03-01', '2020-03-02', '2020-03-03', '2020-03-06',
           '2020-03-07',
           '2020-03-08', '2020-03-09', '2020-03-10', '2020-03-11', '2020-03-12', '2020-03-13', '2020-03-14',
           '2020-03-15',
           '2020-03-18', '2020-03-19', '2020-03-20', '2020-03-21', '2020-03-22', '2020-03-24', '2020-03-25',
           '2020-03-26',
           '2020-03-27', '2020-03-28', '2020-03-29', '2020-03-30', '2020-03-31', '2020-04-01', '2020-04-02',
           '2020-04-03',
           '2020-04-04', '2020-04-05', '2020-04-06', '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-10',
           '2020-04-11',
           '2020-04-12', '2020-04-13', '2020-04-14', '2020-04-15', '2020-04-16', '2020-04-17', '2020-04-18',
           '2020-04-19',
           '2020-04-20', '2020-04-21', '2020-04-22', '2020-04-23', '2020-04-24', '2020-04-27', '2020-04-28',
           '2020-04-29',
           '2020-04-30', '2020-05-01', '2020-05-02', '']

import requests
import datetime
import sys
from time import sleep
from py3pin.Pinterest import Pinterest
from PIL import Image, ImageDraw, ImageFont

pinterest = Pinterest(email='journaldespace@gmail.com',
                      password='iee!NICE150402',
                      username='journaldespace')
try:
    pinterest.login()
except:
    print("Pas besoin de connection.")

journaldespace_url = 'https://imobinfo.com/Actualites.html'

nasa = 'https://api.nasa.gov/planetary/apod'
nasa_params = {
    'api_key': 'IqWPpNh7NbhokTuyrrkaJqjXXXHkShByHQ5uta7h',
}
yandex = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
yandex_params = {
    'key': 'trnsl.1.1.20200425T200440Z.7d571882c8635b32.294ccd14fcf7788229ebe858e87a212d4f8541ff',
    'lang': 'en-fr'
}

# test tienthinht
# board_id = '672303119313037233'
# test
# board_id = '637400222200883386'
# real One
board_id = '637400222200883506'

liste_annees = {
    "1995": "5096321339294266083",
    "1996": "5096323943669745531",
    "1997": "5096323945102103361",
    "1998": "5096323945875944025",
    "1999": "5096323945875944697",
    "2000": "5096323946081472167",
    "2001": "5096323947497044773",
    "2002": "5096323947899702396",
    "2003": "5096323949283815580",
    "2004": "5096323949573229522",
    "2005": "5096323950921693198",
    "2006": "5096323951880097856",
    "2007": "5096323950921695135",
    "2008": "5096323952651844309",
    "2009": "5096323953828348615",
    "2010": "5096323954327468861",
    "2011": "5096323955283775841",
    "2012": "5096323956141502560",
    "2013": "5096323955283777356",
    "2014": "5096323956141504341",
    "2015": "5096323957303330130",
    "2016": "5096323957947147522",
    "2017": "5096323958708425764",
    "2018": "5096323959062840759",
    "2019": "5096323959723435447",
    "2020": "5096323961436811426"
}
# 2020 12 31 1800 1 8961
arg = sys.argv
if len(arg) > 1:
    name = arg[0]
    today = datetime.date(int(arg[1]), int(arg[2]), int(arg[3]))
    wait = int(arg[4])
    nombre = int(arg[5])
else:
    today = datetime.date(2020, 1, 1)
    wait = 0
    nombre = 125


def ModifImage():
    image = Image.open('image')
    marge = image.size[0] / 25
    font_size = int(image.size[0] / 25)
    text = "Clique pour voir l'original !"

    draw = ImageDraw.Draw(image)
    font_type = ImageFont.truetype('AccanthisADFStdNo3-Bold.otf', font_size)
    text_x, text_y = font_type.getsize(text)

    draw.rectangle((0, 0, marge * 2 + text_x, marge * 2 + text_y), fill=(0, 128, 255))
    draw.text(xy=(marge, marge), text=text, fill=(255, 255, 255), font=font_type)

    image.save("sortie.jpg", 'JPEG')


def erreur(date, error):
    print(error)
    with open(f"logs/{date.strftime('%Y')}", '+a') as file:
        file.write(date.strftime('%Y-%m-%d'))
        file.write(f"\n{error}")
        file.write('\n\n\n')


def post(date):
    str_date = date.strftime('%Y-%m-%d')
    print(str_date)

    nasa_params['date'] = str_date
    nasa_r = requests.get(nasa, nasa_params)
    nasa_result = nasa_r.json()

    yandex_params['text'] = nasa_result['title']
    yandex_r = requests.get(yandex, yandex_params)

    if yandex_r.ok:
        yandex_result = yandex_r.json()
        title = yandex_result['text']
    else:
        title = nasa_result['title']
    try:
        url = nasa_result['hdurl']
    except:
        print('Got to take URL instead of HDURL')
        url = nasa_result['url']

    image_r = requests.get(url, allow_redirects=True)
    format_fichier = image_r.headers.get('content-type').split('/')
    if format_fichier[0] == 'image':
        link = f'{journaldespace_url}?date={str_date}'
        try:
            explanation = f"{str_date} - De la NASA écrit par {nasa_result['copyright']}. Pour plus d'information, clique sur la photo."
        except:
            explanation = f"{str_date} - De la NASA. Pour plus d'information, clique sur la photo."
        open('image', 'wb').write(image_r.content)
        ModifImage()
        section_id = liste_annees[date.strftime('%Y')]
        pinterest.upload_pin(board_id, 'sortie.jpg', description=explanation,
                             link=link, title=title, section_id=section_id)
    else:
        erreur(date, sys.exc_info()[0])


for i in range(len(problem)):
    y, m, d = problem[i].split("-")
    date = datetime.date(y, m, d)
    all_try = 3
    for trying in range(all_try):
        try:
            post(date)
            sleep(wait)
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            if trying == all_try-1:
                erreur(date, sys.exc_info()[0])
                break
            else:
                sleep(3600)
                continue
