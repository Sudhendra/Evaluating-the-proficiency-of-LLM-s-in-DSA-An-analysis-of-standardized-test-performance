import pytest
from q_0691_stickersToSpellWord import Solution


@pytest.mark.parametrize(
    "stickers, target, output",
    [
        (["with", "example", "science"], "thehat", 3),
        (["notice", "possible"], "basicbasic", -1),
    ],
)
class TestSolution:
    def test_minStickers(self, stickers: List[str], target: str, output: int):
        sc = Solution()
        assert (
            sc.minStickers(
                stickers,
                target,
            )
            == output
        )
