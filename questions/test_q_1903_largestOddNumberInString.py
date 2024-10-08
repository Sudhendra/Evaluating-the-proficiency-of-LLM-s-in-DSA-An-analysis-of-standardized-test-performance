import pytest
from q_1903_largestOddNumberInString import Solution


@pytest.mark.parametrize("num, output", [("52", "5"), ("4206", ""), ("35427", "35427")])
class TestSolution:
    def test_largestOddNumber(self, num: str, output: str):
        sc = Solution()
        assert (
            sc.largestOddNumber(
                num,
            )
            == output
        )
