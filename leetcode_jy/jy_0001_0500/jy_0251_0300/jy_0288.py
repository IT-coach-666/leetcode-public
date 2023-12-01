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
title_jy = "Unique-Word-Abbreviation(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The abbreviation of a word is a concatenation of its first letter, the number of
characters between the first and last letter, and its last letter. If a word has
only two characters, then it is an abbreviation of itself.

For example:
dog --> d1g because there is one letter between the first letter 'd' and the last
        letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter
                         'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.



Implement the ValidWordAbbr class:
ValidWordAbbr(String[] dictionary): Initializes the object with a dictionary of words.
boolean isUnique(string word): Returns true if either of the following conditions are
                               met (otherwise returns false):
                               1) There is no word in dictionary whose abbreviation is
                                  equal to word's abbreviation.
                       2) For any word in dictionary whose abbreviation is equal
                                  to word's abbreviation, that word and word are the same.

Example 1:
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear");   # return false, dictionary word "deer" and word "dear" have
                                  # the same abbreviation "d2r" but are not the same.
validWordAbbr.isUnique("cart");   # return true, no words in the dictionary have the abbreviation "c2t".
validWordAbbr.isUnique("cane");   # return false, dictionary word "cake" and word "cane" have the same
                                  # abbreviation "c2e" but are not the same.
validWordAbbr.isUnique("make");   # return true, no words in the dictionary have the abbreviation "m2e".
validWordAbbr.isUnique("cake");   # return true, because "cake" is already in the dictionary and no other
                                  # word in the dictionary has "c2e" abbreviation.


Constraints:
1 <= dictionary.length <= 3 * 10^4
1 <= dictionary[i].length <= 20
dictionary[i] consists of lowercase English letters.
1 <= word.length <= 20
word consists of lowercase English letters.
At most 5000 calls will be made to isUnique.
"""




from typing import List


"""
使用 Map 保存缩写和原单词的映射, 判断输入的单词的缩写是否在 Map 中;
"""
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.dict_abbr = {}

        for word in dictionary:
            # jy: 获取单词的缩略格式;
            abbreviation = self._get_abbreviation(word)
            # jy: 如果单词的缩略格式已在字典中, 则将其加入该缩略词对应的字典; 如果不在则初始化;
            if abbreviation in self.dict_abbr:
                self.dict_abbr[abbreviation].add(word)
            else:
                self.dict_abbr[abbreviation] = {word}



    def isUnique(self, word: str) -> bool:
        abbreviation = self._get_abbreviation(word)
        # jy: 如果单词的缩略格式不在字典中, 则返回 True
        if abbreviation not in self.dict_abbr:
            return True
        # jy: 如果单词缩略词在字典中, 且该缩略词对应的单词有且只有该词, 则返回 True
        elif word in self.dict_abbr[abbreviation] and len(self.dict_abbr[abbreviation]) == 1:
            return True
        else:
            return False


    def _get_abbreviation(self, word):
        """ 返回单词的缩略格式 """
        if len(word) <= 2:
            return word

        return word[0] + str(len(word) - 2) + word[-1]


validWordAbbr = ValidWordAbbr(["deer", "door", "cake", "card"])

# jy: return false, dictionary word "deer" and word "dear" have the same abbreviation
#    "d2r" but are not the same.
print(validWordAbbr.isUnique("dear"))

# return true, no words in the dictionary have the abbreviation "c2t".
print(validWordAbbr.isUnique("cart"))

# jy: return false, dictionary word "cake" and word "cane" have the same abbreviation
#    "c2e" but are not the same.
print(validWordAbbr.isUnique("cane"))

# return true, no words in the dictionary have the abbreviation "m2e".
print(validWordAbbr.isUnique("make"))

# jy: return true, because "cake" is already in the dictionary and no other word in the
#    dictionary has "c2e" abbreviation.
print(validWordAbbr.isUnique("cake"))


