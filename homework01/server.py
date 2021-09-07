from flask import Flask
from flask import request

# the dict was obtained by parsing the site https://emojipedia.org/nature/ (emoji_dict.py)

zoo = {'smileys&people': '😃', 'animals&nature': '🐻', 'food&drink': '🍔', 'activity': '⚽', 'travel&places': '🌇', 'objects': '💡', 'symbols': '🔣', 'flags': '🎌', 'see-no-evilmonkey': '🙈', 'hear-no-evilmonkey': '🙉', 'speak-no-evilmonkey': '🙊', 'collision': '💥', 'dizzy': '💫', 'sweatdroplets': '💦', 'dashingaway': '💨', 'monkeyface': '🐵', 'monkey': '🐒', 'gorilla': '🦍', 'orangutan': 'U0001f9a7', 'dogface': '🐶', 'dog': '🐕', 'guidedog': 'U0001f9ae', 'servicedog': '🐕u200dU0001f9ba', 'poodle': '🐩', 'wolf': '🐺', 'fox': '🦊', 'raccoon': '🦝', 'catface': '🐱', 'cat': '🐈', 'blackcat': '🐈u200d⬛', 'lion': '🦁', 'tigerface': '🐯', 'tiger': '🐅', 'leopard': '🐆', 'horseface': '🐴', 'horse': '🐎', 'unicorn': '🦄', 'zebra': '🦓', 'deer': '🦌', 'bison': 'U0001f9ac', 'cowface': '🐮', 'ox': '🐂', 'waterbuffalo': '🐃', 'cow': '🐄', 'pigface': '🐷', 'pig': '🐖', 'boar': '🐗', 'pignose': '🐽', 'ram': '🐏', 'ewe': '🐑', 'goat': '🐐', 'camel': '🐪', 'two-humpcamel': '🐫', 'llama': '🦙', 'giraffe': '🦒', 'elephant': '🐘', 'mammoth': 'U0001f9a3', 'rhinoceros': '🦏', 'hippopotamus': '🦛', 'mouseface': '🐭', 'mouse': '🐁', 'rat': '🐀', 'hamster': '🐹', 'rabbitface': '🐰', 'rabbit': '🐇', 'chipmunk': '🐿️', 'beaver': 'U0001f9ab', 'hedgehog': '🦔', 'bat': '🦇', 'bear': '🐻', 'polarbear': '🐻u200d❄️', 'koala': '🐨', 'panda': '🐼', 'sloth': 'U0001f9a5', 'otter': 'U0001f9a6', 'skunk': 'U0001f9a8', 'kangaroo': '🦘', 'badger': '🦡', 'pawprints': '🐾', 'turkey': '🦃', 'chicken': '🐔', 'rooster': '🐓', 'hatchingchick': '🐣', 'babychick': '🐤', 'front-facingbabychick': '🐥', 'bird': '🐦', 'penguin': '🐧', 'dove': '🕊️', 'eagle': '🦅', 'duck': '🦆', 'swan': '🦢', 'owl': '🦉', 'dodo': 'U0001f9a4', 'feather': 'U0001fab6', 'flamingo': 'U0001f9a9', 'peacock': '🦚', 'parrot': '🦜', 'frog': '🐸', 'crocodile': '🐊', 'turtle': '🐢', 'lizard': '🦎', 'snake': '🐍', 'dragonface': '🐲', 'dragon': '🐉', 'sauropod': '🦕', 't-rex': '🦖', 'spoutingwhale': '🐳', 'whale': '🐋', 'dolphin': '🐬', 'seal': 'U0001f9ad', 'fish': '🐟', 'tropicalfish': '🐠', 'blowfish': '🐡', 'shark': '🦈', 'octopus': '🐙', 'spiralshell': '🐚', 'snail': '🐌', 'butterfly': '🦋', 'bug': '🐛', 'ant': '🐜', 'honeybee': '🐝', 'beetle': 'U0001fab2', 'ladybeetle': '🐞', 'cricket': '🦗', 'cockroach': 'U0001fab3', 'spider': '🕷️', 'spiderweb': '🕸️', 'scorpion': '🦂', 'mosquito': '🦟', 'fly': 'U0001fab0', 'worm': 'U0001fab1', 'microbe': '🦠', 'bouquet': '💐', 'cherryblossom': '🌸', 'whiteflower': '💮', 'rosette': '🏵️', 'rose': '🌹', 'wiltedflower': '🥀', 'hibiscus': '🌺', 'sunflower': '🌻', 'blossom': '🌼', 'tulip': '🌷', 'seedling': '🌱', 'pottedplant': 'U0001fab4', 'evergreentree': '🌲', 'deciduoustree': '🌳', 'palmtree': '🌴', 'cactus': '🌵', 'sheafofrice': '🌾', 'herb': '🌿', 'shamrock': '☘️', 'fourleafclover': '🍀', 'mapleleaf': '🍁', 'fallenleaf': '🍂',
       'leafflutteringinwind': '🍃', 'mushroom': '🍄', 'chestnut': '🌰', 'crab': '🦀', 'lobster': '🦞', 'shrimp': '🦐', 'squid': '🦑', 'globeshowingeurope-africa': '🌍', 'globeshowingamericas': '🌎', 'globeshowingasia-australia': '🌏', 'globewithmeridians': '🌐', 'rock': 'U0001faa8', 'newmoon': '🌑', 'waxingcrescentmoon': '🌒', 'firstquartermoon': '🌓', 'waxinggibbousmoon': '🌔', 'fullmoon': '🌕', 'waninggibbousmoon': '🌖', 'lastquartermoon': '🌗', 'waningcrescentmoon': '🌘', 'crescentmoon': '🌙', 'newmoonface': '🌚', 'firstquartermoonface': '🌛', 'lastquartermoonface': '🌜', 'sun': '☀️', 'fullmoonface': '🌝', 'sunwithface': '🌞', 'star': '⭐', 'glowingstar': '🌟', 'shootingstar': '🌠', 'cloud': '☁️', 'sunbehindcloud': '⛅', 'cloudwithlightningandrain': '⛈️', 'sunbehindsmallcloud': '🌤️', 'sunbehindlargecloud': '🌥️', 'sunbehindraincloud': '🌦️', 'cloudwithrain': '🌧️', 'cloudwithsnow': '🌨️', 'cloudwithlightning': '🌩️', 'tornado': '🌪️', 'fog': '🌫️', 'windface': '🌬️', 'rainbow': '🌈', 'umbrella': '☂️', 'umbrellawithraindrops': '☔', 'highvoltage': '⚡', 'snowflake': '❄️', 'snowman': '☃️', 'snowmanwithoutsnow': '⛄', 'comet': '☄️', 'fire': '🔥', 'droplet': '💧', 'waterwave': '🌊', 'christmastree': '🎄', 'sparkles': '✨', 'tanabatatree': '🎋', 'pinedecoration': '🎍', 'redheart': '❤️', 'pleadingface': '🥺', 'heartonfire': '❤️u200d🔥', 'smilingfacewithsmilingeyes': '😊', 'facewithtearsofjoy': '😂', 'smilingfacewithhearts': '🥰', 'smilingfacewithtear': 'U0001f972', 'samsungoneui3.1.1emojichangelog': '👹', 'facebookemoji13.1changelog': '📖', 'whatabouttheafghanistanflagemoji?': '🇦🇫', 'emojipediajoinszedge': '🌻', 'what’snewonworldemojiday2021': '📅', 'android12emojichangelog': '🤖', 'fasteremojiupdatesonthewayforandroidapps': '⏩', 'skypeemoticonsnowonemojipedia': '💨', 'australiaday': '🇦🇺', 'bastilleday': '🇫🇷', 'birthday': '🎂', 'blackfriday': '🛍️', 'blacklivesmatter': '✊🏿', 'canadaday': '🇨🇦', 'carnaval': '🇧🇷', 'chinesenewyear': '🐉', 'christmas': '🎅', 'cincodemayo': '🇲🇽', 'coronavirus': '🦠', 'diwali': 'U0001fa94', 'dragonboatfestival': '🇨🇳', 'earthday': '🌱', 'easter': '🐰', 'emojimovie': '🎥', 'fallautumn': '🍂', 'father’sday': '👨', 'festivus': '💪', 'fourtwenty420': '🌿', 'graduation': '🎓', 'guyfawkes': '🔥', 'halloween': '🎃', 'hanukkah': '🕎', 'hearts': '💕', 'holi': '🕉️', 'independenceday': '🇺🇸', "internationalwomen'sday": '♀️', 'mother’sday': '🤱', 'newyear’seve': '🎊', 'nsfw': '🔞', 'olympics': '🏊', 'pride': '🏳️u200d🌈', 'purim': '🎭', 'queen’sbirthday': '👑', 'ramadan': '☪️', 'spring': '🌱', 'stpatrick’sday': '☘️', 'summer': '☀️', 'superbowl': '🏈', 'thanksgiving': '🦃', 'valentine’sday': '💘', 'veteransday': '🎖️', 'weddingmarriage': '👰', 'winter': '⛄', 'winterolympics': '🎿', 'workingfromhome': '🏡', 'worldcup': '⚽', 'worldemojiday': '🌎'}


app = Flask(__name__)


def animal_say(animal, sound, count, method):
    say_phrase = ""
    for i in range(int(count)):
        if method == 'POST':
            if animal.lower() in zoo:
                say_phrase = say_phrase + str("{} says {} \n".format(zoo[animal], sound))
            else:
                say_phrase = say_phrase + str("{} says {} \n".format(animal, sound))
        else:
            if animal.lower() in zoo:
                say_phrase = say_phrase + str("<p style='font-size:12pt'><b>{}</b> says {} </p>".format(zoo[animal], sound))                
            else:
                say_phrase = say_phrase + str("<p style='font-size:12pt'><b>{}</b> says {} </p>".format(animal, sound))                

    if method == 'POST':
        say_phrase = say_phrase + "Made with by vacilyok \n"
    else:
        say_phrase = say_phrase + "<p style='font-size:12pt'>Made with by <a href='https://github.com/vacilyok'>vacilyok</a></p>"

    return say_phrase


def incorrectPage():
    html = '''
            <html>
            <body>
            <h1>No data found to display</h1>
            <h2>Exemple data</h2>
            <p>
            <a href='?animal=ram&sound=beeee&count=3'>localhost?animal=ram&sound=beeee&count=3</a>
            </p>

            </body>
            </html>
           '''
    return html


@app.route("/", methods=['GET', 'POST'])
def hello():
    count = 2
    animal = '-'
    sound = '-'
    if request.method == 'POST':
        request_data = request.get_json()
        if request_data == None:
            animal = request.form.get('animal')
            sound = request.form.get('sound')
            count = request.form.get('count')
            if (animal == None or sound == None or count == None):
                return "Incorrect data format"

        else:
            if 'animal' in request_data:
                animal = request_data['animal']
            else:
                return "Incorrect data format. Not found 'animal' key "
            if 'sound' in request_data:
                sound = request_data['sound']
            else:
                return "Incorrect data format. Not found 'sound' key "
            if 'count' in request_data:
                count = request_data['count']
            else:
                return "Incorrect data format. Not found 'count' key "

    if request.method == 'GET':
        animal = request.args.get("animal")
        sound = request.args.get("sound")
        count = request.args.get("count")
        if (animal == None or sound == None or count == None):
            return incorrectPage()

    return animal_say(animal, sound, count, request.method)


if __name__ == "__main__":
    from waitress import serve
    serve(app, port=80)
    # app.run()
