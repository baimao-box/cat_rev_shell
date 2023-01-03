# cat_rev_shell v1.0
```
  ___   _ _____   ___ _____   __  ___ _  _ ___ _    _    
 / __| /_\_   _| | _ \ __\ \ / / / __| || | __| |  | |   
| (__ / _ \| |   |   / _| \ V /  \__ \ __ | _|| |__| |__ 
 \___/_/ \_\_|   |_|_\___| \_/   |___/_||_|___|____|____|
 
```
一个方便的Reverse Shell生成器，可以在交互界面生成shell和设置监听的端口，并且自动运行netcat监听设置的端口，并不需要退出就可以测试多个shell，目前支持的shell：
```
python
python3
nc
mkfifo
bash
```

# 运行
```
chmod +x cat_rev_shell.py
./cat_rev_shell.py
```
![image](https://user-images.githubusercontent.com/52622597/210320383-921c40d0-1a4b-4d30-84a4-2c8cf2f18060.png)

# 参数

输入info可以查看可以运行的命令

![image](https://user-images.githubusercontent.com/52622597/210320732-91f30eb3-4f13-4a2d-8cf9-6d18eba9829f.png)

输入set ip可以设置监听的ip和端口

![image](https://user-images.githubusercontent.com/52622597/210320842-72542be7-1bad-48dd-a36e-9681de1a3152.png)

输入set shell 可以选择生成的shell

![image](https://user-images.githubusercontent.com/52622597/210320899-a4772bf9-aa61-42be-bbfb-2ab406b7c5d5.png)

输入run可以运行netcat监听设置的端口

![image](https://user-images.githubusercontent.com/52622597/210320944-2ddc9600-398b-4b4d-8026-51a091ff0f3b.png)

可以正常的输入bash命令

![image](https://user-images.githubusercontent.com/52622597/210321021-b8faf88d-9413-44a6-8b10-c3345e8965f9.png)

