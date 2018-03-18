# coding=utf-8
import ssh

# 新建一个ssh客户端对象

myclient = ssh.SSHClient()

# 设置成默认自动接受密钥

myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())

# 连接远程主机

myclient.connect("172.31.16.99", port=22, username="ec2-user",password=None,pkey="/home/ec2-user/fxemails163com.pem")

# 在远程机执行shell命令

stdin, stdout, stderr = myclient.exec_command("ls -l")

# 读返回结果
print (stdout.read())

# 在远程机执行python脚本命令

# stdin, stdout, stderr = client.exec_command("python /home/test.py")

#建立一个SSHClient对象以后，除了执行命令，还可以开启一个sftp的session，用于传输文件、创建文件夹等等。

# 新建 sftp session
sftp = myclient.open_sftp()
 
# 创建目录
 
# 从远程主机下载文件，如果失败， 这个可能会抛出异常。
#sftp.get('test.sh', '/home/testl.sh')
 
# 上传文件到远程主机，也可能会抛出异常
sftp.put('/home/ec2-user/shadowapp/conf/shadowsocks.json', '/etc/shadowsocks.json')
