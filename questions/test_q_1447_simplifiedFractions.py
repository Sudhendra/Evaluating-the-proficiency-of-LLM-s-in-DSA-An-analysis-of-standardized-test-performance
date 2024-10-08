import pytest
from q_1447_simplifiedFractions import Solution


@pytest.mark.parametrize(
    "n, output",
    [
        (2, ["1/2"]),
        (3, ["1/2", "1/3", "2/3"]),
        (4, ["1/2", "1/3", "1/4", "2/3", "3/4"]),
    ],
)
class TestSolution:
    def test_simplifiedFractions(self, n: int, output: List[str]):
        sc = Solution()
        assert (
            sc.simplifiedFractions(
                n,
            )
            == output
        )
