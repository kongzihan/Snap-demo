import snap
# 快速测试以确认gnuplot有效
# Gnuplot用于绘制网络的结构特性（例如度分布）
G = snap.GenPrefAttach(100000, 3)
G.PlotInDegDistr("pref-attach", "PrefAttach(100000, 3) in Degree")
