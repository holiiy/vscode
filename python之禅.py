zen_of_python = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# 移除标点符号和换行符
import string
translator = str.maketrans('', '', string.punctuation + '\n')
cleaned_zen = zen_of_python.translate(translator)

# 将字符串转换为小写，并根据空格拆分为单词列表
words = cleaned_zen.lower().split()

# 统计单词出现次数
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 按照次数进行降序排列
sorted_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}

# 输出结果
for word, count in sorted_counts.items():
    print('{}: {}'.format(word,count))
    #print(f"{word}: {count}")
    print('今年{age}岁,我在读{college}'.format(age=count,college='大学'))