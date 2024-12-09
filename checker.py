# SPDX-License-Identifier: MIT
# 
# Copyright (c) 2024 Egor Solyanik
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import subprocess
import sys
import os


def main():
    programs = sys.argv[1:]
    exes = []
    compiles = []
    for program in programs:
        if program[-3:] == ".py":
            exes.append(['python3 ' + program, program])
        elif program[-4:] == ".cpp":
            compiles.append('clang++ ' + program + ' -o ' + program[:-4] + '.out')
            exes.append(['./' + program[:-4] + '.out', program])
        elif program[-5:] == ".java":
            compiles.append('javac ' + program)
            exes.append(['java ' + program[:-5], program])
        elif program[-6:] == ".class":
            exes.append(['java ' + program[:-6], program])
        elif program[-4:] == ".out" or program[-2:] == ".a":
            exes.append(['./' + program, program])
        elif program[-4:] == ".exe":
            if os.name == 'nt':
                exes.append(['./' + program, program])
            elif os.name == 'posix':
                exes.append(['WINEDEBUG=fixme-all wine ' + program, program])
            else:
                print("Unknown os: " + os.name)
                sys.exit(1)
        else:
            print("Unknown file type: " + program)
            sys.exit(1)
    for compile_str in compiles:
        subprocess.run(compile_str, shell=True)
    # loop files in tests directory
    for root, dirs, files in os.walk("tests"):
        for file in files:
            if file == ".keep":
                continue
            results = []
            for exe in exes:
                subprocess.run(f'{exe[0]} --asm tests/{file} --bin tests/out/{exe[1]}.txt',
                               shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                results.append(open(f'tests/out/{exe[1]}.txt').read().strip())
            if all(results[0] == result for result in results):
                print(f"PASS: {file}")
                if os.name == 'nt':
                    subprocess.run(f'del tests\\out\\*', shell=True)
                else:
                    subprocess.run(f'rm tests/out/*', shell=True)
            else:
                print(f"FAIL: {file}. See tests/out/ for details.")
                return


if __name__ == "__main__":
    main()
