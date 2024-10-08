import pytest
from q_1444_numberOfWaysOfCuttingAPizza import Solution


@pytest.mark.parametrize(
    "pizza, k, output",
    [
        (["A..", "AAA", "..."], 3, 3),
        (["A..", "AA.", "..."], 3, 1),
        (["A..", "A..", "..."], 1, 1),
    ],
)
class TestSolution:
    def test_ways(self, pizza: List[str], k: int, output: int):
        sc = Solution()
        assert (
            sc.ways(
                pizza,
                k,
            )
            == output
        )
