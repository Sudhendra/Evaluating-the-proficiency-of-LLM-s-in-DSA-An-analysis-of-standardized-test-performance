import pytest
from q_1734_decodeXoredPermutation import Solution


@pytest.mark.parametrize(
    "encoded, output", [([3, 1], [1, 2, 3]), ([6, 5, 4, 6], [2, 4, 1, 5, 3])]
)
class TestSolution:
    def test_decode(self, encoded: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.decode(
                encoded,
            )
            == output
        )
