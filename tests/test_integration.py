import distance_calculator.utils as utils
import sys

def test_api(countries, expected_values):
    assert utils.get_distance(countries[0], countries[1]) == expected_values[0]
    assert utils.get_distance(countries[2], countries[3]) == expected_values[1]


def test_utils(raw_countries, expected_values):
    parsed_countries = []

    for i in range(len(raw_countries)):
        try:
            parsed_country = utils.parse_country_name(raw_countries[i])

            assert parsed_country == expected_values[i]
            parsed_countries.append(parsed_country)
        except KeyError:
            assert expected_values[i] == "Invalid Country"

    return parsed_countries


if __name__ == "__main__":
    assert len(sys.argv) == 2

    utils.api_key = sys.argv[1]

    raw_countries = ["Netherlands ", "Atlantis", "  France", "Germany", "Croatia"]
    parsed_countries = ["Netherlands", "Invalid Country", "France", "Germany", "Croatia"]

    parsed_countries = test_utils(raw_countries, parsed_countries)
    test_api(parsed_countries, [746, 794])

