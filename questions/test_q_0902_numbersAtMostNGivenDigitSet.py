import pytest
from q_0902_numbersAtMostNGivenDigitSet import Solution


@pytest.mark.parametrize(
    "digits, n, output",
    [
        (["1", "3", "5", "7"], 100, 20),
        (["1", "4", "9"], 1000000000, 29523),
        (["7"], 8, 1),
    ],
)
class TestSolution:
    def test_atMostNGivenDigitSet(self, digits: List[str], n: int, output: int):
        sc = Solution()
        assert (
            sc.atMostNGivenDigitSet(
                digits,
                n,
            )
            == output
        )
