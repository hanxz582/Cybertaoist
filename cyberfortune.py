#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

print("开始后一定要想着自己要问什么")
input("按回车键开始算命")
bengua = []
coin = []
for _ in range(6):
    for _ in range(3):
        random_num = random.randint(0, 1)
        coin.append(random_num)
    if coin == [0,0,0]:
        bengua.append("老阴") 
    elif coin == [1,1,1]:
        bengua.append("老阳")
    else:
        x = Counter(coin).most_common(1)
        if x[0][0] == 0:
            bengua.append("阳爻")
        else:
            bengua.append("阴爻")
    coin = []
print(f"本卦：{bengua}")
biangua = []
for x in bengua:
    if x == "老阴":
        biangua.append("少阳")
    elif x == "老阳":
        biangua.append("少阴")
    else:
        biangua.append(x)
print(f"变卦：{biangua}")


#生成图
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False

yao_types = {
    '阴爻': {'color': '#1166bb', 'style': 'broken'},
    '少阴': {'color': '#1155AA', 'style': 'broken'},
    '少阳': {'color': '#CCAA44', 'style': 'solid'},
    '老阴': {'color': '#113399', 'style': 'broken'},
    '老阳': {'color': '#BB8822', 'style': 'solid'},
    '阳爻': {'color': '#DDAA00', 'style': 'solid'}
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
for ax in [ax1, ax2]:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

y_step = 0.8 / 6
start_y = 0.1

for i, yao in enumerate(bengua):
    y = start_y + i * y_step
    info = yao_types[yao]
    if info['style'] == 'solid':
        ax1.add_patch(Rectangle((0.25, y), 0.5, 0.05, facecolor=info['color']))
    else:
        ax1.add_patch(Rectangle((0.25, y), 0.2, 0.05, facecolor=info['color']))
        ax1.add_patch(Rectangle((0.55, y), 0.2, 0.05, facecolor=info['color']))

for i, yao in enumerate(biangua):
    y = start_y + i * y_step
    info = yao_types[yao]
    if info['style'] == 'solid':
        ax2.add_patch(Rectangle((0.25, y), 0.5, 0.05, facecolor=info['color']))
    else:
        ax2.add_patch(Rectangle((0.25, y), 0.2, 0.05, facecolor=info['color']))
        ax2.add_patch(Rectangle((0.55, y), 0.2, 0.05, facecolor=info['color']))

plt.tight_layout()
plt.savefig('hexagrams.png', dpi=300)
plt.show()     
print("解卦把hexagrams.png给AI看")


