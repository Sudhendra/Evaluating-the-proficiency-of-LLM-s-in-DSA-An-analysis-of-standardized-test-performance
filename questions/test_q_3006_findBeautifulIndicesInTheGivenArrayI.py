import pytest
from q_3006_findBeautifulIndicesInTheGivenArrayI import Solution


@pytest.mark.parametrize(
    "s, a, b, k, output",
    [
        ("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15, [16, 33]),
        ("abcd", "a", "a", 4, [0]),
    ],
)
class TestSolution:
    def test_beautifulIndices(self, s: str, a: str, b: str, k: int, output: List[int]):
        sc = Solution()
        assert (
            sc.beautifulIndices(
                s,
                a,
                b,
                k,
            )
            == output
        )
