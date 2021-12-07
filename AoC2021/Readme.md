# Advent of Code 2021 Puzzles 
[Advent of Code 2021](https://adventofcode.com/2021)

## Day 7 
The median minimises the L1 norm of the distances (i.e. the fuel cost for part 1), and the mean minimises the L2 norm (sum of squared distances). The fuel cost for part 2 is sum(dist*(dist+1)/2), i.e. the average of the L1 and L2 norms of the distances. We can reason that the best alignment position will be between the mean and the median, because when moving outside of that interval both the L1 and L2 norms will be increasing. [julia](https://www.reddit.com/r/adventofcode/comments/rar7ty/2021_day_7_solutions/hnkbtug/?utm_source=share&utm_medium=web2x&context=3)
