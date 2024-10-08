import pytest
from q_0667_beautifulArrangementIi import Solution


@pytest.mark.parametrize("n, k, output", [(3, 1, [1, 2, 3]), (3, 2, [1, 3, 2])])
class TestSolution:
    def test_constructArray(self, n: int, k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.constructArray(
                n,
                k,
            )
            == output
        )
