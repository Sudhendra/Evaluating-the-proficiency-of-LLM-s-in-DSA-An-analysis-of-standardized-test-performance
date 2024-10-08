import pytest
from q_0904_fruitIntoBaskets import Solution


@pytest.mark.parametrize(
    "fruits, output", [([1, 2, 1], 3), ([0, 1, 2, 2], 3), ([1, 2, 3, 2, 2], 4)]
)
class TestSolution:
    def test_totalFruit(self, fruits: List[int], output: int):
        sc = Solution()
        assert (
            sc.totalFruit(
                fruits,
            )
            == output
        )
