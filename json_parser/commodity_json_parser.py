import json

from .libs import berat_parser, komoditas_parser, transform


def json_loader(json_file: str) -> list[dict]:
    return json.load(open(json_file, 'r'))

def json_saver(data, filepath):
    with open(filepath, "w") as outfile:
        json.dump(data, outfile, indent=4)


def json_parser(json_file: str, dest_path: str = None) -> dict:
    """Parsing a commodity json file, then aggregate its value based on each commodity.

    Args:
        json_file (str): The PATH of the json file to be parsed
        dest_path (str, optional): Destination of the result file path. If not set, the result
                will be exported to the current working directory, with filename
                'result.json'.

    Returns:
        dict: The results, sorted from the highest to lowest value.
    """

    komoditas_berat_total = {}
    data = json_loader(json_file)

    for elem in data:
        komoditas_list = komoditas_parser.parse(elem["komoditas"])
        berat_raw_text = berat_parser.parse(elem["berat"])

        if 'kecuali' in berat_raw_text:
            komo_berat_dict = transform.process_kecuali(berat_raw_text, komoditas_list)
            komoditas_berat_total = transform.append_two_dict(komoditas_berat_total, komo_berat_dict)

        else:
            cleaned_berat_list = transform.get_cleaned_list(berat_raw_text.split(','))

            if len(cleaned_berat_list)==1:
                komo_berat_dict = transform.process_berat_one_length(cleaned_berat_list, komoditas_list)
                komoditas_berat_total = transform.append_two_dict(komoditas_berat_total, komo_berat_dict)

            elif len(komoditas_list)==len(cleaned_berat_list):
                komo_berat_dict = transform.process_komo_berat_equal(cleaned_berat_list, komoditas_list)
                komoditas_berat_total = transform.append_two_dict(komoditas_berat_total, komo_berat_dict)
            
            elif len(komoditas_list)<len(cleaned_berat_list):
                komo_berat_dict = transform.process_komo_lt_berat(cleaned_berat_list, komoditas_list)
                komoditas_berat_total = transform.append_two_dict(komoditas_berat_total, komo_berat_dict)

            elif len(komoditas_list)>len(cleaned_berat_list):
                komo_berat_dict = transform.process_komo_gt_berat(cleaned_berat_list, komoditas_list)
                komoditas_berat_total = transform.append_two_dict(komoditas_berat_total, komo_berat_dict)

            else:
                print( f"{komoditas_list} | {cleaned_berat_list}" )

    sorted_komoditas_berat_total = {key: f"{value}kg" for key,value in sorted(komoditas_berat_total.items(), key=lambda item: item[1], reverse=True)}
    if not dest_path:
        dest_path = "result.json"
    json_saver(sorted_komoditas_berat_total, dest_path)
    return sorted_komoditas_berat_total
