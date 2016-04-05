#coding:utf-8
'''
Created on 2016年1月28日

@author: Warmer
'''
from __builtin__ import file
from fileinput import close
1 获取变量长度：len(content)

2 编码，解码=============================================
encode：username.encode('utf-8')//将unicode编码成utf-8
decode：username.decode('utf-8')//将utf-8解码成unicode
======================================================

3 time=====================================================================
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.time() 获取当前时间戳
time.localtime() 当前时间的struct_time形式
time.ctime() 当前时间的字符串形式
时间相加减-----------------------------------------------------------
last_month = time.localtime()[1]-1 or 12
》》》time.localtime()
》》》time.struct_time(tm_year=2016, tm_mon=2, tm_mday=1, tm_hour=14, tm_min=31, tm_sec=40, tm_wday=0, tm_yday=32, tm_isdst=0)
===========================================================================

4 字符串======================================================
拼接：
1   "\t".join(i,j)  将i，j拼接为 i\tj
2   settings.STATIC_URL+'img/'+self.bbs.userid.head
============================================================

5 class======================================================
dao = activityDao()
dao.add_a_activity(realcontent)
class activityDao():
    def __init__(self,req):
        self.us = User.objects.get(id=req["userid"])
    def add_a_activity(self,realcontent):
        do sth。。。
=============================================================

6 获取当前电脑信息================================================
myname = socket.getfqdn(socket.gethostname(  ))#获取本机电脑名
myaddr = socket.gethostbyname(myname)#获取本机ip
=============================================================

7.字典==============================
读取-------------
判断是否有键值：req.has_key('now')
===================================

8.多行字符串======
a='''sss
    sss'''
a=('ssss'
   'sss')
===============

9.读写文件=========================================================================================================================================================
获取当前文件路径：
    a=os.getcwd()
    aa = a.split("\\")

打开文件：
    open(name[, mode[, buffering]]) -> file object
        Open a file using the file() type, returns a file object.  This is the preferred way to open a file. 
        mode:    'r' 、 'U' ——打开的文件必须存在；   'w' ——文件若存在，首先清空，然后创建；    'a' ——写入的数据追加到文件的末尾 
    file(name[, mode[, buffering]]) -> file object
        Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),writing or appending.  
        The file will be created if it doesn't exist when opened for writing or appending; it will be truncated when
        opened for writing.  Add a 'b' to the mode for binary files. Add a '+' to the mode to allow simultaneous reading and writing.
        If the buffering argument is given, 0 means unbuffered, 1 means line buffered, and larger numbers specify the buffer size.  
        The preferred way to open a file is with the builtin open() function. Add a 'U' to mode to open the file 
        for input with universal newline support.  Any line ending in the input file will be seen as a '\n' in Python.  
        Also, a file so opened gains the attribute 'newlines'; the value for this attribute is one of None (no newline 
        read yet), '\r', '\n', '\r\n' or a tuple containing all the newline types seen. 'U' cannot be combined with 'w' or '+' mode.
        
            使用open打开文件后一定要记得调用文件对象的close()方法。比如可以用try/finally语句来确保最后能关闭文件。
    file_object = open('thefile.txt')
    try:
        all_the_text = file_object.read( )
    finally:
        file_object.close( )
            注：不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。
            
    Python 2 里基本没区别。Python 3 里没 file。
    Python 2 里，file 是文件对象。open 是返回新创建的文件对象的内建函数，相当于：
    def open(*args, **kwargs):
        return file(*args, **kwargs)


读取文件：
    .read()、.readline() 和 .readlines()。每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量。 
    .read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。然而 .read() 生成文件内容最直接的字符串表示，但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理。
    .readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
    .readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。
    
            读文本文件
    input = open('data', 'r')
    #第二个参数默认为r
    input = open('data')
            读二进制文件
    input = open('data', 'rb')
            读取所有内容
    file_object = open('thefile.txt')
    try:
        all_the_text = file_object.read( )
    finally:
        file_object.close( )
            读固定字节
    file_object = open('abinfile', 'rb')
    try:
        while True:
            chunk = file_object.read(100)
            if not chunk:
                break
            do_something_with(chunk)
    finally:
        file_object.close( )
            读每行
    for  line in  file_object.readlines(): 
        print  line
            如果文件是文本文件，还可以直接遍历文件对象获取每行：
    for line in file_object:
        process(line)
            
            例如需要在一台物理内存为 2GB 的机器上处理一个 2GB 的日志文件，我们可能希望每次只处理其中 200MB 的内容。
            在 Python 中，内置的 File 对象直接提供了一个 readlines(sizehint) 函数来完成这样的事情。以下面的代码为例：
    file = open('test.log', 'r')
    sizehint = 209715200   # 200M
    position = 0lines = file.readlines(sizehint)
    while not file.tell() - position < 0:       
        position = file.tell()       
        lines = file.readlines(sizehint)
            每次调用 readlines(sizehint) 函数，会返回大约 200MB 的数据，而且所返回的必然都是完整的行数据，大多数情况下，返回的数据的字节数会稍微比 sizehint 指定的值大一点（除最后一次调用 readlines(sizehint) 函数的时候）。
            通常情况下，Python 会自动将用户指定的 sizehint 的值调整成内部缓存大小的整数倍。

写文件：
    .write(str)方法把字符串str写入文件。没有返回值。由于缓冲，字符串可能不实际显示文件，直到flush()或close()方法被调用。
    .writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。

            写文本文件
    output = open('data', 'w')
            写二进制文件
    output = open('data', 'wb')
            追加写文件
    output = open('data', 'w+')
            写数据
    file_object = open('thefile.txt', 'w')
    file_object.write(all_the_text)
    file_object.close( )
            写入多行
    file_object.writelines(list_of_text_strings)
            注意，调用writelines写入多行在性能上会比使用write一次性写入要高。
    
删除：
    os.remove()
    if os.path.exists(dir_path):
        if os.path.isfile(os.path.join(dir_path,i)):
            os.remove(os.path.join(dir_path,i)) #删除文件

创建：
    os.makedirs(targetDir)#创建目录

移动：
    .seek(offset, whence=SEEK_SET)
        Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence. 
        Values for whence are:
            SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
            SEEK_CUR or 1 – current stream position; offset may be negative
            SEEK_END or 2 – end of the stream; offset is usually negative
        Return the new absolute position.
关闭：
    .close()

其他：
    .fileno()    ——返回打开文件的描述符
    .flush()    ——直接把内部缓冲区中的数据立刻写入文件，而不是被动地等待输出缓冲区被写入
    .isatty()    ——检测文件是否一个类tty设备（True | False）
    .truncate(size=file.tell())    ——截取文件到最大size字节，默认为当前文件指针位置
    .tell()     ——返回当前文件中的位置
    
==================================================================================================================================

10.遍历目录==================================================================================
os.walk(top, topdown=True, onerror=None, followlinks=False)
一般只使用第一个参数。（topdown指明遍历的顺序）
该方法对于每个目录返回一个三元组，(dirpath, dirnames, filenames)。第一个是路径，第二个是路径下面的目录，第三个是路径下面的非目录（对于windows来说也就是文件）。
for fpathe,dirs,fs in os.walk('/root'):
  for f in fs:
    print os.path.join(fpathe,f)
    
listdir
可以使用os模块下的几个方法组合起来进行遍历
import os
def gci(filepath):
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)            
    if os.path.isdir(fi_d):
      gci(fi_d)                  
    else:
      print os.path.join(filepath,fi_d)
#递归遍历/root目录下所有文件
gci('/root')
===========================================================================================

11. 操作execl==========================================================
安装xlrd模块（Windows）：easy_install xlrd  
打开Excel文件读取数据
       data = xlrd.open_workbook('excelFile.xls')
获取一个工作表
        table = data.sheets()[0]          #通过索引顺序获取
        table = data.sheet_by_index(0) #通过索引顺序获取
        table = data.sheet_by_name(u'Sheet1')#通过名称获取
 获取整行和整列的值（数组）
         table.row_values(i)
         table.col_values(i)
获取行数和列数
        nrows = table.nrows
        ncols = table.ncols
 循环行列表数据
        for i in range(nrows ):
            print table.row_values(i)
单元格
    cell_A1 = table.cell(0,0).value
    cell_C4 = table.cell(2,3).value
使用行列索引
    cell_A1 = table.row(0)[0].value
    cell_A2 = table.col(1)[0].value
简单的写入
    row = 0
    col = 0
    # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    ctype = 1 
    value = '单元格的值'
    xf = 0 # 扩展的格式化
    table.put_cell(row, col, ctype, value, xf)
    table.cell(0,0)  #单元格的值'
    table.cell(0,0).value #单元格的值'
======================================================================