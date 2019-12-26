---
title: Python 内存管理之 `*` 运算的陷阱
date: 2019-07-10 21:05:49
tags: [python]
---

Python 中实现了 `__mul__` 魔法函数的对象，都支持 `*` 号运算。内置类型更是默认实现了该函数，使用起来也很方便。

<!-- more -->
<!-- toc -->

但是对列表对象进行 `*` 运算时，却不得不注意一个陷阱。

刚接触这个特性时，美滋滋的以为可以快速的扩展列表，比如这样。

```python
>>> a = [1] * 3
>>> a
[1, 1, 1]
>>> a[0] = 2
>>> a
[2, 1, 1]
```

看起来没什么问题，然而实际开发中没这么简单的例子，随便复杂一点，就会出现问题。

```python
>>> b = [[]] * 3
>>> b
[[], [], []]
>>> b[0].append(1)
>>> b
[[1], [1], [1]]
```

很显然出现了问题，我只是给索引位置 `0` 的元素增加了一个子元素，然后所有的元素都改变了。

出现这个问题的原因是 `*` 运算复制的不是子元素，而是当前子元素所指对象的引用，所以当改变该对象时，所有引用该对象的元素都会发生改变。

关于对象引用可以看 [Python 内存管理](/2019/06/16/python-memory-management)，里面有更详细的讲解。

再看一个现象

```python
>>> b[0] = [2]
>>> b
[[2], [1], [1]]
```

这次就想开始那个简单例子一样，结果跟我们预期的一样，这次是为什么呢？

因为我们没有改变该索引位置的对象，而是让他引向了新的对象 `[2]`，这样就不影响其他索引位置的对象了。

那么怎么才能做到扩展列表呢？答案是列表解析

```python
>>> c = [[] for i in range(3)]
>>> c
[[], [], []]
>>> c[0].append(1)
>>> c
[[1], [], []]
```