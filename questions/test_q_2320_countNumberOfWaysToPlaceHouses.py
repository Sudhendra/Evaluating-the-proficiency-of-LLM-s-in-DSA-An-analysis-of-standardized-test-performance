import pytest
from q_2320_countNumberOfWaysToPlaceHouses import Solution


@pytest.mark.parametrize("n, output", [(1, 4), (2, 9)])
class TestSolution:
    def test_countHousePlacements(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countHousePlacements(
                n,
            )
            == output
        )
