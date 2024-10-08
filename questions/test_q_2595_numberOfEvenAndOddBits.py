import pytest
from q_2595_numberOfEvenAndOddBits import Solution


@pytest.mark.parametrize("n, output", [(17, [2, 0]), (2, [0, 1])])
class TestSolution:
    def test_evenOddBit(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.evenOddBit(
                n,
            )
            == output
        )
