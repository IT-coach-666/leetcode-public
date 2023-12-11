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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Design-In-Memory-File-System(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a data structure that simulates an in-memory file system.
Implement the ``FileSystem`` class:

FileSystem()
    Initializes the object of the system.

List<String> ls(String path)
    The answer should in lexicographic order. If path is a file path, returns a list
    that only contains this file's name. If path is a directory path, returns the
    list of file and directory names in this directory.

void mkdir(String path)
    Makes a new directory according to the given path. The given directory path does
    not exist. If the middle directories in the path do not exist, you should create
    them as well.

void addContentToFile(String filePath, String content)
    If filePath does not exist, creates that file containing given content.
    If filePath already exists, appends the given content to original content.

String readContentFromFile(String filePath)
    Returns the content in the file at filePath.


Example 1:
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                                // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                                // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d");        // return "hello"


Constraints:
1) 1 <= path.length, filePath.length <= 100
2) path and filePath are absolute paths which begin with '/' and do not end
   with '/' except that the path is just "/".
3) You can assume that all directory names and file names only contain lowercase
   letters, and the same names will not exist in the same directory.
4) You can assume that all operations will be passed valid parameters, and users
   will not attempt to retrieve file content or list a directory or file that does
   not exist.
5) 1 <= content.length <= 50
6) At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
"""


from typing import List


"""
类似于 Trie，每个文件节点保存所有子文件的映射
"""
class File:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.content = ''
        self.files = {}

    def search(self, path):
        paths = path.split('/')
        file = self

        for i in range(1, len(paths)):
            file = file.files.get(paths[i], None)

            if not file:
                return None

        return file

    def ls(self):
        if self.is_file:
            return [self.name]
        else:
            return sorted(list(map(lambda f: f.name, list(self.files.values()))))


class FileSystem:
    def __init__(self):
        self.root = File('')

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return self.root.ls()

        file = self.root.search(path)

        return file.ls() if file else []

    def mkdir(self, path: str) -> None:
        self._make(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        file = self._make(filePath, True)
        file.content += content

    def readContentFromFile(self, filePath: str) -> str:
        file = self.root.search(filePath)

        return file.content if file else ''

    def _make(self, path, is_file):
        paths = path.split('/')
        file = self.root

        for i in range(1, len(paths)):
            files = file.files
            name = paths[i]

            if name not in files:
                file.files[name] = File(name)
            file = files[name]
        file.is_file = is_file
        return file


fileSystem = new FileSystem()
print(fileSystem.ls("/"))                                # return []
fileSystem.mkdir("/a/b/c")
fileSystem.addContentToFile("/a/b/c/d", "hello")
print(fileSystem.ls("/")                                 # return ["a"]
print(fileSystem.readContentFromFile("/a/b/c/d")         # return "hello"


# 实现文件系统类 FileSystem 供创建目录、查看目录对应的文件或子目录


