import torch

# chunk将tensor切成多个元素组成的数组
# (5,5,6)  ---> [(5,5,2) , (5,5,2) , (5,5,2)]
x = torch.randn([5, 5, 6])
y = x.chunk(3, dim=-1)
print(y)