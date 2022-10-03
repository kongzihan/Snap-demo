import snap


def intro():

    # create a graph PNGraph
    # 创建一个有向图，函数用T
    G1 = snap.TNGraph.New()
    # 先添加结点，再添加边
    G1.AddNode(1)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    print("G1: Nodes %d, Edges %d" % (G1.GetNodes(), G1.GetEdges()))

    # create a directed random graph on 100 nodes and 1k edges
    # 创建一个有向随机图，100个结点，1000条边
    G2 = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    print("G2: Nodes %d, Edges %d" % (G2.GetNodes(), G2.GetEdges()))

    # traverse the nodes
    # 遍历结点，打印结点id、出度、入度
    for NI in G2.Nodes():
        print("node id %d with out-degree %d and in-degree %d" % (
            NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))

    # traverse the edges
    # 遍历边，打印边的起始点和终止点
    for EI in G2.Edges():
        print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    # traverse the edges by nodes
    # 遍历点，并打印该点作为起始点的所有边
    for NI in G2.Nodes():
        for Id in NI.GetOutEdges():
            print("edge (%d %d)" % (NI.GetId(), Id))

    # generate a network using Forest Fire model
    # 用forest fire模型生成一个神经网络
    G3 = snap.GenForestFire(1000, 0.35, 0.35)
    print("G3: Nodes %d, Edges %d" % (G3.GetNodes(), G3.GetEdges()))

    # save and load binary
    # 以二进制的形式保存和加载
    FOut = snap.TFOut("test.graph")
    G3.Save(FOut)
    FOut.Flush()
    FIn = snap.TFIn("test.graph")
    G4 = snap.TNGraph.Load(FIn)
    print("G4: Nodes %d, Edges %d" % (G4.GetNodes(), G4.GetEdges()))

    # save and load from a text file
    # 以文本的形式保存和加载
    G4.SaveEdgeList("test.txt", "Save as tab-separated list of edges")
    G5 = snap.LoadEdgeList(snap.TNGraph, "test.txt", 0, 1)
    print("G5: Nodes %d, Edges %d" % (G5.GetNodes(), G5.GetEdges()))

    # generate a network using Forest Fire model
    # 用forest fire模型生成一个神经网络
    G6 = snap.GenForestFire(1000, 0.35, 0.35)
    print("G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges()))

    # convert to undirected graph
    # 转换为无向图
    G7 = G6.ConvertGraph(snap.TUNGraph)
    print("G7: Nodes %d, Edges %d" % (G7.GetNodes(), G7.GetEdges()))
    # get largest weakly connected component of G
    # 获得最大的弱连通分量
    WccG = G6.GetMxWcc()
    # get a subgraph induced on nodes {0,1,2,3,4,5}
    # 生成子图
    SubG = G6.GetSubGraph([0,1,2,3,4])
    # get 3-core of G
    # 得到该图的3k
    Core3 = G6.GetKCore(3)
    # delete nodes of out degree 10 and in degree 5
    # 删除出度为10且入度为5的结点
    G6.DelDegKNodes(10, 5)
    print("G6: Nodes %d, Edges %d" % (G6.GetNodes(), G6.GetEdges()))

    # generate a Preferential Attachment graph on 1000 nodes and node out degree of 3
    # 生成概述优先连接图
    G8 = snap.GenPrefAttach(1000, 3)
    print("G8: Nodes %d, Edges %d" % (G8.GetNodes(), G8.GetEdges()))
    # get distribution of connected components (component size, count)
    # 连通分支分布
    CntV = G8.GetWccSzCnt()
    # get degree distribution pairs (degree, count)
    # 度分布对
    CntV = G8.GetOutDegCnt()
    # get first eigenvector of graph adjacency matrix
    # 获取图邻接矩阵的第一特征向量
    EigV = G8.GetLeadEigVec()
    # get diameter of G8
    # 获得维度
    G8.GetBfsFullDiam(100)
    # count the number of triads in G8, get the clustering coefficient of G8
    # 计算三元组数和聚类系数
    G8.GetTriads()
    G8.GetClustCf()


if __name__ == '__main__':
    intro()