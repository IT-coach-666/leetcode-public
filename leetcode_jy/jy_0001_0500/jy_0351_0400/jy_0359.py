# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
assert project_name == "leetcode_jy" and project_name == "leetcode_jy" and \
       url_ == "www.yuque.com/it-coach"
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Logger-Rate-Limiter(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique
message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will
prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:
Logger(): Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message): Returns true if the message should be printed
                                                       in the given timestamp, otherwise returns false.

Example 1:
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");    # return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");    # return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");    # 3 < 11, return false
logger.shouldPrintMessage(8, "bar");    # 8 < 12, return false
logger.shouldPrintMessage(10, "foo");   # 10 < 11, return false
logger.shouldPrintMessage(11, "foo");   # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21


Constraints:
0 <= timestamp <= 10^9
Every timestamp will be passed in non-decreasing order (chronological order).
1 <= message.length <= 30
At most 10^4 calls will be made to shouldPrintMessage.
"""

"""
使用 Map 记录日志最开始出现的时间;
"""
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed. The timestamp is in seconds granularity.
        """
        # jy: 如果 message 不在 logs 中, 或者在 logs 中, 但其对应的原有 timestamp 加上 10s 小于当前传
        #    入的 timestamp, 则表明可以输出, 输出时同时更新 timestamp;
        if message not in self.logs or self.logs[message] + 10 <= timestamp:
            self.logs[message] = timestamp
            return True
        else:
            return False


logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))    # return true, next allowed timestamp for "foo" is 1 + 10 = 11
print(logger.shouldPrintMessage(2, "bar"))    # return true, next allowed timestamp for "bar" is 2 + 10 = 12
print(logger.shouldPrintMessage(3, "foo"))    # 3 < 11, return false
print(logger.shouldPrintMessage(8, "bar"))    # 8 < 12, return false
print(logger.shouldPrintMessage(10, "foo"))   # 10 < 11, return false
print(logger.shouldPrintMessage(11, "foo"))   # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21


