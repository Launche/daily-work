"""
 Address: https://leetcode-cn.com/problems/two-sum/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
 Thinking: 两数和等于目标值可以转化为寻值问题。因为不是有序的,所以没有特别好的思路 target - L[i] = L[j].
           btw. 全部完成以后参考了官方给的思路,发现本处可以优化的地方, 即是如果不考虑空间复杂度,可以用动态查找方法(构造hash表 字典),使得查询效率更高
 Test: 1. python 数组可以无序的
       2. i in nums 和  i in enumerate(nums)的区别
       3. a.只有头下标i和冒号（代表的是从该头下标i的元素开始截取,一直到最后）b.只有冒号尾下标i（代表的是从开始一直截取到i-1的元素）c.头下标i,冒号和尾下标j都有（代表的是从i一直截取到j-1的元素）
       4. 字典访问用[]
 Review:
    查找:
        静态查找: 顺序(无序,有序),折半(有序),散列
        动态查找(动态修改查找表): 二叉排序树,散列


"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, e1 in enumerate(nums):
            for j, e2 in enumerate(nums[i + 1:]):
                if target - e1 == e2:
                    return [i, j + i + 1]
        return []


"""
Reference:
    solution2: 方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。因此,我们需要一种更优秀的方法,能够快速寻找数组中是否存在目标元素。如果存在,我们需要找出它的索引。
               使用哈希表,可以将寻找 target - x 的时间复杂度降低到从 O(N)O(N) 降低到 O(1)O(1)。
               这样我们创建一个哈希表,对于每一个 x,我们首先查询哈希表中是否存在 target - x,然后将 x 插入到哈希表中,即可保证不会让 x 和自己匹配。
"""


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i, e in enumerate(nums):
            if target - e in hash_table:
                return [hash_table[target - e], i]
            hash_table[e] = i
        return []


s = Solution2()
nums = [3, 3]
target = 6
print(s.twoSum(nums, target))
