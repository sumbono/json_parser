
class Transform(object):

    def append_two_dict(self, dict_a: dict, dict_b: dict) -> dict:
        """append value and key of dict_b to dict_a.

        Args:
            dict_a (dict): receiver dictionary.
            dict_b (dict): appender dictionary.

        Returns:
            dict: appended dict_a.
        """

        for k,v in dict_b.items():
            if k in dict_a:
                dict_a[k] += v
            else:
                dict_a.update({k:v})
        return dict_a

    def get_cleaned_list(self, a_list: list) -> list:
        """
        - next step on cleaning the text, after split(). 
        - cleaning on each element.
        - removing hypen on a value range, then choose the highest value. 
        - removing 'rerata' string on each element.

        Args:
            a_list (list): list containing raw elements.

        Returns:
            list: cleaned list.
        """

        new_list = []
        for el in a_list:
            if '-' in el.strip():
                nel = el.replace('rerata','').strip().split('-')[-1].strip()
            elif el.strip().isalnum():
                nel = "".join([i for i in el if i.isdigit()])
            else:
                nel = el.replace('rerata','').replace(',',' ').strip()
            if nel.strip():
                new_list.append(nel)
        return new_list

    def process_kecuali(self, berat_raw_text: str, komoditas_list: list) -> dict:
        """use this parser if 'kecuali' word exist on berat_raw_text.

        Args:
            berat_raw_text (str): raw value of 'berat' field.
            komoditas_list (list): cleaned list of 'komoditas' field.

        Returns:
            dict: cleaned komoditas - berat dictionary.
        """

        local_komo_brt = {}
        bti_list = berat_raw_text.split('kecuali') # always being two-elements list
        new_bti_list = self.get_cleaned_list(bti_list)
        
        # process the last element of new_bti_list
        brt_txt, brt_num = [], []
        for brt_spc in new_bti_list[-1].strip().split():
            if brt_spc.strip().isdigit():
                brt_num.append(int(brt_spc.strip()))
            else:
                brt_txt.append(brt_spc.strip())
        local_komo_brt.update( dict(zip(brt_txt, brt_num)) )

        # process the first element of new_bti_list
        if new_bti_list[0]:
            for komo in komoditas_list:
                if komo not in local_komo_brt:
                    local_komo_brt.update({komo : int(new_bti_list[0])})
        
        return local_komo_brt

    def process_berat_one_length(self, cleaned_berat_list: list, komoditas_list: list) -> dict:
        """use this parser if cleaned_berat_list only have one element.

        Args:
            cleaned_berat_list (list): cleaned list of 'berat' field.
            komoditas_list (list): cleaned list of 'komoditas' field.

        Returns:
            dict: cleaned komoditas - berat dictionary.
        """

        local_komo_brt = {}
        
        if cleaned_berat_list[0].isdigit():
            for komo in komoditas_list:
                if komo in local_komo_brt:
                    local_komo_brt[komo] += int(cleaned_berat_list[0])
                else:
                    local_komo_brt.update({komo : int(cleaned_berat_list[0])})
        else:
            brt_txt, brt_num = [], []
            for brt_spc in cleaned_berat_list[0].split():
                if brt_spc.strip().isdigit():
                    brt_num.append(int(brt_spc.strip()))
                else:
                    brt_txt.append(brt_spc.strip())
            
            if len(brt_txt)==len(brt_num):
                kmdts_brt_map = dict(zip(brt_txt, brt_num))
                for k,v in kmdts_brt_map.items():
                    if k in local_komo_brt:
                        local_komo_brt[k] += v
                    else:
                        local_komo_brt.update({k:v})

        return local_komo_brt

    def process_komo_berat_equal(self, cleaned_berat_list: list, komoditas_list: list) -> dict:
        """parser for len(cleaned_berat_list) equal with len(komoditas_list).

        Args:
            cleaned_berat_list (list): cleaned list of 'berat' field.
            komoditas_list (list): cleaned list of 'komoditas' field.

        Returns:
            dict: cleaned komoditas - berat dictionary.
        """

        local_komo_brt = {}

        if all([el.strip().isdigit() for el in cleaned_berat_list]):
            kmdts_brt_map = dict(zip(komoditas_list, [int(el) for el in cleaned_berat_list]))
            for k,v in kmdts_brt_map.items():
                if k in local_komo_brt:
                    local_komo_brt[k] += v
                else:
                    local_komo_brt.update({k:v})
        
        # elif all([not el.strip().isalpha() for el in cleaned_berat_list]):
        elif all([len(el.strip().split())==2 for el in cleaned_berat_list]):
            for brt in cleaned_berat_list:
                txt_num = brt.split()
                if txt_num[0].strip().isalpha():
                    if txt_num[0].strip() in local_komo_brt:
                        local_komo_brt[txt_num[0].strip()] += int(txt_num[1].strip())
                    else:
                        local_komo_brt.update({txt_num[0].strip() : int(txt_num[1].strip())})
                elif txt_num[1].strip().isalpha():
                    if txt_num[1].strip() in local_komo_brt:
                        local_komo_brt[txt_num[1].strip()] += int(txt_num[0].strip())
                    else:
                        local_komo_brt.update({txt_num[1].strip() : int(txt_num[0].strip())})

        return local_komo_brt

    def process_komo_lt_berat(self, cleaned_berat_list: list) -> dict:
        local_komo_brt = {}

        # this cleaned_berat_list contain string and number
        if all([not el.strip().isalpha() for el in cleaned_berat_list]):
            for brt in cleaned_berat_list:
                txt_num = brt.split()
                if txt_num[0].strip().isalpha():
                    if txt_num[0].strip() in local_komo_brt:
                        local_komo_brt[txt_num[0].strip()] += int(txt_num[1].strip())
                    else:
                        local_komo_brt.update({txt_num[0].strip() : int(txt_num[1].strip())})
                elif txt_num[1].strip().isalpha():
                    if txt_num[1].strip() in local_komo_brt:
                        local_komo_brt[txt_num[1].strip()] += int(txt_num[0].strip())
                    else:
                        local_komo_brt.update({txt_num[1].strip() : int(txt_num[0].strip())})

        return local_komo_brt

    def process_komo_gt_berat(self, cleaned_berat_list: list, komoditas_list: list) -> dict:
        local_komo_brt = {}

        #create cleaned_berat_list lists
        nb_digit_only, nb_text_digit = [], []
        for el in cleaned_berat_list:
            if el.isdigit():
                nb_digit_only.append(el)
            else:
                nb_text_digit.append(el)

        # process the list nb_text_digit
        brt_txt, brt_num = [], []
        for ntdg in nb_text_digit:
            for brt_spc in ntdg.split():
                if brt_spc.strip().isdigit():
                    brt_num.append(int(brt_spc.strip()))
                else:
                    brt_txt.append(brt_spc.strip())
        local_komo_brt.update( dict(zip(brt_txt, brt_num)) )

        # process the first element of nb_digit_only
        if nb_digit_only[0]:
            for komo in komoditas_list:
                if komo not in local_komo_brt:
                    local_komo_brt.update({komo : int(nb_digit_only[0])})
                
        return local_komo_brt


transform = Transform()