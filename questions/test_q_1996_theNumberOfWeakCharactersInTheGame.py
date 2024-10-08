import pytest
from q_1996_theNumberOfWeakCharactersInTheGame import Solution


@pytest.mark.parametrize(
    "properties, output",
    [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1),
    ],
)
class TestSolution:
    def test_numberOfWeakCharacters(self, properties: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.numberOfWeakCharacters(
                properties,
            )
            == output
        )
