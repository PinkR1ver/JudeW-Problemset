# Brute force
连续计算斜率，判断断点; 
在面对高精度时，不使用float类型来解，使用Fraction库保存rational类。保证高精度；
rational的实现 - 猜测使用gcd来保证

![Alt text](./attachments/image.png)

# 高精度算法
...

# 交叉相乘
计算slope会遇到高精度问题，使用交叉相乘来判断前后是否连线

![Alt text](./attachments/image-1.png)