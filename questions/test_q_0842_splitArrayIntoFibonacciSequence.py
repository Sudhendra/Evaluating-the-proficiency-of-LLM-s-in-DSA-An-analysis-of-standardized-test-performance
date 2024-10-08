import pytest
from q_0842_splitArrayIntoFibonacciSequence import Solution


@pytest.mark.parametrize(
    "num, output", [("1101111", [11, 0, 11, 11]), ("112358130", []), ("0123", [])]
)
class TestSolution:
    def test_splitIntoFibonacci(self, num: str, output: List[int]):
        sc = Solution()
        assert (
            sc.splitIntoFibonacci(
                num,
            )
            == output
        )
