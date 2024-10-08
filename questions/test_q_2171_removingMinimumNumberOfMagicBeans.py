import pytest
from q_2171_removingMinimumNumberOfMagicBeans import Solution


@pytest.mark.parametrize("beans, output", [([4, 1, 6, 5], 4), ([2, 10, 3, 2], 7)])
class TestSolution:
    def test_minimumRemoval(self, beans: List[int], output: int):
        sc = Solution()
        assert (
            sc.minimumRemoval(
                beans,
            )
            == output
        )
