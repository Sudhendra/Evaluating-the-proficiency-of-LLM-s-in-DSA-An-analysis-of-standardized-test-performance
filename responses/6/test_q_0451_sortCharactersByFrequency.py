import pytest
from q_0451_sortCharactersByFrequency import Solution


@pytest.mark.parametrize(
    "s, output", [("tree", "eert"), ("cccaaa", "aaaccc"), ("Aabb", "bbAa")]
)
class TestSolution:
    def test_frequencySort(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.frequencySort(
                s,
            )
            == output
        )
