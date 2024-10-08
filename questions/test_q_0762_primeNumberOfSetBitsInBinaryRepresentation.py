import pytest
from q_0762_primeNumberOfSetBitsInBinaryRepresentation import Solution


@pytest.mark.parametrize("left, right, output", [(6, 10, 4), (10, 15, 5)])
class TestSolution:
    def test_countPrimeSetBits(self, left: int, right: int, output: int):
        sc = Solution()
        assert (
            sc.countPrimeSetBits(
                left,
                right,
            )
            == output
        )
