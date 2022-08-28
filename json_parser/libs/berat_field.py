import re

berat_num_terms_mapping = {
    'kepiting 1, udang 1': ['kepiting dan udang 1kg' ],
    'udang 1': ['udang cumi 1kg' ],

    # pembulatan ke atas & untuk range ambil nilai tertinggi

    '0': ['gak nentu', 'gak tau kata pegawai nya', 'gak tau katanya cuma jaga warung', 'idem yg punyanya nga ada cuma pegawai', 'idem', 'tidak menentu', 'ekg', ],
    '1': ['sekilo', '1-1/2', '1kg rata2 kadang kurang dari 1kg', ] + ['1/2', 'setengah kilo', 'setengan kilo', '2 hari 1kg', ],
    '2': ['-+ 2', '2kg kadang 1kg masing2', ] + ['1 1/2', '1,5', '1.5', '1s.d 1,5',  ], 
    '3': ['2-2,5', '2,5', ],
    '4': ['4 atau 3kg', ] + ['3-3,5', ],
    '5': ['3-4,5', '4-4,5', ],
    '6': ['5-5,5', ],
    '8': ['15kg untuk 2 kios', ],
}

berat_txt_terms_mapping = {
    'rerata': ['masing masing', 'rata rata', 'masing-masing', 'rata-rata', 'ratarata', 'rata2', 'rata', 'masing2', 'masing', ],
    '-': ["sampai", "sampe", ],
}

stop_words_berat = [
    "idem", "per", "hari", "perhari", "kadang", "kurang", "dari", "semua", "jenis", "ikan", "perikan", "tawar", "lebih", 
]

class BeratParser(object):
    berat_stop_words = re.compile(r'\b(' + r'|'.join(stop_words_berat) + r')\b\s*')

    def __text_mapping(self, txt: str) -> str:
        txt = txt.replace('.', ' ')
        for k,v in berat_num_terms_mapping.items():
            txt = re.sub("|".join(sorted(v, key = len, reverse = True)), k, txt)
        for k,v in berat_txt_terms_mapping.items():
            txt = re.sub("|".join(sorted(v, key = len, reverse = True)), k, txt)
        return txt

    def __get_cleaned_text(self, txt:str) -> str:
        cleaned_txt = txt.lower()
        cleaned_txt = self.berat_stop_words.sub(' ', cleaned_txt)
        cleaned_txt = cleaned_txt.replace('kg', '').replace('jg', ' ').replace('-+', '').replace(' - ', '-')
        return cleaned_txt.strip()

    def parse(self, txt: str) -> str:
        return self.__get_cleaned_text( self.__text_mapping(txt) )

berat_parser = BeratParser()