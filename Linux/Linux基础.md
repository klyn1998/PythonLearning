## Linux指令

### 软件管理相关的命令

#### Debian平台 ==> Ubuntu

+ dpkg
+ apt
+ .deb: 基于Debian平台的软件安装包

#### Fedora平台 ==> CentOS

+ rpm：用来安装离线安装包，不会自动安装依赖
+ yum：可以离线或者在线安装软件，并且会自动安装依赖
+ .rpm: 基于Fedora平台的软件安装包

.tgz: 是一个压缩包，相当于windows里的 zip/rar

#### 安装软件的三种方式

1. 下载离线安装包：dpkg/rpm
2. 直接在线安装：apt/yum
3. 把代码的源代码下载下来，然后编译安装：下载.tgz源代码文件

#### CentOS软件安装相关命令

rpm:

+ `rpm -ivh <package_name.rpm>`：安装离线安装包；不会自动安装依赖，一般会失败

+ `rpm -qa` ：列出安装的所有包
+ `rpm -e <package_name>`：一般不会卸载成功，不会自动卸载依赖

yum: 

+ `yum install 软件名`
+ `yum list installed`
+ `yum remove 软件名`：删除软件
+ `yum check-update`：显示可用更新
+ `yum update 软件名`：用来指定更新的软件

### Linux里的目录结构

`/`：根目录

home: 家目录，管理用户

etc: 储存配置信息，重要，之后会修改

bin: 各种命令，二进制可执行文件

opt: 第三方软件可以安装到该目录

root: root用户的家目录

sbin: 超级用户命令的目录

usr: 用户安装的应用和用户文件，里面也有bin

~ : 当前用户的家目录 

### 文件(夹)相关命令的使用

`--help`：说明

#### cd

`cd -`：返回之前的位置

`cd ../`：上一级

`cd ~`：当前用户的家目录，普通用户`/home/username`，root用户`/root`

`cd`：等价于`cd ~`

`pwd`：显示目前路径

以`/`开头的都是绝对路径，不以`/`开始就是相对路径

#### ls

命令 选项(可选) 参数：`ls -a /home/klyn`

`ls`：列出所有文件和文件夹（不含隐藏的文件和文件夹）

以`.`开头的文件或者文件夹是隐藏文件

`ls <path>`：列出指定目录下的文件和文件夹

`ls -a`列出所有文件（包括隐藏）

`ls -l`用来显示文件(夹)的详细信息：

> drwxrwxr-x 2 klyn klyn 4096 Nov  9 15:24 ddd

drwxrwxr-x：

+ 第一个字母表示文件的类型
  + `d`表示是一个文件夹
  + `-`表示它是一个文件
  + `l`表示一个链接(快捷方式)
+ rwxrwxr-x：表示权限，九个字母，三个一组，分别表示所有者，所属组和其它的权限
  + r：读取
  + w：写入
  + x：执行
  + -：没有权限
+ 2：
  + 如果是一个文件夹，表示这个文件夹里有几个子文件夹
  + 如果是个文件，用来表示文件硬链接的个数
+ klyn：表示所有者
+ klyn：表示所有者所属的组
+ 4096：
  + 文件夹显示的都是4096
  + 文件显示文件的大小
+ Nov  9 15:24：文件(夹)最后一次修改时间
+ ddd：文件(夹)的名字

`ls -lh`：使用更加贴近人类识别的格式显示，以KMGT形式显示

#### 命令的别名

`alias`用来查看别名

`alias la='ls -a'`：起别名；如果在控制台里直接输入，是临时的，终端关闭之后，别名就消失了

`ll`：等价于`ls -l`

#### 文件(夹)的创建删除

`mkdir`：创建文件夹

`mkdir a/b/c/d -p`：添加`-p`可以创建多级目录；选项可以放在中间，以可以放在最后

`touch <filename>`：创建一个空文件

`rmdir`：用来移除一个**空**文件夹；文件夹不为空，报错（一般不用）

`rm -rf`：用来移除文件或文件夹

`rm -rf *.txt`：删除该后缀的所有文件

`rm -rf *`：删除该目录下所有文件

`cp`：用来复制一个文件(夹)；`cp 源文件 目标文件(新名字)`

`mv`：用来移动一个文件(夹)

#### 查看文件相关指令

`cat`：从上到下，查看所有内容

`tac`：从下到上查看

`head -n`：查看前n行的数据，默认是10行

`tail -n`：查看后n行的数据

`wc`：行数，单词数，字节数

`nl`：带行号的显示所有内容

`more`：显示一屏内容，空格翻页，`enter`翻行，查看完毕后自动退出

`less`：显示一屏内容，需要输入`q`退出

### vim的使用

vim是一个文件编辑工具，相当于记事本

`yum install vim `第一步安装这个软件

`vim <filename> (+n)` 使用vim打开一个文件用来编辑；输入`+n`直接跳转到第n行打开；如果文件不存在，会创建一个新的

#### vim的三种模式

##### 插入模式

在这个模式下才能够写入内容，想要退出，必须按esc进入到命令模式才能退出

`i`：进入插入模式

`I`：在第一个非空字符前插入数据

`a`：在光标右侧插入

`A`：在光标所在行的结尾插入数据

`s`：删除光标所在位置的文字，并插入内容

`S`：删除光标所在行的文字，并插入内容

`o`：在光标所在行的下一行插入数据

`O`：在光标所在行的上一行插入数据

##### 命令模式

默认是命令模式，只能接受命令，不能输入内容

`shift+z+z`：保存并退出

`dd`：用来删除一行数据，`ndd`用来删除n行数据

`u`：撤销

`control+r`：反撤销

`yy`：用来复制一行，`nyy`用来复制n行

`p`：粘贴

`G`：定位到最后1行

`gg`：定位到第1行

`ngg`：定位到第n行

`$`：定位到行尾

`0/^`：定位到行首

`kjhl`：上下左右

`control+f`：下翻一页

`control+b`：上翻一页

`control+d`：下翻半页

`control+u`：上翻半页

`nx`：往后删几个

`nX`：删除光标左边的n个文字

##### 底线命令模式

`:`进入底线命令模式

`w`：保存修改

`q`：退出

`q!`：不保存强制退出

`wq`：保存并退出，等价于命令模式下的`shift+z+z`

`wq!`：强制修改只读文件并退出

`e!`：放弃之前的修改

`set nu`：显示行号

`n`：跳转到第n行

`/<keyword>`：用来进行查找，`n`下一个匹配，`N`上一个匹配；`noh`取消高亮

`%s/<oldword>/<newword>`：替换每一行第一次出现的关键词，添加`/g`全部替换

`m,ns/<oldword>/<newword>`：m~n行替换

#### vim的配置文件

`etc/vimrc`：所有的用户都能读取到这个配置

`~/.vimrc`：只有当前用户读取该配置

### 配置文件介绍

`/etc/bashrc/`, `~/.bashrc/`，每次打开终端，都会自动执行配置文件里的代码

把`alias md='mkdir'`命令写在`/etc/bashrc`文件中，重新连接终端之后，依然可以使用命令；无论使用哪个用户登陆，都会自动执行`/etc/bashrc`里的命令

`~/.bashrc`只用当前用户登录时，才会执行该文件里的命令

添加命令时，一般添加在最后一行

### 用户管理相关的命令

#### `useradd <username>`

用来新建一个用户

+ `-m`：创建用户的家目录，会在`/home`文件夹下创建一个和用户名同名的文件夹
+ `-M`：不创建用户家目录
+ `-d`：指定用户的家目录，一般情况下不指定
+ `-s`：指定用户登录时的shell解析脚本，一般指定`/bin/bash`

`su <username>`可以切换到指定的用户，可能需要输入密码

`su`或者`su -`切换到root用户

#### `passwd`

用来设置密码：

+ `passwd <username>`：root给该用户设置密码
+ `passwd`：给当前用户设置密码

#### `userdel`

删除用户的指令：

`-r`：删除用户的同时，删除用户的家目录等信息

`whoami`：查看当前登陆的用户

#### `sudo`

使用root用户权限执行命令：

+ 直接修改sudoers文件：

  + 不是所有的用户都能够实行`sudo`命令申请root权限，只有被添加到`/etc/sudoers`这个文件里的用户才有该权限(`vim sudoers`)

  + Linux里有一个专门的命令`visudo`，也可以修改`/etc/sudoers`

+ 将用户添加到有权限的组里

#### 组的概念

当我们创建一个用户时，会创建一个和它同名的分组

`groups`：查看当前用户所在的分组

`groups <username>`：查看指定用户分组

`gpasswd`：用来将用户添加到一个分组，或者从一个分组里移除

+ `-a <username> <groupname>`：将用户添加到对应的分组 

+ `-d <username> <groupname>`：将用户从指定的组里删除

root权限：ubuntu sudo组，centos wheel组

#### 用户和组相关的文件

`/etc/passwd`：列出了系统里所有的用户

+ `x` 密码
+ 数字：用户名 用户组
+ 办公信息
+ 家目录
+ 登陆脚本

`/etc/shadow`：保存用户密码（加密）

+ `!` 未设置密码；`*` 账号被锁定；`$1$` md5加密；`$6$`：sha512加密
+ 修改日期，上次修改密码日期到1970-1-1的天数
+ 密码不可修改的天数
+ 密码需要修改的期限
+ 修改期限前n天发出警告

`/etc/group`：分组信息

### 文件(夹)权限管理

`chmod`：用来修改权限

+ `o`：其它 `chmod o+w demo.txt`
+ `u`：所有者 `chmod u+x demo.txt`, `chmod u=rw demo.txt`
+ `g`：所属组 `chmod g-w demo.txt`
+ `a`：全部 `chmod a-r demo.txt`

权限值：

+ `r`: 4
+ `w`: 2
+ `x`: 1

`chmod 777`

默认权限：文件664，文件夹775

`umask` 用来查看文件(夹)的默认权限 002：取反 `000 000 010` ==> `111 111 101`

`umask 0022`修改

`chgrp <groupname> <filename>` 改变所属组

`chown <ownername> <filename>` 改变所有者

### 压缩解压命令

Linux里常见的压缩格式：.zip .tgz .tbz

#### zip压缩

`zip <a.zip> <a.txt>`

`unzip <a.zip>`

可以对文件夹进行压缩`-r`

#### gzip压缩

`gzip 1.txt` 会把原来的文件替换为`1.txt.gz`

`gunzip` 解压替换回来

压缩文件夹 `-r`，递归压缩文件夹里所有的文件

#### bzip2压缩

用法和`gzip`基本一致

不能压缩文件夹

#### tar 打包

不会对内容进行压缩，反而还会变大

##### -c 打包

`tar -cf a.tar a.txt`

##### -x 拆包

`tar xf a.tar`

##### -t 不拆包查看内容

`tar -tvf a.tar`

`-f`指定文件

`-v`查看细节(verbose)

##### `-z`

使用gzip压缩、解压

`tar -zcvf test.tgz test` 将test文件夹压缩成test.tgz

`tar -zxvf test.tgz` 解压

##### -j

使用bzip2压缩、挤压

`tar -jcvf test.tbz test`

### 多个指令的连接

`cmd1; cmd2`：前一个命令执行之后，无论成功与否，执行后一个命令

`cmd1 || cmd2`：或。如果前面的命令执行成功了，后面的命令不再执行

`cmd1 && cmd2`：前面的指令执行成功，才会执行后面的命令

## Nginx

### yum安装

#### 步骤

1. 安装nginx
2. 启动 `systemctl start nginx`
3. `ps -aux|grep nginx`

#### 配置文件的存放路径

1. `whereis nginx`
2. 读取`vim /etc/nginx/nginx.conf`
   + `listen 80` 设置监听的端口
   + `/usr/share/nginx/html` 静态页面的存放路径

### 下载源码安装

1. `wget <url>` 从官网上下载源代码
2. 解压
3. 运行configure文件 `./configure --prefix=/usr/local/nginx`，进行配置
   + `--prefix`指定安装路径
   + 配置的目的是查看当前系统的环境是否能够安装软件，在此过程中可能会出现错误提示，需要安装第三方的依赖包；运行命令安装依赖
   + 依赖安装完成后，再次运行configure文件
4. configure命令执行成功之后，会生成一个新的makefile文件
5. 执行命令进行编译安装`sudo make && sudo make install`
6. 启动nginx
   + `cd /usr/local/nginx/sbin`
   + 执行 nginx文件  `./nginx`

配置文件存放路径都在`/usr/local/nginx`

## 开放端口调整

服务器官网可以添加或删除所开放的端口

## 虚拟环境管理

### macOS

![image-20221113123949064](/Users/chenghao/Library/Mobile Documents/com~apple~CloudDocs/Python Notes/images/image-20221113123949064.png)

代码、环境分开管理

![image-20221113124011056](/Users/chenghao/Library/Mobile Documents/com~apple~CloudDocs/Python Notes/images/image-20221113124011056.png)

### Linux

![image-20221113132926093](/Users/chenghao/Library/Mobile Documents/com~apple~CloudDocs/Python Notes/images/image-20221113132926093.png)

1. `sudo pip3 install virtualenv`

2. `sudo pip3 install virtualenvwrapper`

3. `vim ~/.bashrc`，添加
   + `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6` 指定新虚拟环境默认的Python版本
   + `export WORKON_HOME=~/.venvs` 指创建的新的虚拟环境保存在哪个文件夹下
   + `source /usr/local/bin/virtualenvwrapper.sh` 执行virtualenvwrapper.sh脚本

4. `source ~/.bashrc` 需要重读`.bashrc`文件
5. `mkvirtualenv <name>` 创建一个新的虚拟环境

`workon <name>` 进入指定虚拟环境

`deactivate` 退出虚拟环境

#### 步骤解释

Linux里的命令都对应了一个可执行文件：

`ls` ==> `/bin/ls`文件

`python`, `python2`, `python2.7` 完全等价

在`usr/bin`中，有链接指向。`sudo ln -s python2.7 python`创建新的链接指向

`export`定义全局变量，`source`执行脚本

## 服务监听

`ps -aux`

`kill <pid>`(`kill -9`尽量不用)

`ps -aux|grep`

`ps -aux|grep -v grep|grep nginx`

`pstree`

`netstat -anop|grep`

## 管道和重定向

### 管道

把上一个命令的标准输出作为下一个命令的标准输入

`yum list installed|more`

`find -name demo.py|xargs rm -rf` 找到一个文件并删除

### 重定向

#### 方式

`ps -aux > ps.txt` 把执行结果重定向到一个指定的文件；如果文件已经存在，会覆盖

`ps -aux >> ps.txt` 把执行结果追加到一个文件

#### 分类

标准输出：默认 `1>`

错误输出：`2>` 将错误信息输入

全部输出：`&>` 把所有的输出都重定向

## Shell编程

把命令写到一个文件里

### 运行脚本文件的方法

首行通过注释的方式指明执行脚本的程序`#!bin/bash`

`bash test.sh `环境变量需要重新连接

`source test.sh` 环境变量立即生效

`./test.sh`：该方式执行脚本，这个脚本必须要有可执行权限 `chmod a+x`

Python脚本的第一句一般是`#!/usr/bin/env python`

### 变量和引号的使用

```shell
#!/bin/bash

a=10  # shell里定义了一个变量a，值是10。注意：等号两端不能有空格
# 使用$获取变量的值
echo goodafternoon$a
echo "hi$a"  # hi10
# 单引号里的内容会原样输出
echo 'hi$a'  # hi$a
# 反引号里的内容会被当作命令执行
echo `whoami`  # klyn
```

### $符的使用

```shell
#!/bin/bash

# shell里$功能强大
a=100
# ${变量名}可以用来取值，大多数情况下可以省略
echo $a
echo ${a}

# 特殊值
# 执行脚本时直接在命令后面传参
echo '$0的值是'$0  # $0表示脚本文件的名字
echo '$1的值是'$1  # 第一个参数的名字
echo '$2的值是'$2  # 第二个参数的名字，以此类推

echo '$*的值是'$*  # 所有参数
echo '$@的值是'$@  # 所有参数
echo '$#的值是'$#  # 参数的个数

# $(cmd)  执行小括号里的命令
echo $(whoami)  # 等价于echo `whoami`

# $((表达式))
echo $((1+1))

# $? 表示脚本的执行结果，0表示执行完成，正常退出
echo '$?的值是'$?
```

### 环境变量的使用及修改

```shell
#!/bin/bash

# 定义环境变量
export x=yes
# source 环境变量的使用.sh
# source执行立即生效；bash执行需要重新连接
# echo $x

# 内置环境变量
# $PATH $PWD $HOME $USER $UID

# 修改内置环境变量
# 在~/.bashrc里添加export PATH=$PATH:<newpath>进行环境变量的修改
```

### 获取用户输入

```shell
#!/bin/bash
read -p '请输入您的年龄' age
echo '年龄是'$age
```

### if语句的使用

```shell
#!/bin/bash

if ls /;then  # if后跟一个命令
	echo '命令执行成功'  # 如果命令成功，执行这个语句
else
	echo '命令执行失败'  # 如果命令失败，执行else语句
fi

# 条件测试命令
if [ condition ];then  # 两边要加空格
	commands
fi

# 数值比较
# -eq -ne -ge -gt- -le -lt
if [ 3 -gt 2 ];then
	echo '3大于2'
else
	echo '3不大于2'
fi

# 字符串比较
read -p '输入一段内容' x
read -p '再输入一段内容' y
if [ $x = $y ];then
	echo $x等于$y
else
	echo $x不等于$y

if [[ $x > $y ]];then  # 要用两个中括号
	echo $x > $y
else
	echo $x < $y
fi

# 判断文件类型
read -p '请输入一个路径' path
# -d -f -e
if [ -d $path ];then
	echo $path是一个文件夹
else
	echo $path不是一个文件夹
fi
```

### case语句的使用

```shell
#!/bin/bash

# case语句，即条件判断语句，用来判断相等的情况
read -p '请输入需要执行的操作' op
case $op in
	1)
		echo 添加用户
		;;
	2)
		echo 删除用户
		;;
	3)
		echo 查询用户
		;;
	*)
		echo 输入的操作不正确
		;;
esac
```

### for循环语句的使用

```shell
#!/bin/bash
for i in `seq 1 10`  # for...in循环，相当于Python for i in range(1,11)
do
	echo $i
done

# C语言风格的for循环
for ((j=0;j<=10;j++))
do
	echo $j
done
```

### 函数的使用

```shell
#!/bin/bash

# function可以省略不写
function foo(){
	echo foo里的$0  # 脚本名
	echo foo里的$1  # 第一个参数
	echo hello
}
foo 10 20 30
```

### 数组

```shell
#!/bin/bash

# 数组的使用，可以理解为Python里的列表
names=(hello 12 34 good)
echo $names  # 默认获取数组里的第0个数据
echo ${names[3]}  # 这里{}不能省略 

# *和@都能获取到所有的数据
echo ${names[*]}
echo ${names[@]}

# 获取长度
echo ${#names[*]}
echo ${#names[@]}

# 遍历数组
for i in ${names[*]}
do
	echo $i
done

for ((x=0;x<${#names[*]};x++))
do
	echo ${names[x]}
done
```
