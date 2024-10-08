import pytest
from q_2309_greatestEnglishLetterInUpperAndLowerCase import Solution


@pytest.mark.parametrize(
    "s, output", [("l**Ee**TcOd**E**", "E"), ("a**rR**AzFif", "R"), ("AbCdEfGhIjK", "")]
)
class TestSolution:
    def test_greatestLetter(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.greatestLetter(
                s,
            )
            == output
        )
