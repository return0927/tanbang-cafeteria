# -*- coding: utf-8 -*-
from setuptools import setup


try:
   with open('README.md') as f:
       readme = f.read()
except IOError:
   readme = ''


setup(
   name="tanbang-cafeteria",
   version='0.1.2',
   py_modules=['tCafeteria'],
   author='w3bn00b',
   author_email='powderbanana@gmail.com',
   url='https://github.com/w3bnoob/tanbang-cafeteria',
   description="Meal and schedule crawler for korean middle school",
   long_description=README.md,
   install_requires=["requests", "bs4"],
)
