# APDOCC - A Python Dictionary of Color Combinations

The book ['A Dictionary of Color Combinations' by Sanzo Wada](https://www.amazon.com/Dictionary-Color-Combinations-Various/dp/4861522471) contains a collection of beautifully crafted color combinations. 
This repository creates a digital version of that version that can be used digitally and  is basically a less polished version of the repository ['sanzo-wada' by dblodorn](https://github.com/dblodorn/sanzo-wada).
 

## How to use

The main files are `combinations.json` and `colors.json`.
Loading them as `combinations` and `colors` respectively, the usage is as follows:


```
>>>combinations[4] # note that '4' is the key of the dict. 
[50, 148] # combination '4' is composed of colors '50' and '148'

>>>colors[50] # check out color '50'
{'name': 'Isabella Color',
 'cmyk': [15, 28, 60, 10],
 'combinations': [4, 12, 241, 292],
 'rgbfloat': (195.07500000000002, 165.24, 91.8),
 'rgb': [195, 165, 91],
 'hex': '#c3a55b',
 'index': 51}
```

There are a total of 348 combinations and 157 different colors. Combinations contain one, two, three, four, or five colors. 

