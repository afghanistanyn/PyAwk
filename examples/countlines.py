#!/usr/bin/env python3.3
from pyawk import PyAwk, p
class CountLines(PyAwk):

    def end(self):
        self.print(self.NR)

if __name__ == '__main__':
    CountLines().run()
