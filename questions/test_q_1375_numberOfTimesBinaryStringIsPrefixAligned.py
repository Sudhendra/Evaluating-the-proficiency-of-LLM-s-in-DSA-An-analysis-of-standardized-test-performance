import pytest
from q_1375_numberOfTimesBinaryStringIsPrefixAligned import Solution


@pytest.mark.parametrize("flips, output", [([3, 2, 4, 1, 5], 2), ([4, 1, 2, 3], 1)])
class TestSolution:
    def test_numTimesAllBlue(self, flips: List[int], output: int):
        sc = Solution()
        assert (
            sc.numTimesAllBlue(
                flips,
            )
            == output
        )
