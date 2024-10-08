import pytest
from q_0984_stringWithoutAaaOrBbb import Solution


@pytest.mark.parametrize("a, b, output", [(1, 2, "abb"), (4, 1, "aabaa")])
class TestSolution:
    def test_strWithout3a3b(self, a: int, b: int, output: str):
        sc = Solution()
        assert (
            sc.strWithout3a3b(
                a,
                b,
            )
            == output
        )
