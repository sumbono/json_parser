from collections import Counter
from string import punctuation

import re


komoditas_stop_words = [
    "ikan", "kecuali", "dll", "ikn", "nasi", "babat",  "laut", 
    "pecel", "sate", "usus", "uduk", "soto", "kikil", "tawar",
    "sotobayam", "sea", "food", "kepala", "goreng", "bakar", 
    "merah", "hitam", 
    "ayam", "bebek", 
    "dan ", 
    "rata2", "rata", "idem", 
]

komoditas_word_mapping = {
    "tongkol": ["tongkol", "tingkol", "tngkol", ],
    "salem": ["salem", "salam"],
    "patin": ["patin", "parin"],
    "mujair": ["mujair", "mujaer", "majaer", "jaer", "muajir", ], 
    "nila ": ["nil "],  
    "mas": ["mas", "man", "emas", ],
    "lele": ["lelw", "kele", "ikanlele", ],
    "kerapu": ["krapu", "kerpu", ],
    "kembung": ["kembug", "gembung" ], 
    "gurame": ["gurami", ], 
    # "baronang": ["barunang", ], 
}

class KomoditasParser(object):
    regx_komo_stop_words = re.compile(r'\b(' + r'|'.join(komoditas_stop_words) + r')\b\s*')

    def __get_cleaned_text(self, txt: str) -> str:
        cleaned_txt = txt.lower()
        for punc in punctuation:
            cleaned_txt = cleaned_txt.replace(punc,' ')
        cleaned_txt = self.regx_komo_stop_words.sub(' ', cleaned_txt)
        return cleaned_txt

    def __replace_wrong_words(self, txt: str) -> str:
        for k,v in komoditas_word_mapping.items():
            txt = re.sub("|".join(sorted(v, key = len, reverse = True)), k, txt)
        return txt

    def __get_word_list(self, txt: str) -> list:
        word_counts = dict(Counter(txt.split()))
        return [k for k,v in word_counts.items()]
    
    def parse(self, txt: str) -> list:
        return self.__get_word_list( self.__replace_wrong_words( self.__get_cleaned_text(txt) ) )

komoditas_parser = KomoditasParser()