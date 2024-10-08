import pytest
from q_2379_minimumRecolorsToGetKConsecutiveBlackBlocks import Solution


@pytest.mark.parametrize("blocks, k, output", [("WBBWWBBWBW", 7, 3), ("WBWBBBW", 2, 0)])
class TestSolution:
    def test_minimumRecolors(self, blocks: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.minimumRecolors(
                blocks,
                k,
            )
            == output
        )
