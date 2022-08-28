import pytest
import json

result_part_2 = json.load(open("tests/result-2-part.json", 'r'))
result_full_2 = json.load(open("tests/result-2.json", 'r'))

@pytest.fixture(params = [
    {"data":("tests/soal-2-part.json", "tests/result-2-part.json"), "result": result_part_2},
    {"data":("tests/soal-2.json", "tests/result-2.json"), "result": result_full_2},
])
def common_args(request):
    return request.param
