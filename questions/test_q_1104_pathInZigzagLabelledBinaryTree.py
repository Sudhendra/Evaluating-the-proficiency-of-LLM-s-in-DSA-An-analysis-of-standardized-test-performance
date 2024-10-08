import pytest
from q_1104_pathInZigzagLabelledBinaryTree import Solution


@pytest.mark.parametrize(
    "label, output", [(14, [1, 3, 4, 14]), (26, [1, 2, 6, 10, 26])]
)
class TestSolution:
    def test_pathInZigZagTree(self, label: int, output: List[int]):
        sc = Solution()
        assert (
            sc.pathInZigZagTree(
                label,
            )
            == output
        )
