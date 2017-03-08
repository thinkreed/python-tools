#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '17/3/7'

"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def main():
    with open('./test.txt', 'r+', encoding="utf-8") as f:
        word_cloud = WordCloud(font_path="msyh.ttf").generate(f.read())
        plt.imshow(word_cloud)
        plt.axis("off")
        plt.show()


main()
