from json_parser import __version__, json_parser


def test_version():
    assert __version__ == '0.1.0'

def test_commodity_json_parser(common_args):
    data = common_args["data"]
    expected = common_args["result"]
    actual = json_parser(data[0], data[1])
    assert actual == expected, f"Failed match actual parsed: {actual} | expected parsed: {expected}"