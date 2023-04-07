# -*- encoding=utf8 -*-
__author__ = "吴积帅"

one_open = False

# auto_Wuyan = 0
# 群雄逐鹿统计次数初始化
# auto_Wuyan_Win  = 0
# 群雄逐鹿胜利次数初始化



from airtest.core.api import *

auto_setup(__file__)

#恭喜获得处理方法
def gxhd():
    if exists(Template(r"tpl1680164392791.png", record_pos=(-0.001, -0.095), resolution=(1440, 810))):
        touch(Template(r"tpl1680164403449.png", record_pos=(-0.003, -0.091), resolution=(1440, 810)))
        while exists(Template(r"tpl1680164392791.png", record_pos=(-0.001, -0.095), resolution=(1440, 810))):
            gxhd()
            

#返回方法1
def out():
    touch(Template(r"tpl1679795085845.png", record_pos=(-0.453, -0.267), resolution=(1440, 810)))

    
    
#返回方法2
def out_x():
    if exists(Template(r"tpl1680052864566.png", record_pos=(0.388, -0.231), resolution=(1440, 810))):
        touch(Template(r"tpl1680052886754.png", record_pos=(0.385, -0.234), resolution=(1440, 810)))
    while exists(Template(r"tpl1680052864566.png", record_pos=(0.388, -0.231), resolution=(1440, 810))):
        out_x()
        
#一键执行类
class YJZX():
    
    
    def await(self):
        if exists(Template(r"tpl1678162004810.png", record_pos=(0.005, 0.169), resolution=(1440, 810))) or exists(Template(r"tpl1680489010769.png", record_pos=(-0.366, -0.266), resolution=(1440, 810))) or exists(Template(r"tpl1678240705666.png", record_pos=(0.458, 0.229), resolution=(1440, 810))) or exists(Template(r"tpl1680570952663.png", record_pos=(-0.368, -0.266), resolution=(1440, 810))):
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
            touch(Template(r"tpl1678161062972.png", record_pos=(0.01, 0.005), resolution=(1440, 810)))
            sleep(2.0)
            if exists(Template(r"tpl1679996321989.png", record_pos=(0.007, 0.104), resolution=(1440, 810))):
                touch(Template(r"tpl1679996333986.png", record_pos=(0.006, 0.104), resolution=(1440, 810)))
                sleep(2.0)
        elif  exists(Template(r"tpl1680152617591.png", record_pos=(0.004, -0.154), resolution=(1440, 810))):
            touch(Template(r"tpl1678161062972.png", record_pos=(0.01, 0.005), resolution=(1440, 810)))
            sleep(2.0)
            if exists(Template(r"tpl1679710369624.png", record_pos=(0.034, 0.068), resolution=(1440, 810))):
                touch(Template(r"tpl1679710384491.png", record_pos=(0.034, 0.069), resolution=(1440, 810)))
#             else :
                

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
            
            if exists(Template(r"tpl1679794516400.png", record_pos=(0.006, 0.207), resolution=(1440, 810))):
                touch(Template(r"tpl1679794530313.png", record_pos=(0.006, 0.205), resolution=(1440, 810)))
        else:
            touch(Template(r"tpl1679793910178.png", record_pos=(0.331, 0.133), resolution=(1440, 810)))
        self.auto_wuyan_hw+=1
        print(f"进行会武第{self.auto_wuyan_hw}次")
        sleep(5.0)

        touch(Template(r"tpl1679794080518.png", record_pos=(-0.001, -0.106), resolution=(1440, 810)))
        while self.auto_wuyan_hw<10 :
            self.hw_zhandou()

        
        
#每日任务类
class MRRW():

    
#清体力模块(未解决)    
    def ti_li(self):
        if exists(Template(r"tpl1680494144502.png", record_pos=(-0.041, -0.054), resolution=(1440, 810))):
            touch(Template(r"tpl1680494164078.png", record_pos=(0.369, -0.038), resolution=(1440, 810)))
            if exists(Template(r"tpl1680494463925.png", record_pos=(-0.369, -0.265), resolution=(1440, 810))):
                touch(Template(r"tpl1680494177165.png", record_pos=(-0.462, -0.17), resolution=(1440, 810)))
                sleep(10.0)
            touch(Template(r"tpl1680494209527.png", record_pos=(-0.203, 0.232), resolution=(1440, 810)))
            if exists(Template(r"tpl1680494231994.png", record_pos=(-0.001, 0.037), resolution=(1440, 810))):
                touch(Template(r"tpl1680494243223.png", record_pos=(-0.11, 0.04), resolution=(1440, 810)))
            touch(Template(r"tpl1680494255278.png", record_pos=(0.002, 0.093), resolution=(1440, 810)))
            while exists(Template(r"tpl1680494288727.png", record_pos=(-0.028, -0.262), resolution=(1440, 810))):
                sleep(10.0)
            self.ti_li
#             if exists(Template(r"tpl1680495541328.png", record_pos=(0.202, -0.165), resolution=(1440, 810))):
#                 touch(Template(r"tpl1680495913672.png", record_pos=(-0.001, 0.089), resolution=(1440, 810)))
#                 touch(Template(r"tpl1680495924641.png", record_pos=(-0.085, 0.217), resolution=(1440, 810)))
#                 touch(Template(r"tpl1680495937193.png", record_pos=(0.458, -0.05), resolution=(1440, 810)))
#                 if exists(Template(r"tpl1680496219771.png", record_pos=(0.146, 0.173), resolution=(1440, 810))) and 
#                 touch(Template(r"tpl1680496132001.png", record_pos=(-0.086, 0.165), resolution=(1440, 810)))
#                 touch(Template(r"tpl1680496117249.png", record_pos=(0.065, -0.037), resolution=(1440, 810)))


                









    
    
    
#组队挑战模块_加入队伍方法   
    def zu_dui_jiaru(self):
        if exists(Template(r"tpl1680054779306.png", record_pos=(-0.049, -0.056), resolution=(1440, 810))):
            touch(Template(r"tpl1680054794221.png", record_pos=(0.368, -0.04), resolution=(1440, 810)))
            touch(Template(r"tpl1680054838666.png", record_pos=(0.422, 0.185), resolution=(1440, 810)))
            self.zu_dui_jrsb()


#组队挑战加入方法
    def zu_dui_jrsb(self):
        touch(Template(r"tpl1680054900454.png", record_pos=(0.195, 0.195), resolution=(1440, 810)))
        sleep(2.0)
        while exists(Template(r"tpl1680235859424.png", record_pos=(0.196, 0.196), resolution=(1440, 810))):
            self.zu_dui_jrsb()
        self.zu_dui_zhandou()
            

            
#组队挑战_准备挑战方法
    def zu_dui_zhandou(self):
        touch(Template(r"tpl1680054911065.png", record_pos=(0.344, 0.199), resolution=(1440, 810)))
        sleep(120.0)
        if exists(Template(r"tpl1680055007475.png", record_pos=(0.001, -0.148), resolution=(1440, 810))):
            touch(Template(r"tpl1680055025673.png", record_pos=(0.0, -0.014), resolution=(1440, 810)))
            touch(Template(r"tpl1680055067539.png", record_pos=(0.422, -0.231), resolution=(1440, 810)))
        out()
        touch(Template(r"tpl1680055102541.png", record_pos=(0.364, -0.04), resolution=(1440, 810)))
            

            
#远古剑冢方法
    def jian_zhou(self):
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






    def xi_xin():
        touch(Template(r"tpl1680154344708.png", record_pos=(-0.298, -0.217), resolution=(1440, 810)))
        touch(Template(r"tpl1680154356162.png", record_pos=(-0.449, -0.175), resolution=(1440, 810)))
        touch(Template(r"tpl1680154362587.png", record_pos=(-0.395, 0.053), resolution=(1440, 810)))
        sleep(6.0)


            



            
    
#领取已完成的每日任务方法
    def open_mrrw(self):
        touch(Template(r"tpl1680054159696.png", record_pos=(0.217, -0.215), resolution=(1440, 810)))
        if exists(Template(r"tpl1680054191757.png", record_pos=(0.405, 0.172), resolution=(1440, 810))):
            touch(Template(r"tpl1680054191757.png", record_pos=(0.405, 0.172), resolution=(1440, 810)))
            sleep(10.0)
            if exists(Template(r"tpl1680054254583.png", record_pos=(-0.003, -0.153), resolution=(1440, 810))):
                gxhd()
            
            
            
            
#山河类
class SH():
    
    def shan_he_zhandou(self):
        touch(Template(r"tpl1680154847187.png", record_pos=(-0.006, -0.069), resolution=(1440, 810)))
        touch(Template(r"tpl1680154867796.png", record_pos=(-0.249, 0.246), resolution=(1440, 810)))
        sleep(7.0)
        if exists(Template(r"tpl1680575046562.png", record_pos=(0.201, -0.16), resolution=(1440, 810))):
            touch(Template(r"tpl1680154891513.png", record_pos=(0.32, 0.118), resolution=(1440, 810)))
            while True:
                self.shan_he_zhandou()
        elif exists(Template(r"tpl1680155542281.png", record_pos=(0.206, -0.163), resolution=(1440, 810))):
            
            touch(Template(r"tpl1680155529751.png", record_pos=(0.333, 0.208), resolution=(1440, 810)))
            touch(Template(r"tpl1680155560297.png", record_pos=(0.018, -0.023), resolution=(1440, 810)))
            sleep(12.0)
            if exists(Template(r"tpl1680155613213.png", record_pos=(0.133, 0.039), resolution=(1440, 810))):
                touch(Template(r"tpl1680155626517.png", record_pos=(-0.006, 0.187), resolution=(1440, 810)))
                while True:
                    self.shan_he_zhandou()
            elif exists(Template(r"tpl1680155765863.png", record_pos=(0.137, 0.041), resolution=(1440, 810))):
                touch(Template(r"tpl1680155777027.png", record_pos=(-0.003, 0.185), resolution=(1440, 810)))
        elif exists(Template(r"tpl1680154867796.png", record_pos=(-0.249, 0.246), resolution=(1440, 810))) :
            touch(Template(r"tpl1680154867796.png", record_pos=(-0.249, 0.246), resolution=(1440, 810)))
            sleep(2.0)
            touch(Template(r"tpl1680156449500.png", record_pos=(0.316, 0.119), resolution=(1440, 810)))
            while True:
                self.shan_he_zhandou()
        elif exists(Template(r"tpl1680156573167.png", record_pos=(-0.001, -0.119), resolution=(1440, 810))):
            touch(Template(r"tpl1680156590221.png", record_pos=(-0.002, -0.116), resolution=(1440, 810)))

        else:
            touch(Template(r"tpl1680160130903.png", record_pos=(0.317, 0.12), resolution=(1440, 810)))
            while True:
                self.shan_he_zhandou()




#乾坤环境类
class QKHJ():
     
#     def __init__(self):
#         if exists(Template(r"tpl1680163230825.png", record_pos=(0.226, -0.147), resolution=(1440, 810))):
#             x=bzwj
#         elif exists(Template(r"tpl1680163344331.png", record_pos=(0.232, -0.147), resolution=(1440, 810))):    

    def QKHJ_tuitu_bzwj(self):

            touch(Template(r"tpl1680163254234.png", record_pos=(0.424, 0.211), resolution=(1440, 810)))
            sleep(30.0)
            touch(Template(r"tpl1680163298659.png", record_pos=(-0.001, 0.128), resolution=(1440, 810)))

    def QKHJ_tuitu_sjld(self):
        self.QKHJ_dh()
        if exists(Template(r"tpl1680166518086.png", record_pos=(-0.367, -0.264), resolution=(1440, 810))):
            touch(Template(r"tpl1680164775832.png", record_pos=(0.417, 0.21), resolution=(1440, 810)))
        if exists(Template(r"tpl1680166396252.png", record_pos=(-0.365, -0.264), resolution=(1440, 810))):
            touch(Template(r"tpl1680163647947.png", record_pos=(-0.003, -0.061), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"tpl1680163716309.png", record_pos=(-0.249, 0.248), resolution=(1440, 810)))            
        sleep(3.0)
        touch(Template(r"tpl1680163732199.png", record_pos=(0.317, 0.119), resolution=(1440, 810)))
        gxhd()

        
        
        while True:
            self.QKHJ_tuitu_sjld()
        
        

    def QKHJ_dh(self):
        if exists(Template(r"tpl1680166130086.png", record_pos=(0.423, 0.221), resolution=(1440, 810))):
            touch(Template(r"tpl1680166142878.png", record_pos=(0.416, 0.223), resolution=(1440, 810)))
            sleep(5.0)
            if exists(Template(r"tpl1680167099923.png", record_pos=(-0.124, 0.11), resolution=(1440, 810))):
                touch(Template(r"tpl1680167115744.png", record_pos=(-0.124, 0.105), resolution=(1440, 810)))
                touch(Template(r"tpl1680167134506.png", record_pos=(0.0, 0.133), resolution=(1440, 810)))
            sleep(5.0)
            if exists(Template(r"tpl1680166157888.png", record_pos=(0.388, -0.25), resolution=(1440, 810))):
                touch(Template(r"tpl1680166157888.png", record_pos=(0.388, -0.25), resolution=(1440, 810)))
        if exists(Template(r"tpl1680244859538.png", record_pos=(0.42, 0.221), resolution=(1440, 810))):
            touch(Template(r"tpl1680244868973.png", record_pos=(0.422, 0.223), resolution=(1440, 810)))
            gxhd()
            

    def QKHJ_qzj(self):
        if exists(Template(r"tpl1680256324194.png", record_pos=(-0.364, -0.265), resolution=(1440, 810))):
            touch(Template(r"tpl1680256333764.png", record_pos=(0.426, 0.209), resolution=(1440, 810)))
            sleep(2.0)
        if exists(Template(r"tpl1680256447392.png", record_pos=(-0.363, -0.264), resolution=(1440, 810))):
            touch(Template(r"tpl1680256381323.png", record_pos=(-0.008, -0.052), resolution=(1440, 810)))
            sleep(1.0)
            touch(Template(r"tpl1680256576683.png", record_pos=(-0.251, 0.245), resolution=(1440, 810)))
            sleep(4.0)
            if exists(Template(r"tpl1680256403340.png", record_pos=(0.201, -0.157), resolution=(1440, 810))):
                touch(Template(r"tpl1680256424236.png", record_pos=(0.316, 0.119), resolution=(1440, 810)))
                if exists(Template(r"tpl1680256696582.png", record_pos=(-0.002, -0.093), resolution=(1440, 810))):
                    gxhd()

                while True:
                    self.QKHJ_qzj()
            elif exists(Template(r"tpl1680256771859.png", record_pos=(0.199, -0.161), resolution=(1440, 810))):
                touch(Template(r"tpl1680256780905.png", record_pos=(0.333, 0.21), resolution=(1440, 810)))
                self.QKHJ_qzj()






        
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

    
def shanhe_tuitu():
    c=SH()
    c.shan_he_zhandou()

    
#实例化每日   
def mr():
    d=MRRW()
    d.open_mrrw()
#     d.ti_li()
    d.zu_dui_jiaru()
    d.jian_zhou()
    

def qkhj_sl():
    e=QKHJ()
#     e.QKHJ_tuitu_sjld()
    e.QKHJ_qzj()
    
#调用武演和一键执行方法
def start():
    huansan()
    QXZL()
    mr()
#     shanhe_tuitu()
#     qkhj_sl()

#调用方法
start()    
 