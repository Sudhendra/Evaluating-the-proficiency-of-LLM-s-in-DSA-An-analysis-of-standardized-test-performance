import pytest
from q_2785_sortVowelsInAString import Solution


@pytest.mark.parametrize("s, output", [("lEetcOde", "lEOtcede"), ("lYmpH", "lYmpH")])
class TestSolution:
    def test_sortVowels(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.sortVowels(
                s,
            )
            == output
        )
