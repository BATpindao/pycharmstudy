"""
子进程：
很多时候，子进程并不是自身，而是一个外部程序，我们创建了子进程之后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便的启动一个子进程，然后控制其输入输出
"""

"""
subprocess 是 Python 标准库
用于创建和管理系统级子进程
"""
import subprocess

print('$ nslookup www.python.org')
#                         命令         参数
r = subprocess.call(['nslookup', 'www.python.org'])
"""
解读：
nslookup:网络查询工具 （查询域名 DNS信息）
www.python.org：要查询的域名
列表格式：第一个元素是命令，后面是参数

call()方法特点：
    。阻塞式执行：等待命令完成才继续
    。返回退出代码（exit code）
    。直接输出到终端（继承父进程的输入输出）
"""
print('出口代码:', r)
"""
退出代码含义：
    0:执行成功
    非0:执行失败
"""

"""
$ nslookup www.python.org
Server:		114.114.114.114
Address:	114.114.114.114#53

Non-authoritative answer:
www.python.org	canonical name = dualstack.python.map.fastly.net.
Name:	dualstack.python.map.fastly.net
Address: 167.82.0.223

出口代码: 0
"""
