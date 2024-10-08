import pytest
from q_2129_capitalizeTheTitle import Solution


@pytest.mark.parametrize(
    "title, output",
    [
        ("capiTalIze tHe titLe", "Capitalize The Title"),
        ("First leTTeR of EACH Word", "First Letter of Each Word"),
        ("i lOve leetcode", "i Love Leetcode"),
    ],
)
class TestSolution:
    def test_capitalizeTitle(self, title: str, output: str):
        sc = Solution()
        assert (
            sc.capitalizeTitle(
                title,
            )
            == output
        )
