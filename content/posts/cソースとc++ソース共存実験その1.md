---
title: CソースとC++ソース共存実験(その1)
date: '2010-08-08T07:31:00+09:00'
slug: cソースとc++ソース共存実験その1
tags:
- C++
- C言語
draft: false
disqus_identifier: 2010-08-08-csosutocsosugong-cun-shi-yan-sono1
cover:
  image: /images/covers/uncategorized.jpg
  alt: CソースとC++ソース共存実験(その1)
---

CソースとC++ソースの共存を実験してみた。
とは言っても、printf()とcout&lt;&lt; を同時に使ってみただけ。

同時に使えるんですね。まずは、第一歩。

`$ cat c_cpp_test.cpp #include #include using namespace std;`

int main()
{
printf("Hello, world\\n");
cout &lt;&lt; "Hello, world2\\n";

return 0;
}
\$ g++ c\_cpp\_test.cpp
\$ ./a.out
Hello, world
Hello, world2
\$

続きがあるのか？は未定w
