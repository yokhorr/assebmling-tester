Usage:
`python checker.py [file1.cpp] [file2.py] [file3.java] [file4.out] [file5.a] [file6.class]`

All these file formats are supported. Source files are compiled before running; .cpp files are compiled with `clang++` (if not installed, replace for `g++` or smth).
Specify as many files as you need. The results of the specified programs are compared. If at least one is different from the others, the checker stops, and you can see output for every program in [tests/out](tests/out) directory.

Tests are placed in [tests](tests) directory. By default, there are three files. Every one of them can be correctly assembled due to the laboratory work condition.
You can add your own test files to this directory.

**Please, put your source / executable files in the root directory of this project!**
