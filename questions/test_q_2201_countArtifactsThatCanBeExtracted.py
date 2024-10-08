import pytest
from q_2201_countArtifactsThatCanBeExtracted import Solution


@pytest.mark.parametrize(
    "n, artifacts, dig, output",
    [
        (2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1]], 1),
        (2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1]], 2),
    ],
)
class TestSolution:
    def test_digArtifacts(
        self, n: int, artifacts: List[List[int]], dig: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.digArtifacts(
                n,
                artifacts,
                dig,
            )
            == output
        )
