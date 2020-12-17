"""
Code to accompany the research paper "Neural Machine 
Translation for Amharic-English Translation".

Code copyright (c) 2021 by Andargachew Mekonnen Gezmu

You are free to use this code under the MIT licencse: 
http://www.opensource.org/licenses/mit-license.php
"""

from string import punctuation


VOWELS = 'aeiouə'
EPI = 'ɨ'
CONSONANTS = 'bcċdfghjklmnñpṗqrsšṣtṭvwyzž'
NUMERALS = '፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼'


ethiopic_latin_table = {
    'ሀ':'ha', 'ሁ':'hu', 'ሂ':'hi', 'ሃ':'ha', 'ሄ':'he', 'ህ':'h', 'ሆ':'ho',
    'ሇ':'ho',
    'ለ':'lə', 'ሉ':'lu', 'ሊ':'li', 'ላ':'la', 'ሌ':'le', 'ል':'l', 'ሎ':'lo',
    'ሏ':'lʷa',
    'ሐ':'ha', 'ሑ':'hu', 'ሒ':'hi', 'ሓ':'ha', 'ሔ':'he', 'ሕ':'h', 'ሖ':'ho',
    'ሗ':'hʷa',
    'መ':'mə', 'ሙ':'mu', 'ሚ':'mi', 'ማ':'ma', 'ሜ':'me', 'ም':'m', 'ሞ':'mo',
    'ሟ':'mʷa', 'ፙ':'mʷa',
    'ሠ':'sə', 'ሡ':'su', 'ሢ':'si', 'ሣ':'sa', 'ሤ':'se', 'ሥ':'s', 'ሦ':'so',
    'ሧ':'sʷa',
    'ረ':'rə', 'ሩ':'ru', 'ሪ':'ri', 'ራ':'ra', 'ሬ':'re', 'ር':'r', 'ሮ':'ro',
    'ሯ':'rʷa', 'ፘ':'rʷa',
    'ሰ':'sə', 'ሱ':'su', 'ሲ':'si', 'ሳ':'sa', 'ሴ':'se', 'ስ':'s', 'ሶ':'so',
    'ሷ':'sʷa',
    'ሸ':'šə', 'ሹ':'šu', 'ሺ':'ši', 'ሻ':'ša', 'ሼ':'še', 'ሽ':'š', 'ሾ':'šo',
    'ሿ':'šʷa',
    'ቀ':'qə', 'ቁ':'qu', 'ቂ':'qi', 'ቃ':'qa', 'ቄ':'qe', 'ቅ':'q', 'ቆ':'qo',
    'ቈ':'qo', 'ቊ':'qu', 'ቋ':'qʷa', 'ቌ':'qʷa', 'ቍ':'qu', 'ቇ':'qo',
    'ቐ':'qə', 'ቑ':'qu', 'ቒ':'qi', 'ቓ':'qa', 'ቔ':'qe', 'ቕ':'q', 'ቖ':'qo',
    'ቘ':'qo', 'ቚ':'qu', 'ቛ':'qʷa', 'ቜ':'qʷa', 'ቝ':'qu',
    'በ':'bə', 'ቡ':'bu', 'ቢ':'bi', 'ባ':'ba', 'ቤ':'be', 'ብ':'b', 'ቦ':'bo',
    'ቧ':'bʷa',
    'ቨ':'və', 'ቩ':'vu', 'ቪ':'vi', 'ቫ':'va', 'ቬ':'ve', 'ቭ':'v', 'ቮ':'vo',
    'ቯ':'vʷa',
    'ተ':'tə', 'ቱ':'tu', 'ቲ':'ti', 'ታ':'ta', 'ቴ':'te', 'ት':'t', 'ቶ':'to',
    'ቷ':'tʷa',
    'ቸ':'cə', 'ቹ':'cu', 'ቺ':'ci', 'ቻ':'ca', 'ቼ':'ce', 'ች':'c', 'ቾ':'co',
    'ቿ':'cʷa',
    'ኀ':'ha', 'ኁ':'hu', 'ኂ':'hi', 'ኃ':'ha', 'ኄ':'he', 'ኅ':'h', 'ኆ':'ho',
    'ኇ':'ho', 'ኈ':'ho', 'ኊ':'hu', 'ኋ':'hʷa', 'ኌ':'hʷa', 'ኍ':'hu',
    'ነ':'nə', 'ኑ':'nu', 'ኒ':'ni', 'ና':'na', 'ኔ':'ne', 'ን':'n', 'ኖ':'no',
    'ኗ':'nʷa',
    'ኘ':'ñə', 'ኙ':'ñu', 'ኚ':'ñi', 'ኛ':'ña', 'ኜ':'ñe', 'ኝ':'ñ', 'ኞ':'ño',
    'ኟ':'ñʷa',
    'አ':'a', 'ኡ':'u', 'ኢ':'i', 'ኣ':'a', 'ኤ':'e', 'እ':'ɨ', 'ኦ':'o',
    'ኧ':'ə',
    'ከ':'kə', 'ኩ':'ku', 'ኪ':'ki', 'ካ':'ka', 'ኬ':'ke', 'ክ':'k', 'ኮ':'ko',
    'ኯ':'ko', 'ኰ':'ko', 'ኲ':'ku', 'ኳ':'kʷa', 'ኴ':'kʷa', 'ኵ':'ku',
    'ኸ':'hə', 'ኹ':'hu', 'ኺ':'hi', 'ኻ':'ha', 'ኼ':'he', 'ኽ':'h', 'ኾ':'ho',
    'ዀ':'ho', 'ዂ':'hu', 'ዃ':'hʷa', 'ዄ':'hʷa', 'ዅ':'hu',
    'ወ':'wə', 'ዉ':'wu', 'ዊ':'wi', 'ዋ':'wa', 'ዌ':'we', 'ው':'w', 'ዎ':'wo',
    'ዏ':'wo',
    'ዐ':'a', 'ዑ':'u', 'ዒ':'i', 'ዓ':'a', 'ዔ':'e', 'ዕ':'ɨ', 'ዖ':'o',
    'ዘ':'zə', 'ዙ':'zu', 'ዚ':'zi', 'ዛ':'za', 'ዜ':'ze', 'ዝ':'z', 'ዞ':'zo',
    'ዟ':'zʷa',
    'ዠ':'žə', 'ዡ':'žu', 'ዢ':'ži', 'ዣ':'ža', 'ዤ':'že', 'ዥ':'ž', 'ዦ':'žo',
    'ዧ':'žʷa',
    'የ':'yə', 'ዩ':'yu', 'ዪ':'yi', 'ያ':'ya', 'ዬ':'ye', 'ይ':'y', 'ዮ':'yo',
    'ዯ':'yo',
    'ዸ':'ṗə', 'ዹ':'ṗu', 'ዺ':'ṗi', 'ዻ':'ṗa', 'ዼ':'ṗe', 'ዽ':'ṗ', 'ዾ':'ṗo',
    'ዿ':'ṗʷa',
    'ደ':'də', 'ዱ':'du', 'ዲ':'di', 'ዳ':'da', 'ዴ':'de', 'ድ':'d', 'ዶ':'do',
    'ዷ':'dʷa',
    'ጀ':'jə', 'ጁ':'ju', 'ጂ':'ji', 'ጃ':'ja', 'ጄ':'je', 'ጅ':'j', 'ጆ':'jo',
    'ጇ':'jʷa',
    'ገ':'gə', 'ጉ':'gu', 'ጊ':'gi', 'ጋ':'ga', 'ጌ':'ge', 'ግ':'g', 'ጎ':'go',
    'ጏ':'go', 'ጐ':'go', 'ጒ':'gu', 'ጓ':'gʷa', 'ጔ':'gʷa', 'ጕ':'gu',
    'ጘ':'gə', 'ጙ':'gu', 'ጚ':'gi', 'ጛ':'ga', 'ጜ':'ge', 'ጝ':'g', 'ጞ':'go',
    'ጟ':'gʷa',
    'ጠ':'ṭə', 'ጡ':'ṭu', 'ጢ':'ṭi', 'ጣ':'ṭa', 'ጤ':'ṭe', 'ጥ':'ṭ', 'ጦ':'ṭo',
    'ጧ':'ṭʷa',
    'ጨ':'ċə', 'ጩ':'ċu', 'ጪ':'ċi', 'ጫ':'ċa', 'ጬ':'ċe', 'ጭ':'ċ', 'ጮ':'ċo',
    'ጯ':'ċʷa',
    'ጰ':'ṗə', 'ጱ':'ṗu', 'ጲ':'ṗi', 'ጳ':'ṗa', 'ጴ':'ṗe', 'ጵ':'ṗ', 'ጶ':'ṗo',
    'ጷ':'ṗʷa',
    'ጸ':'ṣə', 'ጹ':'ṣu', 'ጺ':'ṣi', 'ጻ':'ṣa', 'ጼ':'ṣe', 'ጽ':'ṣ', 'ጾ':'ṣo',
    'ጿ':'ṣʷa',
    'ፀ':'ṣə', 'ፁ':'ṣu', 'ፂ':'ṣi', 'ፃ':'ṣa', 'ፄ':'ṣe', 'ፅ':'ṣ', 'ፆ':'ṣo',
    'ፇ':'ṣo',
    'ፈ':'fə', 'ፉ':'fu', 'ፊ':'fi', 'ፋ':'fa', 'ፌ':'fe', 'ፍ':'f', 'ፎ':'fo',
    'ፏ':'fʷa', 'ፚ':'fʷa',
    'ፐ':'pə', 'ፑ':'pu', 'ፒ':'pi', 'ፓ':'pa', 'ፔ':'pe', 'ፕ':'p', 'ፖ':'po',
    'ፗ':'pʷa',
    '፩':'1', '፪':'2', '፫':'3', '፬':'4', '፭':'5', '፮':'6', '፯':'7', '፰':'8',
    '፱':'9', '፲':'10', '፳':'20', '፴':'30', '፵':'40', '፶':'50', '፷':'60', 
    '፸':'70', '፹':'80', '፺':'90', '፻':'100', '፼':'10000',
    '።':'.', '፣':',', '፥':':', '፤':';', '፦':'-', '፡':' ', '፧':'?',
    '«':'"', '»':'"', "‹":"'", "›":"'"}


latin_ethiopic_table = {
    'hə':'ኸ', 'hu':'ሁ', 'hi':'ሂ', 'ha':'ሃ', 'he':'ሄ', 'h':'ህ', 'ho':'ሆ', 'hʷa':'ኋ',
    'lə':'ለ', 'lu':'ሉ', 'li':'ሊ', 'la':'ላ', 'le':'ሌ', 'l':'ል', 'lo':'ሎ', 'lʷa':'ሏ',
    'mə':'መ', 'mu':'ሙ', 'mi':'ሚ', 'ma':'ማ', 'me':'ሜ', 'm':'ም', 'mo':'ሞ', 'mʷa':'ሟ',
    'rə':'ረ', 'ru':'ሩ', 'ri':'ሪ', 'ra':'ራ', 're':'ሬ', 'r':'ር', 'ro':'ሮ', 'rʷa':'ሯ',
    'sə':'ሰ', 'su':'ሱ', 'si':'ሲ', 'sa':'ሳ', 'se':'ሴ', 's':'ስ', 'so':'ሶ', 'sʷa':'ሷ',
    'šə':'ሸ', 'šu':'ሹ', 'ši':'ሺ', 'ša':'ሻ', 'še':'ሼ', 'š':'ሽ', 'šo':'ሾ', 'šʷa':'ሿ',
    'qə':'ቀ', 'qu':'ቁ', 'qi':'ቂ', 'qa':'ቃ', 'qe':'ቄ', 'q':'ቅ', 'qo':'ቆ', 'qʷa':'ቋ',
    'bə':'በ', 'bu':'ቡ', 'bi':'ቢ', 'ba':'ባ', 'be':'ቤ', 'b':'ብ', 'bo':'ቦ', 'bʷa':'ቧ',
    'və':'ቨ', 'vu':'ቩ', 'vi':'ቪ', 'va':'ቫ', 've':'ቬ', 'v':'ቭ', 'vo':'ቮ', 'vʷa':'ቯ',
    'tə':'ተ', 'tu':'ቱ', 'ti':'ቲ', 'ta':'ታ', 'te':'ቴ', 't':'ት', 'to':'ቶ', 'tʷa':'ቷ',
    'cə':'ቸ', 'cu':'ቹ', 'ci':'ቺ', 'ca':'ቻ', 'ce':'ቼ', 'c':'ች', 'co':'ቾ', 'cʷa':'ቿ',
    'nə':'ነ', 'nu':'ኑ', 'ni':'ኒ', 'na':'ና', 'ne':'ኔ', 'n':'ን', 'no':'ኖ', 'nʷa':'ኗ',
    'ñə':'ኘ', 'ñu':'ኙ', 'ñi':'ኚ', 'ña':'ኛ', 'ñe':'ኜ', 'ñ':'ኝ', 'ño':'ኞ', 'ñʷa':'ኟ',
    'a':'አ', 'u':'ኡ', 'i':'ኢ', 'e':'ኤ', 'ɨ':'እ', 'o':'ኦ', 'ə':'ኧ',
    'kə':'ከ', 'ku':'ኩ', 'ki':'ኪ', 'ka':'ካ', 'ke':'ኬ', 'k':'ክ', 'ko':'ኮ', 'kʷa':'ኳ',
    'wə':'ወ', 'wu':'ዉ', 'wi':'ዊ', 'wa':'ዋ', 'we':'ዌ', 'w':'ው', 'wo':'ዎ',
    'zə':'ዘ', 'zu':'ዙ', 'zi':'ዚ', 'za':'ዛ', 'ze':'ዜ', 'z':'ዝ', 'zo':'ዞ', 'zʷa':'ዟ',
    'žə':'ዠ', 'žu':'ዡ', 'ži':'ዢ', 'ža':'ዣ', 'že':'ዤ', 'ž':'ዥ', 'žo':'ዦ', 'žʷa':'ዧ',
    'yə':'የ', 'yu':'ዩ', 'yi':'ዪ', 'ya':'ያ', 'ye':'ዬ', 'y':'ይ', 'yo':'ዮ',
    'də':'ደ', 'du':'ዱ', 'di':'ዲ', 'da':'ዳ', 'de':'ዴ', 'd':'ድ', 'do':'ዶ', 'dʷa':'ዷ',
    'jə':'ጀ', 'ju':'ጁ', 'ji':'ጂ', 'ja':'ጃ', 'je':'ጄ', 'j':'ጅ', 'jo':'ጆ', 'jʷa':'ጇ',
    'gə':'ገ', 'gu':'ጉ', 'gi':'ጊ', 'ga':'ጋ', 'ge':'ጌ', 'g':'ግ', 'go':'ጎ', 'gʷa':'ጓ',
    'ṭə':'ጠ', 'ṭu':'ጡ', 'ṭi':'ጢ', 'ṭa':'ጣ', 'ṭe':'ጤ', 'ṭ':'ጥ', 'ṭo':'ጦ', 'ṭʷa':'ጧ',
    'ċə':'ጨ', 'ċu':'ጩ', 'ċi':'ጪ', 'ċa':'ጫ', 'ċe':'ጬ', 'ċ':'ጭ', 'ċo':'ጮ', 'ċʷa':'ጯ',
    'ṗə':'ጰ', 'ṗu':'ጱ', 'ṗi':'ጲ', 'ṗa':'ጳ', 'ṗe':'ጴ', 'ṗ':'ጵ', 'ṗo':'ጶ', 'ṗʷa':'ጷ',
    'ṣə':'ፀ', 'ṣu':'ፁ', 'ṣi':'ፂ', 'ṣa':'ፃ', 'ṣe':'ፄ', 'ṣ':'ፅ', 'ṣo':'ፆ', 'ṣʷa':'ጿ',
    'fə':'ፈ', 'fu':'ፉ', 'fi':'ፊ', 'fa':'ፋ', 'fe':'ፌ', 'f':'ፍ', 'fo':'ፎ', 'fʷa':'ፏ',
    'pə':'ፐ', 'pu':'ፑ', 'pi':'ፒ', 'pa':'ፓ', 'pe':'ፔ', 'p':'ፕ', 'po':'ፖ', 'pʷa':'ፗ',
    '.':'።', ',':'፣', ';':'፤', '-':'፦', '{':'{', '}':'}', '!':'!', '"':'"', "'":"'",
    '#':'#', '$':'$', '%':'%', '&':'&', '(':'(', ')':')', '*':'*', '+':'+', '/':'/',
    ':':'፥', '<':'<', '=':'=', '>':'>', '?':'?', '@':'@', '[':'[', '\\':'\\', ']':']',
    '^':'^', '_':'_', '`':'`', '|':'|', '~':'~', '0':'0', '1':'1', '2':'2','3':'3',
    '4':'4', '5':'5', '6':'6', '7':'7', '8':'8','9':'9'
}


def is_ethiopic_num(number):
    for digit in number:
        if digit not in NUMERALS:
            return False
    return True


def ethionum2arabicnum(number):
    """Converts an Ethiopic numeral into an Arabic numeral."""
    if len(number) == 1:
        return ethiopic_latin_table[number]
    result = 0
    for digit in number:
        if (digit == '፻') or (digit == '፼'):  # ፻ is equivalent to 100 and ፼ is equivalent to 10,000
            result *= 100
        else:
            result += int(ethiopic_latin_table[digit])
    return result


def ethiopic2latin(token):
    """Converts an Amharic token into Latin."""
    if token.isnumeric():
        if is_ethiopic_num(token):
            return ethionum2arabicnum(token)
        else:
            return token
    result = ''
    for c in token:
        # from 1200 to 135A (for letters) or 1361 to 1367 (for punctuation) in Unicode character code table
        if (4608 <= ord(c) <= 4954) or (4961 <= ord(c) <= 4967) or (c in NUMERALS):
            result += ethiopic_latin_table[c]
        else:
            result += c
    return result


def latin2ethiopic(token):
    """Converts a Latin token into Amharic."""
    if token.replace(',', '').replace('.', '').isnumeric():
        return token
    if len(token) == 1:
        try:
            return latin_ethiopic_table[token]
        except:
            return token
    result = ''
    index = 0
    length = len(token) - 1
    while index < length:
        if token[index] in CONSONANTS:
            if token[index+1] in VOWELS:
                result += latin_ethiopic_table[token[index:index+2]]
                index += 2
            elif token[index+1] == 'ʷ':
                result += latin_ethiopic_table[token[index:index+3]]
                index += 3
            else:
                result += latin_ethiopic_table[token[index]]
                index += 1
        elif (token[index] in VOWELS) or (token[index] in EPI):
            result += latin_ethiopic_table[token[index]]
            index += 1
        else:
            result += token[index]
            index += 1
    if (token[-1] in CONSONANTS) or (token[-1] in EPI) or (token[-1] in punctuation):
        result += latin_ethiopic_table[token[-1]]
    return result
