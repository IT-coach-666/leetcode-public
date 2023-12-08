
"""
参考:
https://blog.csdn.net/ANNILingMo/article/details/80879910

字典树/前缀树(Trie): N 叉树的一种特殊形式;

"""

import collections


class TrieNode(object):
    def __init__(self):
        # jy: 子节点的类型也为 TrieNode 类型, 故使用默认值为 TrieNode 的字典表示(使用普通字
        #     典也可以, 因为带有默认值的字典也并不会对该属性进行约束, 只是更直观明确而已)
        # self.children = collections.defaultdict(TrieNode)
        self.children = {}
        # jy: 用于判断前缀树中截止当前 TrieNode 节点对应的字符为止是否为一个有效的单词;
        self.end_of_word = False


class Trie_v1(object):
    def __init__(self):
        # jy: 定义 Trie 树的根节点为一个 TrieNode, 该 TrieNode 的 self.children 属性将用于存
        #     放不同单词的前缀;
        # jy: 此处也可将 TrieNode 中的两个初始化属性直接搬过来, 因此可以减少 TrieNode 节点类
        #     的定义, 但节点不再是 TrieNode 类后(而是一个简单的 {...}), 则判断某个字符是否是
        #     单词的末尾字符时, 不再能依赖原先的字符节点 TrieNode 的 end_of_word 属性, 而是需
        #     要通过字符对应的 {...} 中添加指定的标签来标记(参加 Trie_v2 的代码实现);
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        # jy: 逐个遍历要插入的单词中的字符;
        for char in word:
            # jy: 判断截止单词 word 的当前字符 char 为止对应的前缀是否存在于字典树中, 如果存在, 则
            #     不断递进 word 中的字符(即扩大前缀的长度)并判断, 直到当前字符不在字典树中, 则将该
            #     字符插入到当前字典树节点的子节点中(字典树的叶子节点对应的 children 属性为 {}, 而
            #     end_of_word 属性为 True);
            # jy: 注意, 此处必须调用字典的 get() 方法, 因为 char 可能不止字典树中;
            child = node.children.get(char)
            # jy: 如果当前字符 char 不在上一个字符对应的 TrieNode 的 children 属性中, 则将其加入到
            #     上一个字符对应的 TrieNode 的 children 属性中;
            if not child:
                node.children[char] = TrieNode()
            node = node.children[char]
        # jy: 以上 for 循环全部执行完成后, node 为单词 word 最后一个字符对应的 TrieNode, 因此将该
        #     TrieNode 的 end_of_word 标记为 True, 表名截止该字符有一个真正的单词存在;
        # jy: 注意, 此时的 TrieNode 的 children 属性值不一定是空字典, 因为该单词 word 可能是其它单
        #     词的前缀, 此时的整个字典树中, 单词 word 的最后一个字符(当前字符)的 children 属性值依
        #     然保留了其它字符;
        node.end_of_word = True

    def search(self, word):
        """
        判断字典树中是否存在单词 word
        """
        node = self.root
        # jy: 循环遍历单词 word 中的每个字符, 需确保这些字符依次存在于字典树的根节点不
        #     断向下深度遍历中, 且遍历至 word 的最后一个字符时, 该字符对应的 TrieNode 的
        #     end_of_word 属性值为 True (表明有以该字符结尾的单词存在);
        for char in word:
            node = node.children.get(char)
            if not node:
                return False
        # jy: 以上 for 循环遍历完成后, node 即为 word 中最后一个字符对应的 TrieNode, 如果其
        #     end_of_word 属性值为 True, 表明字典树中存在单词 word (否则表明没有 word 单词存
        #     在, 即 word 仅仅是某些单词的一个前缀而已);
        return node.end_of_word

    def startsWith(self, prefix):
        """
        判断字典树中是否存在前缀为 prefix 的单词
        """
        node = self.root
        # jy: 逻辑类似于从字典树中查找单词 word, 只是此处查找的是前缀 prefix, 由于是查找前缀,
        #     只需要确保 prefix 对应的字符依据先后顺序均存在于字典树的深度遍历路径中, 并不需
        #     要判断 prefix 的最后一个字符是否是单词的末尾(如果 prefix 中的字符依据先后顺序均
        #     存在于字典树的深度遍历路径中, 则直接返回 True 即可);
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return False
        return True

    def prefix_words(self, prefix):
        """
        获取字典树中所有前缀为 prefix 的单词, 没有则返回 []; (在 startsWith 的基础上进行修改即可)
        """
        ls_prefix_words = []
        # jy: 判断前缀 prefix 是否存在, 如果不存在, 则直接返回 []
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return ls_prefix_words

        # jy-version-1-Begin --------------------------------------------------
        """
        # jy: 如果前缀 prefix 的最后一个字符对应的 TrieNode 的 end_of_word 属性为 True, 表明
        #     该前缀也对应一个完整的单词存在于字典树中, 将其加入列表;
        if node.end_of_word:
            ls_prefix_words.append(prefix)

        def _dfs(node, ls_, prefix):
            '''
            深度优先遍历, 获取前缀为 prefix 的所有单词并加入到列表 ls_ 中;
            node 对应前缀 prefix 的最后一个字符对应的 TrieNode 类;
            '''
            # jy: 循环遍历 node 的所有子节点, 判断子节点对应字符与当前 prefix 构成的新前
            #     缀(即 prefix + char)是否为一个完整的单词, 如果是则加入到列表, 随后继续
            #     在该子节点的基础上深度优先遍历;
            for char, child_node in node.children.items():
                if child_node.end_of_word:
                    ls_.append(prefix + char)
                _dfs(child_node, ls_, prefix + char)
        """
        # jy-version-1-End ----------------------------------------------------
        # jy-version-2-Begin --------------------------------------------------
        def _dfs(node, ls_, prefix):
            '''
            深度优先遍历, 获取前缀为 prefix 的所有单词并加入到列表 ls_ 中;
            node 为前缀 prefix 的最后一个字符对应的 TrieNode 类;
            '''
            # jy: 如果前缀 prefix 的最后一个字符对应的 TrieNode 类的 end_of_word 属性为 True;
            #     表明字典树中存在 prefix 单词, 因此将其加入到列表 ls_ 中;
            if node.end_of_word:
                ls_.append(prefix)
            # jy: 遍历 node 节点的所有子节点, 将子节点对应的字符加到 prefix 后进行递归判断;
            for char, child_node in node.children.items():
                _dfs(child_node, ls_, prefix + char)
        # jy-version-2-End ----------------------------------------------------

        _dfs(node, ls_prefix_words, prefix)

        return ls_prefix_words


class Trie_v2:
    def __init__(self):
        self.root = {}
        # jy: 此处的 self.word_end 仅仅作为一个标记符合, 其值可以是任何一个 hashable 类型且与 word
        #     中的字符没有交集的值(由于字典树中每个节点均为一个字符, 因此 self.word_end 可以是其它
        #     非字符类型的 hashable 类型的值, 也可以是字符子串, 只要能明确与字典树中的字符区分开即可),
        #     因为后续可能将其作为 dict 中的 key 插入; 在字典树中, 如果当前字符 char 为某个单词
        #     的末尾字符, 则其对应的字典格式为: {char: {self.word_end: True, ...}}, 其中键值 char
        #     对应的 {self.word_end: True, ...} 除了 self.word_end 键值外不一定就没有其它键值, 如果以
        #     字符 char 结尾的单词 word 是其它单词的前缀, 则就包含了其它键值;
        self.word_end = -1
        # self.word_end = 0
        # jy: 如果 self.word_end 为 "a", 则插入 ["a", "aa"] 时会产生冲突; 类似的, 如果 self.word_end
        #     为 "f", 则插入 ["af", "aff"] 时会产生冲突;
        # self.word_end = "a"
        # self.word_end = "f"

    def insert(self, word):
        """
        在字典树中插入单词 word
        """
        cur_node = self.root
        # jy: cur_node 为一个保存有键值为 char 的字符的字典: {char: {}}
        for char in word:
            if char not in cur_node:
                cur_node[char] = {}

            cur_node = cur_node[char]
        # jy: cur_node 为一个字典 {...}, 其不一定为空字典, 如果单词 word 在字典树中作为其它单词的
        #     前缀, 则 key 为最后一个字符 char 的对应 value 就不是空字典, 会是一个包含了其它字符的
        #     字典, 最后在该字典中加入 key 为 self.word_end 且对应的 value 为 True 的记录, 表明指向
        #     该字典的 char 是一个单词的末尾字符;
        # jy: 注意, 此处 key 为 self.word_end 对应的 value 不一定非要是 True, 可以是任何类型的值, 因
        #     为后续判断 char 是否是某单词的末尾时, 只需要判断 self.word_end 是否在 char 对应的字典
        #     中即可;
        cur_node[self.word_end] = True

    def search(self, word):
        """
        在字典树中查找单词 word
        """
        cur_node = self.root
        for char in word:
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        # jy: 最终的 cur_node 是 word 中最后一个字符所指向的 {...}, 如果 char 对应的 {...} 中包含了
        #     self.word_end, 则表明 word 存在于字典树中;
        return self.word_end in cur_node

    def startsWith(self, prefix):
        """
        判断字典树中是否存在以 prefix 为前缀的单词
        """
        # jy: 类似在字典树中查找 word, 但不需要判断 prefix 的最后一个字符是否是单词的末尾, 如果从开
        #     始到最后一个字符均在字典树的深度遍历路径下, 即表明该前缀存在;
        cur_node = self.root
        for char in prefix:
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        return True


# trie_tree = Trie_v2()
trie_tree = Trie_v1()
# ls_words = ["apple", "app_03", "app_01", "app2_02", "subject", "sub"]
ls_words = ["a", "aa", "aff", "b", "c", "d", "e"]
ls_prefix = ["ap", "app", "sub"]
for word in ls_words:
    trie_tree.insert(word)

print(trie_tree.search("a"))
print(trie_tree.prefix_words("a"))
print(trie_tree.search("f"))
print(trie_tree.startsWith("app2"))
print(trie_tree.root)


