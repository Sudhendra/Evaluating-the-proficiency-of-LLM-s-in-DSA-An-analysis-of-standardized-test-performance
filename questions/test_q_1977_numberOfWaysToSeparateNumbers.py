import pytest
from q_1977_numberOfWaysToSeparateNumbers import Solution


@pytest.mark.parametrize("num, output", [("327", 2), ("094", 0), ("0", 0)])
class TestSolution:
    def test_numberOfCombinations(self, num: str, output: int):
        sc = Solution()
        assert (
            sc.numberOfCombinations(
                num,
            )
            == output
        )
