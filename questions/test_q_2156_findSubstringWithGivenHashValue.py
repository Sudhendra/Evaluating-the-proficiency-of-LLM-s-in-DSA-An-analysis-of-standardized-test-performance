import pytest
from q_2156_findSubstringWithGivenHashValue import Solution


@pytest.mark.parametrize(
    "s, power, modulo, k, hashValue, output",
    [("leetcode", 7, 20, 2, 0, "ee"), ("fbxzaad", 31, 100, 3, 32, "fbx")],
)
class TestSolution:
    def test_subStrHash(
        self, s: str, power: int, modulo: int, k: int, hashValue: int, output: str
    ):
        sc = Solution()
        assert (
            sc.subStrHash(
                s,
                power,
                modulo,
                k,
                hashValue,
            )
            == output
        )
