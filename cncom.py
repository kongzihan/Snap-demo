import snap
# 与连通分支有关函数的使用

# create a random directed graph
# 创建一个随机的有向图
G = snap.GenRndGnm(snap.PNGraph, 10000, 5000)

# test if the graph is connected or weakly connected
# 判断是强连通还是弱连通
print("IsConnected(G) =", G.IsConnected())
print("IsWeaklyConnected(G) =", G.IsWeaklyConn())

# get the weakly connected component counts
# 弱连通分支数
WccSzCnt = G.GetWccSzCnt()
for i in range (0, len(WccSzCnt)):
    print("WccSzCnt[%d] = (%d, %d)" % (
                i, WccSzCnt[i].GetVal1(), WccSzCnt[i].GetVal2()))

# return nodes in the same weakly connected component as node 1
# 返回与节点1处于同一弱连通分支中的节点数
CnCom = G.GetNodeWcc(1)
print("CnCom size = %d" % (len(CnCom)))

# get nodes in weakly connected components
# 获得每个连通分支中的所有结点
WCnComV = G.GetWccs()
for i in range(0, len(WCnComV)):
    print("WCnComV[%d] size = %d" % (i, len(WCnComV[i])))
    for j in range (0, len(WCnComV[i])):
        print("WCnComV[%d][%d] = %d" % (i, j, WCnComV[i][j]))

# get the size of the maximum weakly connected component
# 获得最大弱连通分支的大小
MxWccSz = G.GetMxWccSz();
print("MxWccSz = %.5f" % (MxWccSz))

# get the graph with the largest weakly connected component
# 得到弱连通分支最大的图
GMx = G.GetMxWcc();
print("GMx: GetNodes() = %d, GetEdges() = %d" % (
    GMx.GetNodes(), GMx.GetEdges()))

# get strongly connected components
# 打印所有强连通分支
SCnComV = G.GetSccs()
for i in range(0, len(SCnComV)):
    print("SCnComV[%d] size = %d" % (i, len(SCnComV[i])))

# get the graph representing the largest bi-connected component
# 得到表示最大双连通分支的图
GMxBi = G.GetMxBiCon()
print("GMxBi: GetNodes() = %d, GetEdges() = %d" % (
    GMxBi.GetNodes(), GMxBi.GetEdges()))
