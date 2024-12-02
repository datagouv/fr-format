from frformat import Canton
from frformat.utils.versioned_set import Version


def test_canton():
    canton_2023 = Canton(Version("2023"))
    canton_2024 = Canton(Version("2024"))
    # canton_2025 = Canton(Version("2025"))

    valid_test_cases_cog_2023 = [
        "Lagnieu",
        "Meximieux",
    ]
    invalid_test_cases_cog_2023 = ["Paris", "Lyon", "paris"]

    valid_test_cases_cog_2024 = ["Paris", "Lyon"]

    invalid_test_cases_cog_2024 = ["Saint Quentin", "saint  quentin"]

    for tc in valid_test_cases_cog_2023:
        assert canton_2023.is_valid(tc)

    for tc in invalid_test_cases_cog_2023:
        assert not canton_2023.is_valid(tc)

    for tc in valid_test_cases_cog_2024:
        assert canton_2024.is_valid(tc)

    for tc in invalid_test_cases_cog_2024:
        assert not canton_2024.is_valid(tc)

    # assert canton_2025.is_valid("paris")
