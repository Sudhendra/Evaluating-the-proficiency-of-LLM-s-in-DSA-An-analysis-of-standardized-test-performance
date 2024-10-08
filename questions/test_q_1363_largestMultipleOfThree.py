import pytest
from q_1363_largestMultipleOfThree import Solution


@pytest.mark.parametrize(
    "digits, output", [([8, 1, 9], "981"), ([8, 6, 7, 1, 0], "8760"), ([1], "")]
)
class TestSolution:
    def test_largestMultipleOfThree(self, digits: List[int], output: str):
        sc = Solution()
        assert (
            sc.largestMultipleOfThree(
                digits,
            )
            == output
        )
