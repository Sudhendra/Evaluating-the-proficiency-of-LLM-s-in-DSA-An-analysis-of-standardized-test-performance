import pytest
from q_2325_decodeTheMessage import Solution


@pytest.mark.parametrize(
    "key, message, output",
    [
        (
            "the quick brown fox jumps over the lazy dog",
            "vkbs bs t suepuv",
            "this is a secret",
        ),
        (
            "eljuxhpwnyrdgtqkviszcfmabo",
            "zwx hnfx lqantp mnoeius ycgk vcnjrdb",
            "the five boxing wizards jump quickly",
        ),
    ],
)
class TestSolution:
    def test_decodeMessage(self, key: str, message: str, output: str):
        sc = Solution()
        assert (
            sc.decodeMessage(
                key,
                message,
            )
            == output
        )
