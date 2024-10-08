import pytest
from q_1441_buildAnArrayWithStackOperations import Solution


@pytest.mark.parametrize(
    "target, n, output",
    [
        ([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
        ([1, 2, 3], 3, ["Push", "Push", "Push"]),
        ([1, 2], 4, ["Push", "Push"]),
    ],
)
class TestSolution:
    def test_buildArray(self, target: List[int], n: int, output: List[str]):
        sc = Solution()
        assert (
            sc.buildArray(
                target,
                n,
            )
            == output
        )
