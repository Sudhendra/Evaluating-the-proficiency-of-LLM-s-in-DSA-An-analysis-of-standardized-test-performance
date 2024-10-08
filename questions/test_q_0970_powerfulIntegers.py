import pytest
from q_0970_powerfulIntegers import Solution


@pytest.mark.parametrize(
    "x, y, bound, output",
    [(2, 3, 10, [2, 3, 4, 5, 7, 9, 10]), (3, 5, 15, [2, 4, 6, 8, 10, 14])],
)
class TestSolution:
    def test_powerfulIntegers(self, x: int, y: int, bound: int, output: List[int]):
        sc = Solution()
        assert (
            sc.powerfulIntegers(
                x,
                y,
                bound,
            )
            == output
        )
