# Method

## [1. Simulation](./simulation.py)

Simulate the processing is very time-consuming. It can not pass the leet-code for "Time Limite Exceeded"

## Instruction from [leetcode.cn](https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/solution/shi-zi-fu-chuan-you-xu-de-zui-shao-cao-z-qgra/)

### Lemma We need Know

#### 排列数计算

假设有$a_0$个物品0，$a_1$个物品1，$\cdots$，$a_{n-1}$个物品n-1，我们把他们排成一排，则方案数为：
$$
\frac{(a_0 + a_1 + \cdots a_{n-1}!)}{a_0!a_1!\cdots a_{n-1}!}
$$


