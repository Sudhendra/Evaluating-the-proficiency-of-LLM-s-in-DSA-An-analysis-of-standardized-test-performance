import pytest
from q_2125_numberOfLaserBeamsInABank import Solution


@pytest.mark.parametrize(
    "bank, output",
    [(["011001", "000000", "010100", "001000"], 8), (["000", "111", "000"], 0)],
)
class TestSolution:
    def test_numberOfBeams(self, bank: List[str], output: int):
        sc = Solution()
        assert (
            sc.numberOfBeams(
                bank,
            )
            == output
        )
