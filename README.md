# What is this?

Files and notes I used to compile [VLang](https://github.com/vlang/v) compiler, `v.exe` in the following context, in MSYS2/MingW64 on my Ms Windows 7 64bits.



# Why not fork [VLang](https://github.com/vlang/v), edit then ask for merging?

There is something bad for my Internet connection, so it takes too long when I try to fork&edit some files every time.



# Why not report bugs in [issues](https://github.com/vlang/v/issues)? Or why write your own scripts?

I did report.

However, [VLang](https://github.com/vlang/v) is so eager to succeed to prove that its propaganda is not false, hence its code is changed and released frequently on [VLang](https://github.com/vlang/v). However, some codes are submitted without thorough test; as a result, the behavior of `v.exe` changes from time to time, for example, [examples/tetris/tetris.v can't be compiled any more](https://github.com/vlang/v/issues/825) (which is solved now though); or more worse, the new `v.exe` totally fails to compile any `.v` sources with the code after July 27th, 2019. (Please see the next section for details).

In order to [save my time](https://github.com/vlang/v/issues/827), I stopped checking [VLang](https://github.com/vlang/v) manually, on the other hand I wrote scripts to download/build/test [VLang](https://github.com/vlang/v) in an automatic way.



# I was banned from posting on [VLang](https://github.com/vlang/v)'s [issues](https://github.com/vlang/v/issues)

On July 27th, 2019, I reported the problem( `v.exe compiles nothing in msys2`) as a bug in [issues](https://github.com/vlang/v/issues). In the report, the latest cloned [VLang](https://github.com/vlang/v) sources are used like I always do, official template are filled in details; I also pointed out that `v.exe` from days ago can compile without problem. Then a user told me that I should `copy log.v to the directory where v.exe lives`, then `do not use msys2, instead use dos prompt`.  The suggestions do not work for MSYS2, and ignore the fact that previous `v.exe` works without problem which I have addressed in the report. I said again [please do thorough test before any release!!!](https://github.com/vlang/v/issues/827) in the report.

**Then the most funny thing happened: the report is deleted; and further more, I was banned** from posting on [VLang](https://github.com/vlang/v)'s [issues](https://github.com/vlang/v/issues).

TLDR, the following is what I met in MSYS2

```bash
$ git clone https://github.com/vlang/v
makeCloning into 'v'...
remote: Enumerating objects: 4208, done.
remote: Total 4208 (delta 0), reused 0 (delta 0), pack-reused 4208
Receiving objects: 100% (4208/4208), 2.08 MiB | 37.00 KiB/s, done.
Resolving deltas: 100% (2669/2669), done.

$ cd v

$ make
rm -f v.c .v.c v vprod thirdparty/**/*.o
find . -name '.*.c' -print0 | xargs -0 -n1 rm -f
curl -Os https://raw.githubusercontent.com/vlang/vc/master/v.c
cc -std=gnu11 -w -o v v.c -lm
./v -o v compiler
V 0.1.16
Use Ctrl-C or `exit` to exit
>>> V has been successfully built

$ ./v examples/hello_world.v
V 0.1.16
Use Ctrl-C or `exit` to exit
>>>

$ ls examples/*.exe
ls: cannot access 'examples/*.exe': No such file or directory
```



# The temporary solution to the problem( `v.exe compiles nothing`)

In `Makefile`, the line 

`${CC} -std=gnu11 -w -o v v.c -lm` 

should be replaced with 

`${CC} -std=gnu11 -DUNICODE -D_UNICODE -w -o v v.c -lm`

In fact this is the idea from `make.bat`. But `Makefile` can be used in MSYS2, or dos prompt; however `make.bat` can only be used in dos prompt.

I named it a `temporary` solution because I don't know 

1. why `-DUNICODE -D_UNICODE` must be used on Windows; does this mean, no Unicode-related function is available on Linux/Mac Osx/...?
2. will `-DUNICODE -D_UNICODE` produce bad compiler on Linux/Mac Osx/...?

Maybe OS-specified statement can be written in `Makefile`, but it is out of my knowledge.



# Why not use `make.bat` in dos prompt?

Currently, `make.bat` calls `gcc` to perform the operation. MSYS2/MingW64 is a better environment for `gcc` to my opinion.



# How to use the scripts to compile  [VLang](https://github.com/vlang/v) in MSYS2/MingW64?

1. install python3,
2. modify `checkit.py`, `compileDemo.py`, `patchit.py` and `v.sh` according to your file-system,
3. run `./v.sh`, then you will get `v.exe` under directory `v`.



# Why there are so many commented out lines in  `patchit.py`?

I began to write the scripts in the end of June, 2019. All the lines are necessary to make 

1. `v.exe` can be compiled , or

2. `v.exe` can compile, for example `examples/tetris/tetris.v` to `examples/tetris/tetris.exe`

in MSYS2/MingW64. 

Since time passed, some code in `patchit.py` are not necessary, so I commented them out; new bug appears, so I added new code. I hope one day, no patch is need anymore.



# Why not use `make test`

Because it does not compile examples in `examples/hot_code_reloading` with `-live` option.



# Why check which EXE has been made?

If the compiler can not even generate an EXE file, we can not check the result of the EXE file. So this must be the first place.



# Why do you learn [VLang](https://github.com/vlang/v)?

[VLang](https://github.com/vlang/v)'s slogan sounds great; especially simplicity/fast compilation/high performance/powerful UI seems to meet my need. 



# When will you and how do you use [VLang](https://github.com/vlang/v)?

That is hard to say, because 

1. [VLang](https://github.com/vlang/v) is far from mature, just as [the official page](https://vlang.io/) says, v 1.0 is planned for December 2019. But we all know it is just a plan.
2. I need to do scientific calculation and representation, which do not live in [VLang](https://github.com/vlang/v)'s world yet. 
3. Further more, there is still bugs in [VLang](https://github.com/vlang/v).



# Bugs till July 28th, 2019

I found at least these bugs:

## bug 1, #IND

```bash
$ ./examples/spectral.exe
-1.#IND00000
```

## bug 2, mystic dot

No matter I build `v.exe` in MSYS2 or dos prompt, then

in dos prompt

```cmd
R:\v>v examples\hello_world.v
failed to create .examples\hello_world.c
gcc: error: .examples\hello_world.c: No such file or directory
gcc: fatal error: no input files
compilation terminated.
V panic: clang error

R:\v>v .\examples\hello_world.v
failed to create ..\examples\hello_world.c
gcc: error: ..\examples\hello_world.c: No such file or directory
gcc: fatal error: no input files
compilation terminated.
V panic: clang error

R:\v>v r:\v\examples\hello_world.v
failed to create .r:\v\examples\hello_world.c
gcc: error: .r:\v\examples\hello_world.c: Invalid argument
gcc: fatal error: no input files
compilation terminated.
V panic: clang error

```



However, in MSYS2

```bash
$ ./v examples/hello_world.v

$ examples/hello_world.exe
Hello, World!

```



## bug 3, `SO` on windows

```bash
$ ./v -live examples/hot_code_reloading/graph.v

$ ls examples/hot_code_reloading/graph.*
examples/hot_code_reloading/graph.exe  examples/hot_code_reloading/graph.v
examples/hot_code_reloading/graph.so

```

but `graph.so` is actually a DLL file

```bash
$ file examples/hot_code_reloading/graph.so
examples/hot_code_reloading/graph.so: PE32+ executable (DLL) (console) x86-64, for MS Windows

```

luckly this is not a big problem since `graph.exe` tries to load `graph.so`

```bash
$ mv examples/hot_code_reloading/graph.so examples/hot_code_reloading/graph.dll

$ examples/hot_code_reloading/graph.exe
open failed

```



## bug 4, `Segmentation fault` of examples in `hot_code_reloading` directory

```bash
$ mv examples/hot_code_reloading/graph.dll examples/hot_code_reloading/graph.so

$ examples/hot_code_reloading/graph.exe
Segmentation fault

```



# bug 5, `news_fetcher` and `links_scraper` fail

But I remember they can fetch some information before.

```bash
$ /r/v/examples/news_fetcher.exe
HttpOpenRequest() failed
failed to fetch topstories.json
Error in decode() for array_int error_ptr=: %s

$ /r/v/examples/links_scraper.exe
HttpOpenRequest() failed

```

# Bonus(?), how to use DLL created by [VLang](https://github.com/vlang/v)

This is a weird solution:

1. create `fib_v.v` 

```go
module main

import os
import time

[live]
fn fib(x int) int{
    if x <=1 {
        return 1
    }
    else {
        return fib(x-1) + fib(x-2)
    }
}

fn main() {
}


```

2. compile `fib_v.v` 

```bash
$ ./v -live fib_v.v

$ mv fib_v.so fib_v.dll

```

3. python code `fib_py.py`

```python
import ctypes, time

def fib_py(x):
    if x <=1 :
        return 1
    else:
        return fib_py(x-1) + fib_py(x-2)

fib_v = ctypes.CDLL('fib_v.so').fib

st = time.time()
ans1 = fib_py(40)
et = time.time()
t1 = et - st

st = time.time()
ans2 = fib_v(40)
et = time.time()
t2 = et - st

print(ans1)
print(ans2)
print(t1)
print(t2)


```

4. the result of `fib_py.py`

```
165580141
165580141
64.11766743659973
158.59907150268555
```

yes, `fib_v.fib` needs more time then `fib_py` does. But I think it is because the generated DLL/SO by `-live` is not optimized for normal DLL/SO file. So we have to wait for `true dll compiler` function, if there will be one.