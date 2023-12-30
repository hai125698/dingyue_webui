        # dingyue_webui
        1.  购买VPS  --> 此处略过 
        2.  查看源代码 
        [dingyue_webui源码地址](https://github.com/hai125698/dingyue_webui)
        3.  简单安装 
          a. 直接安装到服务器
          b. 打包为docker镜像再进行安装
        4.  docker镜像使用
        以上源码我已经打包为docker镜像上传到dockerhub上，可以直接使用 
        docker run -d --restart always -p 10011:5000 --name getnode_webui brownbearye/getnode_webui:latest
         
        5.  参数讲解
        这段docker 代码只有一个参数，就是webui发布的端口，如果想在其他端口上使用，就将10011 改变为其他端口，比如 
        docker run -d --restart always -p 10012:5000 --name getnode_webui brownbearye/getnode_webui:latest
         
        6.  平台使用 
          a.  输入IP：端口登录到系统，默认密码为123456  
![RUNOOB 图标](https://tc.vless.vip/i/2023/12/16/s4c2fi.png)

          c. 新建节点
            ⅰ. 点击新建标签即为新加入节点，输入节点分享信息，然后点保存即可保存节点 
            
![添加节点](https://tc.vless.vip/i/2023/12/16/s4cczl.png) 

          d. 修改密码
            ⅰ. 同理，点击修在新密码栏输入新的密码，再点击修改密码，即可修改登录密码
        8. 订阅链接使用-- 以V2rayN为例 
        http://ip:10011/get_node?token=123456
        10.  参数讲解 
          a. ip:10011   这里就是搭建webui的服务器的IP ， 10011就是在新建docker容器时，参数指定的端口
          b. get_node?token=    这里保存不变，
          c. 123456    这里就是你的登录密码， 如果在web上面修改了密码， 节点订阅地址同样需要修改
