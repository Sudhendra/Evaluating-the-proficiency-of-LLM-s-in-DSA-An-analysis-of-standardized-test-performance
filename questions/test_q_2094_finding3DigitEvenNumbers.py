import pytest
from q_2094_finding3DigitEvenNumbers import Solution


@pytest.mark.parametrize(
    "digits, output",
    [
        ([2, 1, 3, 0], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),
        ([2, 2, 8, 8, 2], [222, 228, 282, 288, 822, 828, 882]),
        ([3, 7, 5], []),
    ],
)
class TestSolution:
    def test_findEvenNumbers(self, digits: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findEvenNumbers(
                digits,
            )
            == output
        )
