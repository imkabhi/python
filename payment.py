import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from course import course

def payment():
    print('this is my payment file')

course.course()