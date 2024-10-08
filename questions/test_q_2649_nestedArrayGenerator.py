import pytest
from q_2649_nestedArrayGenerator import Solution


@pytest.mark.parametrize("arr, output", [([[[6]], [1, 3], []], [6, 1, 3]), ([], [])])
class TestSolution:
    def test_nestedArrayGenerator(self, output: Any):
        sc = Solution()
        assert (
            sc.nestedArrayGenerator(
                arr,
            )
            == output
        )
