import requests
import datetime
import sys
from time import sleep
from py3pin.Pinterest import Pinterest
from PIL import Image, ImageDraw, ImageFont

pinterest = Pinterest(email='journaldespace@gmail.com',
                      password='',
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


for i in range(nombre):
    date = today + datetime.timedelta(days=i)
<<<<<<< HEAD
    try:
        post(date)
        sleep(wait)
    except KeyboardInterrupt:
        sys.exit()
    except:
        erreur(date, sys.exc_info()[0])
=======
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
>>>>>>> first commit
