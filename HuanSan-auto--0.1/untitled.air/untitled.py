# -*- encoding=utf8 -*-
__author__ = "吴积帅"

one_open = False

# auto_Wuyan = 0
# 群雄逐鹿统计次数初始化
# auto_Wuyan_Win  = 0
# 群雄逐鹿胜利次数初始化



from airtest.core.api import *

auto_setup(__file__)

#返回类
def out():
    touch(Template(r"tpl1679795085845.png", record_pos=(-0.453, -0.267), resolution=(1440, 810)))

    
    
#返回类
def out_x():
    if exists(Template(r"tpl1680052864566.png", record_pos=(0.388, -0.231), resolution=(1440, 810))):
        touch(Template(r"tpl1680052886754.png", record_pos=(0.385, -0.234), resolution=(1440, 810)))
    while exists(Template(r"tpl1680052864566.png", record_pos=(0.388, -0.231), resolution=(1440, 810))):
        out_x()
        
#一键执行类
class YJZX():
    
    
    def await(self):
        if exists(Template(r"tpl1678162004810.png", record_pos=(0.005, 0.169), resolution=(1440, 810))) or exists(Template(r"tpl1678240705666.png", record_pos=(0.458, 0.229), resolution=(1440, 810))):

                sleep(10.0)
                self.await()

                
    def  OpenHuansan(self):
        touch(Template(r"tpl1678159767264.png", record_pos=(-0.168, 0.242), resolution=(1440, 810)))
        sleep(5.0)
        touch(Template(r"tpl1678159817568.png", record_pos=(0.376, 0.176), resolution=(1440, 810)))
        self.await()
        if exists(Template(r"tpl1678162087610.png", record_pos=(-0.006, 0.18), resolution=(1440, 810))):
            touch(Template(r"tpl1678160831198.png", record_pos=(0.001, 0.174), resolution=(1440, 810)))
        touch(Template(r"tpl1678160897147.png", record_pos=(0.269, -0.203), resolution=(1440, 810)))


#武演类
class WY():
    
    def __init__(self,auto_wuyan_win,auto_wuyan,auto_wuyan_hw):
        self.auto_wuyan_win=auto_wuyan_win
        self.auto_wuyan = auto_wuyan
        self.auto_wuyan_hw=auto_wuyan_hw

#下面的方法为进入群雄逐鹿的操作        
    def WYQX(self):

            touch(Template(r"tpl1678160977893.png", record_pos=(0.41, -0.088), resolution=(1440, 810)))
            touch(Template(r"tpl1678161018807.png", record_pos=(0.009, -0.004), resolution=(1440, 810)))
            if exists(Template(r"tpl1679902002458.png", record_pos=(0.183, -0.085), resolution=(1440, 810))):
                touch(Template(r"tpl1679902018074.png", record_pos=(0.178, 0.082), resolution=(1440, 810)))

            if exists(Template(r"tpl1679709740575.png", record_pos=(-0.023, -0.084), resolution=(1440, 810))):
                touch(Template(r"tpl1679709762677.png", record_pos=(0.002, -0.081), resolution=(1440, 810)))


                
                
#下面的方法为匹配同时完成胜场任务
    def qx_zhandou(self):

        touch(Template(r"tpl1678161041234.png", record_pos=(0.342, 0.128), resolution=(1440, 810)))
        self.auto_wuyan+=1
        print(f"匹第{self.auto_wuyan}次")
        sleep(6.0)
        if exists(Template(r"tpl1679793249834.png", record_pos=(-0.013, -0.149), resolution=(1440, 810))):
                self.auto_wuyan_win+=1
                print(f"群雄逐鹿胜利第{self.auto_wuyan_win}次")
                if exists(Template(r"tpl1679996321989.png", record_pos=(0.007, 0.104), resolution=(1440, 810))):
                    touch(Template(r"tpl1679996333986.png", record_pos=(0.006, 0.104), resolution=(1440, 810)))

        sleep(2.0)
        if exists(Template(r"tpl1679710369624.png", record_pos=(0.034, 0.068), resolution=(1440, 810))):
            touch(Template(r"tpl1679710384491.png", record_pos=(0.034, 0.069), resolution=(1440, 810)))
            self.qx_zhandou()


        touch(Template(r"tpl1678161062972.png", record_pos=(0.01, 0.005), resolution=(1440, 810)))
        while self.auto_wuyan<10 or self.auto_wuyan_win<5:
            self.qx_zhandou()


#下面方法为进入会武操作            
    def wy_hy(self):
        touch(Template(r"tpl1679795147092.png", record_pos=(0.222, 0.203), resolution=(1440, 810)))
        if exists(Template(r"tpl1679793731925.png", record_pos=(0.177, -0.081), resolution=(1440, 810))):
            touch(Template(r"tpl1679793762648.png", record_pos=(0.175, 0.082), resolution=(1440, 810)))
        if exists(Template(r"tpl1679997184533.png", record_pos=(-0.005, -0.083), resolution=(1440, 810))):
            touch(Template(r"tpl1679997194737.png", record_pos=(-0.001, -0.081), resolution=(1440, 810)))



#下面方法为会武匹配任务
    def hw_zhandou(self):
        if exists(Template(r"tpl1679794438747.png", record_pos=(0.335, 0.136), resolution=(1440, 810))):
            touch(Template(r"tpl1679794452484.png", record_pos=(0.333, 0.135), resolution=(1440, 810)))
        else:
            touch(Template(r"tpl1679793910178.png", record_pos=(0.331, 0.133), resolution=(1440, 810)))
        self.auto_wuyan_hw+=1
        print(f"进行会武第{self.auto_wuyan_hw}次")
        sleep(5.0)
        if exists(Template(r"tpl1679794516400.png", record_pos=(0.006, 0.207), resolution=(1440, 810))):
            touch(Template(r"tpl1679794530313.png", record_pos=(0.006, 0.205), resolution=(1440, 810)))
        touch(Template(r"tpl1679794080518.png", record_pos=(-0.001, -0.106), resolution=(1440, 810)))
        while self.auto_wuyan_hw<10 :
            self.hw_zhandou()
        
        
#每日任务类
class MRRW():

    
#清体力模块(未解决)    
    def ti_li():
            touch(Template(r"tpl1680054620468.png", record_pos=(-0.087, 0.256), resolution=(1440, 810)))
    
    
    
#组队挑战模块    
    def zu_dui():
        if exists(Template(r"tpl1680054779306.png", record_pos=(-0.049, -0.056), resolution=(1440, 810))):
            touch(Template(r"tpl1680054794221.png", record_pos=(0.368, -0.04), resolution=(1440, 810)))
            touch(Template(r"tpl1680054838666.png", record_pos=(0.422, 0.185), resolution=(1440, 810)))
            touch(Template(r"tpl1680054900454.png", record_pos=(0.195, 0.195), resolution=(1440, 810)))
            touch(Template(r"tpl1680054911065.png", record_pos=(0.344, 0.199), resolution=(1440, 810)))
            if exists(Template(r"tpl1680055007475.png", record_pos=(0.001, -0.148), resolution=(1440, 810))):
                touch(Template(r"tpl1680055025673.png", record_pos=(0.0, -0.014), resolution=(1440, 810)))
                touch(Template(r"tpl1680055067539.png", record_pos=(0.422, -0.231), resolution=(1440, 810)))
            out()
            touch(Template(r"tpl1680055102541.png", record_pos=(0.364, -0.04), resolution=(1440, 810)))



#远古剑冢方法
    def jian_zhou():
        if exists(Template(r"tpl1680055221445.png", record_pos=(-0.051, 0.119), resolution=(1440, 810))):
            touch(Template(r"tpl1680055241172.png", record_pos=(0.365, 0.133), resolution=(1440, 810)))
        if exists(Template(r"tpl1680055281202.png", record_pos=(0.101, 0.065), resolution=(1440, 810))):
            touch(Template(r"tpl1680055281202.png", record_pos=(0.101, 0.065), resolution=(1440, 810)))
            touch(Template(r"tpl1680055341823.png", record_pos=(0.002, -0.006), resolution=(1440, 810)))
            touch(Template(r"tpl1680055357477.png", record_pos=(-0.249, 0.249), resolution=(1440, 810)))
            if exists(Template(r"tpl1680055408655.png", record_pos=(0.196, -0.154), resolution=(1440, 810))):
                touch(Template(r"tpl1680055418110.png", record_pos=(0.197, -0.155), resolution=(1440, 810)))
            out()
            touch(Template(r"tpl1680055530656.png", record_pos=(0.368, -0.043), resolution=(1440, 810)))








            







            
    
#领取已完成的每日任务方法
    def open_mrrw():
        touch(Template(r"tpl1680054159696.png", record_pos=(0.217, -0.215), resolution=(1440, 810)))
        touch(Template(r"tpl1680054191757.png", record_pos=(0.405, 0.172), resolution=(1440, 810)))
        if exists(Template(r"tpl1680054254583.png", record_pos=(-0.003, -0.153), resolution=(1440, 810))):
            touch(Template(r"tpl1680054276387.png", record_pos=(-0.008, -0.111), resolution=(1440, 810)))

    


        
        
        
#实例化武演类
def QXZL():
    a=WY(0,0,0)
    a.WYQX()
    a.qx_zhandou()
    out()
    a.wy_hy()
    a.hw_zhandou()
    out()
    out()
    out_x()

    
    
#实例化一键执行类
def huansan():
    b=YJZX()
    b.OpenHuansan()

    
    
#调用武演和一键执行方法
def start():
#     OpenHuansan()
    huansan()
    QXZL()
    
#调用方法
start()    
