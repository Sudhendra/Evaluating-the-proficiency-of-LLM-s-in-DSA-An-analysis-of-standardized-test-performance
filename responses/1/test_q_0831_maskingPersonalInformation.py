import pytest
from q_0831_maskingPersonalInformation import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("LeetCode@LeetCode.com", "l*****e@leetcode.com"),
        ("AB@qq.com", "a*****b@qq.com"),
        ("1(234)567-890", "***-***-7890"),
    ],
)
class TestSolution:
    def test_maskPII(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.maskPII(
                s,
            )
            == output
        )
