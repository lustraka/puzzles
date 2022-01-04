# Advent of Code 2021 Puzzles 
[Advent of Code 2021](https://adventofcode.com/2021) | [MathWorld](https://mathworld.wolfram.com/)

## Contents 
- [Day 1: Sonar Sweep](AoC_01.ipynb)
	- ⭐ Part I uses `pd.Series.diff`.
	- ⭐ Part II uses `pd.Series.rolling` and `pd.query`.
- [Day 2: Dive!](AoC_01.ipynb)
	- ⭐ Part I uses `pd.DataFrame` to parse instruction and calculate a position.
	- ⭐ Part II includes a third variable *aim* into a calculation.
- [Day 3: Binary Diagnostic](AoC_01.ipynb)
	- ⭐ Part I uses `np.mean` to calculate proportions and a function to convert binary value (str) to int:
	```python
	def bin_to_int(list):
  		return int('0b'+"".join(np.array(list).astype(str)), base=2)
	```
	- ⭐ Part II needs `pd.DataFrame` and step by step filtering of rows.
- [Day 4: Giant Squid](AoC_01.ipynb)
	- ⭐ Part I uses `set.difference()` and `set.issubset()`.
	- ⭐ Part II uses `list.remove()` to remove winning boards and a couple of conditional statements to get results.
- [Day 5: Hydrothermal Venture](AoC_01.ipynb)
	- ⭐ Part I calculates overlapping horizontal and vertical lines using `np.array[np.array>1]`. Examines `np.max(axis=.)` for a multidimensional array.
	- ⭐ Part II solve same thing including diagonal lines. Includes a practice with Dürer’s magic square.
- [Day 6: Lanternfish](AoC_01.ipynb)
	- ⭐ Part I solved with a class `Laternfish` and a list `school`.
	- ⭐ Part II solved with `np.array`, `np.roll`, and `np.concatenate` (exponential population growth requires a better memory management).
- [Day 7: The Treachery of Whales](AoC_01.ipynb)
	- ⭐ Part I uses `sklearn.metrics.mean_absolute_error` and `np.median`.
	- ⭐ Part II illustrates difference between median (L1 norm - absolute value) and mean (L2 norm - squared value).
- [Day 8: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 9: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 10: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 11: ]()
	- Part I
	- Part II
- [Day 12: ]()
	- Part I
	- Part II
- [Day 13: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 14: ]()
	- ⭐ Part I
	- Part II
- [Day 15: ]()
	- ⭐ Part I
	- Part II
- [Day 16: ]()
	- Part I
	- Part II
- [Day 17: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 18: ]()
	- Part I
	- Part II
- [Day 19: ]()
	- Part I
	- Part II
- [Day 20: ]()
	- Part I
	- Part II
- [Day 21: ]()
	- ⭐ Part I
	- ⭐ Part II
- [Day 22: ]()
	- Part I
	- Part II
- [Day 23: ]()
	- Part I
	- Part II
- [Day 24: ]()
	- Part I
	- Part II
- [Day 25: ]()
	- Part I
	- Part II



## Day 2021-12-07 Reflection
After pondering various functions of `scikit-learn`, `scipy`, and `numpy.linalg` I got a key hint at *reddit*:

> The median minimises the L1 norm of the distances (i.e. the fuel cost for part 1), and the mean minimises the L2 norm (sum of squared distances). The fuel cost for part 2 is sum(dist*(dist+1)/2), i.e. the average of the L1 and L2 norms of the distances. We can reason that the best alignment position will be between the mean and the median, because when moving outside of that interval both the L1 and L2 norms will be increasing. [[julia](https://www.reddit.com/r/adventofcode/comments/rar7ty/2021_day_7_solutions/hnkbtug/?utm_source=share&utm_medium=web2x&context=3)]

Actually, it is sufficient to calculate a couple of values around the mean and return the minimum. Furthermore:
- **practice logical thinking**: sometimes I do futile mistakes when expressing ideas in the code,
- **learn about and apply algorithms**: I try to find useful functions for the task.

Anyway, I need:
- pay more attention when expressing ideas in the code, maybe write down a little more documentation including pseudocode,
- carve out proper mathematical models, such as [arithmetic series](https://mathworld.wolfram.com/ArithmeticSeries.html) in the Day 7 puzzle.

## Templates
```markdown
## [Day x](https://adventofcode.com/2021/day/x): 
### Part I
- **Unknown**: 
- **Data**: 
- **Condition**:
  - 
  - 
- **Plan**:
  - 

----

### Part II
- **Unknown**: 
- **Data**: 
- **Condition**:
  - 
  - 
- **Plan**:
  - 

```
```python
{
  "nbformat": 4,
  "nbformat_minor": 5,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.11"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dDZWBB4Ll10C"
      },
      "source": [
        "# Advent of Code Puzzles\n",
        "[Advent of Code 2021](https://adventofcode.com/2021) | [reddit/adventofcode](https://www.reddit.com/r/adventofcode/)"
      ],
      "id": "dDZWBB4Ll10C"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ri3O_1i3l2mo"
      },
      "source": [
        "import requests\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "path = 'https://raw.githubusercontent.com/lustraka/puzzles/main/AoC2021/data/'"
      ],
      "id": "ri3O_1i3l2mo",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TnFAd8h1l8NI"
      },
      "source": [
        "## [Day x](https://adventofcode.com/2021/day/x): \n",
        "### Part I\n",
        "- **Unknown**: \n",
        "- **Data**: \n",
        "- **Condition**:\n",
        "  - \n",
        "  - \n",
        "- **Plan**:\n",
        "  - \n",
        "\n",
        "----\n",
        "\n",
        "### Part II\n",
        "- **Unknown**: \n",
        "- **Data**: \n",
        "- **Condition**:\n",
        "  - \n",
        "  - \n",
        "- **Plan**:\n",
        "  - \n"
      ],
      "id": "TnFAd8h1l8NI"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HZXVSS9bl736"
      },
      "source": [
        "example = \"\"\"\"\"\""
      ],
      "id": "HZXVSS9bl736",
      "execution_count": null,
      "outputs": []
    }
  ]
}
```
