import pytest
from q_0135_candy import Solution


@pytest.mark.parametrize("ratings, output", [([1, 0, 2], 5), ([1, 2, 2], 4)])
class TestSolution:
    def test_candy(self, ratings: List[int], output: int):
        sc = Solution()
        assert (
            sc.candy(
                ratings,
            )
            == output
        )
