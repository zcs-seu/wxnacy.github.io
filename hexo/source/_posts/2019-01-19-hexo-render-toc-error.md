---
title: Hexo 解决升级版本后渲染 Markdown TOC 不生效
date: 2019-01-19 13:57:46
tags: [hexo]
---

这两天因为升级 Node 环境到 `10.15.0` 版本，导致 Hexo 也做了升级，结果发生了意外。

<!-- more --><!-- toc -->

原来的很多文章，渲染 Markdown 文件都出现了问题，并没有渲染成相应的 `html` 代码，然而另一部分却正常。

开始以为是某些库的问题，进行了各种清除缓存重新下载的操作，依然有问题。

愁了好长时间，将没有问题的文章和有问题的一一对比，并且逐渐尝试，终于，终于找到了问题。

问题出在了 &#60;&#33;&#45;&#45; toc &#45;&#45;&#62; 上，在文章的开头我需要使用这个符号进行目录转义。

```bash
这两天因为升级 Node 环境到 `10.15.0` 版本，导致 Hexo 也做了升级，结果发生了意外。

<!-- more --><!-- toc -->
```

如果去掉中间的空行，那么就会解析错误，我认为这是 hexo 插件的 bug，不过显然我等不到它来解决了，只能手动加上了空行。

不过我查看了，我的文章中有 300 多个有问题的，额，作为一个程序猿，怎么可能手动去改呢，写个程序，将这些全部都刷上空行，搞定。

经过了这次，也算是一个小教训，以后更加需要关注的是写作规范，每行间手动加上空格，也是一个良好的编写习惯。

哎！我也只能这样安慰自己。