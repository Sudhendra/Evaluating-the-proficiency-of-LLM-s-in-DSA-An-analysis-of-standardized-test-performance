import pytest
from q_1954_minimumGardenPerimeterToCollectEnoughApples import Solution


@pytest.mark.parametrize("neededApples, output", [(1, 8), (13, 16), (1000000000, 5040)])
class TestSolution:
    def test_minimumPerimeter(self, neededApples: int, output: int):
        sc = Solution()
        assert (
            sc.minimumPerimeter(
                neededApples,
            )
            == output
        )
