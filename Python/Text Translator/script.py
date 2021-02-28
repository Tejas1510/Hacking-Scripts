### text translator in python ###
from textblob import TextBlob


def Translate():
    Lang = [
        'Hindi', 'Bengali', 'Tamil', 'Telugu', 'Malayalam', 'Marathi',
        'Gujarati'
    ]
    for i in range(len(Lang)):
        print("Press " + str(i) + " for " + Lang[i])
    lang_list = {
        Lang[0]: 'hi',
        Lang[1]: 'bn',
        Lang[2]: 'ta',
        Lang[3]: 'te',
        Lang[4]: 'ml',
        Lang[5]: 'mr',
        Lang[6]: 'gu'
    }
    Target_lang = int(input())
    text = open("textfiles/input.txt", "r")
    content = TextBlob(text.read())
    final = content.translate(to=lang_list[Lang[Target_lang]])
    translation = open("textfiles/output.txt", 'w', encoding="utf-8")
    # print(str(final))
    translation.write(str(final))
    text.close()
    translation.close()


if __name__ == "__main__":
    Translate()
