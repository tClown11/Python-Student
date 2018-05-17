#-*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='dong', db='mysql', charset='utf-8')
cur = conn.cursor()
cur.execute("use wikipedia")


class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("select toPageId from links where fromPageId =%s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

#当前节点相连的page
def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}] * len(links)))
    return {}


#链接树要么为空，要么包含多个链接
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        #停止递归，返回结果
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            #若此节点页面无链接，则跳过此节点
            return {}
    cur.execute("select url from page where id = %s", (currentPageId))
    if cur.rowcount == 0:
        url = ()
    else:
        url = cur.fetchone()
    if targetPageId in linkTree.keys():
        print("target" + str(targetPageId) + "found!")
        raise SolutionFound("page:" + str(currentPageId) + " : " + str(url))

    for branchkey, branchValue in linkTree.items():
        try:
            #递归建立链接树
            linkTree[branchkey] = searchDepth(targetPageId, branchkey, branchValue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("page:" + str(currentPageId) + " : " + str(url))
        return linkTree

    try:
        searchDepth(1342, 1, {}, 4)
        print("No solution found")
    except SolutionFound as e:
        print(e.message)
