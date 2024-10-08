import pytest
from q_0749_containVirus import Solution


@pytest.mark.parametrize(
    "isInfected, output",
    [
        (
            [
                [0, 1, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            10,
        ),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 4),
        (
            [
                [1, 1, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 0, 0, 0],
            ],
            13,
        ),
    ],
)
class TestSolution:
    def test_containVirus(self, isInfected: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.containVirus(
                isInfected,
            )
            == output
        )
