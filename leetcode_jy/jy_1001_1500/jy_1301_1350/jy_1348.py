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
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Tweet-Counts-Per-Frequency(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).
For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:
Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
Every day (86400-second chunks): [10,10000]
Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).
Design and implement an API to help the company with their analysis.
Implement the TweetCounts class:
TweetCounts() Initializes the TweetCounts object.
void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime, endTime] (in seconds) and frequency freq.
  ○ freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.
Example:
Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[None,None,None,None,[2],[2,1],None,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0)                               # New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60)                              # New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10)                              # New tweet "tweet3" at time 10
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)  # return [2]; chunk [0,59] had 2 tweets
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)  # return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120)                             # New tweet "tweet3" at time 120
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210)   # return [4]; chunk [0,210] had 4 tweets


Constraints:
0 <= time, startTime, endTime <= 10^9
0 <= endTime - startTime <= 10^4
There will be at most 10^4 calls in total to recordTweet and getTweetCountsPerFrequency.
"""


import bisect
import collections
from bisect import bisect_left
from typing import List


"""
解法1
使用 Map 保存 tweetName 对应的操作时间, 并保持有序; 查找时, 使用二分查找定位区间的开始和结束位置对应的位置, 两者相减就是该区间内的 Tweet 数量;
"""
class TweetCounts:
    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> List[int]:
        delta = 1

        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 60 * 60
        elif freq == 'day':
            delta = 60 * 60 * 24

        start = startTime
        counts = []

        while start <= endTime:
            end = min(start + delta, endTime + 1)
            count = bisect_left(self.tweets[tweetName], end) \
                - bisect_left(self.tweets[tweetName], start)
            counts.append(count)
            start += delta

        return counts


import bisect
import collections
from typing import List


"""
解法2
同样是使用 Map 保存 tweetName 对应的操作时间, 但无须保持有序; 查找时, 先根据开始时间和结束时间计算出区间的个数, 提前初始化固定容量的数组, 然后遍历所有具体时间, 将其放入到指定的位置中;
"""
class TweetCounts:
    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> List[int]:
        delta = 1

        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 60 * 60
        elif freq == 'day':
            delta = 60 * 60 * 24

        size = (endTime - startTime) # delta + 1
        counts = [0] * size

        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                index = (time - startTime) # delta
                counts[index] += 1

        return counts



