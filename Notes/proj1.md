# Proj1 Notes

## 1.make and Makefile
- Makefile文件可以将C语言的文件联合起来，指定哪些文件先编译，哪些文件后编译；可以将大的工程结合在一起，使测试和运行变的简单方便。
- 在 ubuntu 里面可以用make 来运行Makefile里面事先定义的target。
- Makefile的基本格式如下：
   ```
    target: prerequisites ...
        recipe
        ...
        ...
   ```
## 2.`printf()`, `fprintf()` and `sprintf()`    
这三个函数的使用方法基本上是一样的，不同的是`fprintf()`需要指定文件的指针，`sprintf()`需要指定字符串的指针。
用法：格式化输出

- `printf(const char *, ... )`。

- `fprintf(FILE *, const char *, ... )`。

- `sprintf(char *, const char *, ... )`。可以批量，指定格式的构造字符串。

## 3.`u_int64_t`, `uint8_t`, `long`
- 实际的应用无特殊情况，没必要用`u_int64_t` 和 `uint8_t`, 用`int`, `long` 和 `unsigned int` 就足够了。
- 这proj1使用的时候没看测试文件，导致了debug了半天。在**测试文件**里面和**代码文件**里用的变量的类型不同，导致了数据溢出。

## 4.file input/output
- 俗话说得好"百看不如一练"。刚开始学文件I/O的时候觉得这里比较麻烦一直不想用，也不做实验看看。在做proj1的时候不得不用文件的I/O结果发现，其实很简单。还是**任务驱动型学习**比较有效率。

- 用法：

- 打开文件`FILE * file = fopen(const char *filename, const char * model)`
- 读文件`fscanf(FILE *, const char *, ...)`。 和`scanf()`的用法基本一样
- 写文件`fprintf(FILE *, "%d %d\n", a, b)`。
- 关文件`fclose(FILE *)`。

## 5.C languages' `int argc` and `char *argv[]`
- 原来看见有的C语言程序在`main`函数里面写这两个参数，而有的没有写。想知道为什么，但又懒得没去找。这次正好proj1里面有这个参数就了解了解。
- 这两个参数是程序运行时就输入到程序里面的命令行参数，第一个是输入了几个参数，第二个是那几个参数的字符串形式。