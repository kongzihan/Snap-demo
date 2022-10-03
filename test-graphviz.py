# import snap
# # 一个快速测试，以确认 Graphviz 是否有效
# # Graphviz用于绘制和可视化小图
# G = snap.GenGrid(snap.PUNGraph, 5, 3)
# G.DrawGViz(snap.gvlDot, "grid5x3.png", "Grid 5x3")

from graphviz import Digraph

dot = Digraph(comment='The Test Table')
# 添加圆点A,A的标签是Dot A
dot.node('A', 'Dot A')
# 添加圆点 B, B的标签是Dot B
dot.node('B', 'Dot B')
# dot.view()
# 添加圆点 C, C的标签是Dot C
dot.node(name='C', label= 'Dot C',color='red')
# dot.view()

# 创建一堆边，即连接AB的两条边，连接AC的一条边。
dot.edges(['AB', 'AC', 'AB'])
# dot.view()
# 在创建两圆点之间创建一条边
dot.edge('B', 'C', 'test')
# dot.view()

# 获取DOT source源码的字符串形式
print(dot.source)
dot.view()
dot.render('test-table.gv', view=True)
