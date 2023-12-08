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
title_jy = "Design-Underground-System(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.
Implement the UndergroundSystem class:
void checkIn(int id, string stationName, int t)
  ○ A customer with a card ID equal to id, checks in at the station stationName at time t.
  ○ A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
  ○ A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
  ○ Returns the average time it takes to travel from startStation to endStation.
  ○ The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
  ○ The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
  ○ There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

Example 1:
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[None,None,None,None,None,None,None,14.00000,11.00000,None,11.00000,None,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15)   # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20)   # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge")  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38)   # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo")     # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

Example 2:
Input
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

Output
[None,None,None,5.00000,None,None,5.50000,None,None,6.66667]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8)  # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 5.00000, (5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16)  # Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 5.50000, (5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30)  # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
undergroundSystem.getAverageTime("Leyton", "Paradise")  # return 6.66667, (5 + 6 + 9) / 3 = 6.66667


Constraints:
1 <= id, t <= 10^6
1 <= stationName.length, startStation.length, endStation.length <= 10
All strings consist of uppercase and lowercase English letters and digits.
There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and getAverageTime.
Answers within 10^-5 of the actual value will be accepted.
"""


import collections


class User:
    def __init__(self, id, check_in_station_name, check_in_time):
        self.id = id
        self.check_in_station_name = check_in_station_name
        self.check_in_time = check_in_time


class Station:
    def __init__(self, total_time=0, count=0):
        self.total_time = total_time
        self.count = count

"""
使用 Map 根据用户 id 保存用户的进站记录, 再使用一个 Map 保存始发站到各个终点站的映射, 每个站点维护所有用户的旅行总时间和旅行次数; 用户出站时, 根据 id 拿到进站记录, 将用户的旅行时间更新到对应的出站站点的信息中; 平均旅行时间就是对应站点的总时间除以旅行次数;
"""
class UndergroundSystem:
    def __init__(self):
        self.users = {}
        self.stations = collections.defaultdict(
            lambda: collections.defaultdict(Station))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = User(id, stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        user = self.users.pop(id)
        end_station = self.stations[user.check_in_station_name][stationName]
        end_station.count += 1
        end_station.total_time += t - user.check_in_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        end_station = self.stations[startStation][endStation]

        return end_station.total_time / end_station.count


