# Advent of Code 2021 Puzzles 
[Advent of Code 2021](https://adventofcode.com/2021) | [MathWorld](https://mathworld.wolfram.com/)

## Contents ⭐
- [Day x : ]()
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
