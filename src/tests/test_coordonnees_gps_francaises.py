from dataclasses import dataclass

from frformat import CoordonneesGPSFrancaises


def test_coordonnees_gps_francaises__is_valid():
    @dataclass
    class TestCase:
        name: str
        coordinates: tuple[float, float]
        is_in_france: bool

    test_cases = [
        TestCase("Paris", (2.294481, 48.85837), True),
        TestCase("Bellac", (1.0613287, 46.1257867), True),
        TestCase("Corse", (9.1947495, 42.2315836), True),
        TestCase("Guadeloupe", (-61.4794838, 16.1923342), True),
        TestCase("Martinique", (-60.9622795, 14.5618015), True),
        TestCase("Guyane", (-53.9511024, 3.9935171), True),
        TestCase("La Réunion", (55.4264032, -21.3089126), True),
        TestCase("Mayotte", (45.0993933, -12.8392093), True),
        TestCase("Berlin", (13.3982663, 52.5075445), False),
        TestCase("Valence", (-0.4439106, 39.4078888), False),
    ]

    for tc in test_cases:
        assert (
            CoordonneesGPSFrancaises.is_valid(*tc.coordinates) == tc.is_in_france
        ), tc.name
