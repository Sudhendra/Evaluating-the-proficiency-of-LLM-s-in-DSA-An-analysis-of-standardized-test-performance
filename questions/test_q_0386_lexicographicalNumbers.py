import pytest
from q_0386_lexicographicalNumbers import Solution


@pytest.mark.parametrize(
    "n, output", [(13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]), (2, [1, 2])]
)
class TestSolution:
    def test_lexicalOrder(self, n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.lexicalOrder(
                n,
            )
            == output
        )
