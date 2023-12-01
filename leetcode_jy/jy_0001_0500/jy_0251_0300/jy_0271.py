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
title_jy = "Encode-and-Decode-Strings(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent
over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
    # ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
    string encoded_string = encode(strs);
and Machine 2 does:
    vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.
Implement the encode and decode methods.


Example 1:
Input: dummy_input = ["Hello", "World"]

Output: ["Hello", "World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);


Example 2:
Input: dummy_input = [""]
Output: [""]


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.


Follow up:
    Could you write a generalized algorithm to work on any possible characters?
    Could you solve the problem without using any serialize methods (such as eval)?
"""

class Codec:
    """
使用 ``字符串长度 + # + 字符串`` 进行编码;
    """
    def encode(self, strs: [str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> [str]:
        """
        Decodes a single string to a list of strings.
        """
        digit = 0
        i, length = 0, len(s)
        result = []

        while i < length:
            c = s[i]
            # jy: 如果字符 c 是数字字符, 则将其转换为相应数值;
            if c.isdigit():
                digit = digit * 10 + int(c)
                i += 1
            # jy: 如果字符为 '#', 表明该字符的下一个字符开始的 digit 个字符为编码前的一个字符串, 将其
            #    加入到结果列表中, 并将 digit 置为 0, 且 i 从该字符串的末尾的下一个字符开始遍历;
            elif c == '#':
                end = i+1 + digit
                result.append(s[i+1: end])
                digit = 0
                i = end

        return result


dummy_input = ["Hello", "World"]
# Output: ["Hello", "World"]
res = Codec().encode(dummy_input)
print("encode: ", res)
res = Codec().decode(res)
print("decode: ", res)

dummy_input = [""]
# Output: [""]
res = Codec().encode(dummy_input)
res = Codec().decode(res)
print(res)

dummy_input = ["12324"]
# Output: [""]
res = Codec().encode(dummy_input)
res = Codec().decode(res)
print(res)


