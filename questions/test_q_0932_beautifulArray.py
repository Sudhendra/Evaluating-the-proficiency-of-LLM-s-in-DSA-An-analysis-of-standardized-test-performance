import pytest
from q_0932_beautifulArray import Solution


@pytest.mark.parametrize("n, output", [(4, [2, 1, 4, 3]), (5, [3, 1, 2, 5, 4])])
class TestSolution:
    def test_beautifulArray(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.beautifulArray(
                n,
            )
            == output
        )
