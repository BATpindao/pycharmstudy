import subprocess

print('$ nslookup')

p = subprocess.Popen(['nslookup'],
                        stdin=subprocess.PIPE, # 标准的输入管道
                        stdout=subprocess.PIPE, # 标准输出管道
                        stderr=subprocess.PIPE) # 错误输出管道
"""
参数详解：
    参数                     作用           说明
    ['nslookup']             命令           只指定命令，不指定参数
    stdin=subprocess.PIPE    输入管道        ✓ 可以向子进程写入数据
    stdout=subprocess.PIPE   输出管道       ✓ 可以读取子进程的输出
    stderr=subprocess.PIPE   错误管道       ✓ 可以读取错误信息
    
call 和 Popen的区别
# ❌ call() 无法交互
subprocess.call(['nslookup', 'www.python.org'])  # 一次性执行

# ✅ Popen() 可以交互
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, ...)
# 可以分多次发送指令

"""

#发送指令并获取结果
"""
communicate() 方法：
.一次性发送所有输入给子进程
.等待子进程结束
.返回 (标准输出，错误输出) 元组
"""
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')

print(output.decode('utf-8'))

print('出口代码:', p.returncode)
