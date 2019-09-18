# PythonExerciseBook
用python期间的一些小脚本，和写脚本期间涉及的技术小点。

## python commandline

  exit()
  
  jupyter notebook
  
## Jupyter Notebook操作问题

  + cell运行顺序问题 ：需要重启jupyter.
  
  + OS Error : engine = 'python'

##  数据清洗
+ Regex 基本匹配符 [菜鸟教程](https://www.runoob.com/python/python-reg-expressions.html) 

+ pandas 

    + df操作[全](https://chf2012.github.io/2017/05/17/%E8%BD%AF%E4%BB%B6%E5%BA%94%E7%94%A8_%E7%A8%8B%E5%BA%8F%E7%BC%96%E7%A8%8B/Python/Python_%E4%B8%93%E9%A2%98%E6%80%BB%E7%BB%93/Python_%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86_pandas_old/)
   
    + 细化到单元格的清洗 df.iterrow loc/at
      - [参考同学写脚本的方式](https://github.com/Ddd1101/BGP_1)
      - [最佳实践](https://github.com/pandas-dev/pandas/issues/15269) 以及根据最佳实践自己的尝试：[脚本](https://github.com/A-ZHANG1/PythonExerciseBook/blob/master/cleaner.py) [jupyter](https://github.com/A-ZHANG1/PythonExerciseBook/blob/master/regexCleaner.ipynb)
      - [操作方式列表](https://blog.csdn.net/qimiejia5584/article/details/78565953)
      
      修改单元格的值 df.set_value(idx, colName, newValue)

    + pandas re模块
      1. re.match(pattern, string)从头开始匹配
      2. re.search(pattern, string)从任意位置开始匹配
      
    + 字符串模糊匹配 
      1. 编辑距离（动归）
      2. fuzzywuzzy库 leskov距离
      3. 通过regex及pattern matching
      
    + pandas group count 等基本数据分析操作行为
      
      return None if not matched; return matched object if matched

## Crawler

药品知识图谱用到的[crawler](https://github.com/A-ZHANG1/drug/tree/master/crawler/crawler).涉及到数据库连接和类、方法的基本写法。

## Python语言问题 [61A](https://www.bookstack.cn/read/sicp-py-zh/ch5.md#5.2.5%20%E6%B5%81)
+ 层次（树形）结构 -产生于- 数据（？服务封装/类节点）的封闭性 （tuple的树形存储方式） 
+ 递归处理树形结构：将树操作降至枝干（的枝干...）操作，直到叶子节点 ？Guoqiang 某一习题
+ 递归函数均为高阶函数
+ python描述内置类函数hin清楚的[官方文档](https://docs.python.or
g/3/library/stdtypes.html#set)
...

## 基础JS

