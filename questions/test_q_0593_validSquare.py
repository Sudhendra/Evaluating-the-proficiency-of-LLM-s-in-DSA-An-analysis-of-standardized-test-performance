import pytest
from q_0593_validSquare import Solution


@pytest.mark.parametrize(
    "p1, p2, p3, p4, output",
    [
        ([0, 0], [1, 1], [1, 0], [0, 1], True),
        ([0, 0], [1, 1], [1, 0], [0, 12], False),
        ([1, 0], [-1, 0], [0, 1], [0, -1], True),
    ],
)
class TestSolution:
    def test_validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int], output: bool
    ):
        sc = Solution()
        assert (
            sc.validSquare(
                p1,
                p2,
                p3,
                p4,
            )
            == output
        )
