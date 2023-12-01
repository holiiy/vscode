'''
两个集合是否相等(元素相同就相等)
s1==s2 True
s1!=s2  False
一个集合是否是另一个集合的子集 
'''
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  #False
渗透 kali
