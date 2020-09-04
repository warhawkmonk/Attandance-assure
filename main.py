import datetime
import json
import threading
from functools import partial

import matplotlib.pyplot as plt
import pandas as pd
import requests

import kivy.uix.treeview as TreeView
from kivy.app import App
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.behaviors.compoundselection import CompoundSelectionBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDIconButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.tab import MDTabs
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.textfield import MDTextField, MDTextFieldRound, TextInput
from kivymd.uix.toolbar import MDToolbar


class monk(Screen):
    def __init__(self,**kwargs): 
        super().__init__(**kwargs)
        self.mokila=ObjectProperty(None)
        self.mokilal=ObjectProperty(None)
        self.mokilali=ObjectProperty(None)
        self.mokilall=ObjectProperty(None)
        self.count=0
        self.count1=3
        self.dialog = None
        self.strong=ObjectProperty(None)
        self.count2=0
        self.lomku=ObjectProperty(None)
        self.strong=ObjectProperty(None)
        # self.h=AnotherScreen()
        # self.add_widget(self.h,0)  
    def goodies(self):
        self.h=AnotherScreen()
        self.add_widget(self.h)  
    def star(self):  
        uhb=0
        klng=0 
        oplk=[]
        self.impoiu()
        try:
            address=open("address.txt","r") 
        except:
            pass
        if len(str(self.ids.mokilali.text))==0 : 
            yt=address.read()
        else:
            address=open("address.txt",'w')
            address.write(str(self.ids.mokilali.text))
            address.close() 
            address=open("address.txt","r")
            yt=address.read() 
        k=pd.DataFrame(pd.read_csv(str(yt)))
        pok=Popup(title="info.",size_hint=(0.8,0.8), auto_dismiss=True,background ='E:\lkom.jpg')
        if len(self.ids.strong.text)!=0 and int(self.ids.strong.text)<len(k):
            mnk=GridLayout(rows=3)
            t=FigureCanvasKivyAgg(plt.gcf())
            btn=Button(text="close")
            btn.bind(on_press=pok.dismiss)
            a=(k[int(self.ids.strong.text)-1:int(self.ids.strong.text)])
            mnk.add_widget(t)
            l=[]
            po=[]
            for i in a:
                l.append(str(i))
            a=str(a)
            for j in l:
                a=a.replace(j,"")
            srtgh=GridLayout(rows=2)
            srtgh.add_widget(Label(text=k['monk'][int(self.ids.strong.text)-1]))
            srtgh.add_widget(Label(text=str(k['no.'][int(self.ids.strong.text)-1])))
            mnk.add_widget(srtgh)
            b=a.replace(str(k['monk'][int(self.ids.strong.text)-1]),"").replace(str(k['no.'][int(self.ids.strong.text)-1]),"").replace(" ","")
            c=a.replace(str(k['monk'][int(self.ids.strong.text)-1]),"").replace(str(k['no.'][int(self.ids.strong.text)-1]),"").replace(" ","")
            if len(self.ids.strong.text)==1:
                for er in c:
                    po.append(er)
                po.remove('\n')
                po.remove(po[0])
                for lny in po:
                    if int(lny)==1:
                        uhb=uhb+1
                    klng=klng+1
                    oplk.append(uhb/float(klng))   
            elif len(self.ids.strong.text)==2:
                for er in b:
                    po.append(er) 
                po.remove('\n')
                po.remove(po[0])
                po.remove(po[0])
                for tong in po:
                    if int(tong)==1:
                        uhb=uhb+1
                    klng=klng+1
                    oplk.append(uhb/float(klng)) 
            elif len(self.ids.strong.text)==3:
                for er in b:
                    po.append(er) 
                po.remove('\n')
                po.remove(po[0])
                po.remove(po[0])
                po.remove(po[0])
                for bong in po:
                    if int(bong)==1:
                        uhb=uhb+1
                    klng=klng+1
                    oplk.append(uhb/float(klng)) 
            elif len(self.ids.strong.text)==4:
                for er in b:
                    po.append(er) 
                po.remove('\n')
                po.remove(po[0])
                po.remove(po[0])
                po.remove(po[0])
                po.remove(po[0])
                for rong in po:
                    if int(rong)==1:
                        uhb=uhb+1
                    klng=klng+1
                    oplk.append(uhb/float(klng)) 
            plt.plot(oplk)
            plt.ylabel('attandace ratio')
            plt.xlabel('no. of days')
            mnk.add_widget(btn)
            pok.content=mnk
            pok.open()
        else:
            sdf=Label(text=".csv file saved")
            pok.content=sdf
            pok.open()
    def click(self):
        image=Image(source='E:\circle-cropped.png', size_hint=(1,1),allow_stretch=True,size=(200,200))
        layout = GridLayout(cols=1) 
        popupLabel = Label(text = "Mayank Raj\nEmail:\nrajstarts35325@gmail.com\nphone n.\n6204396601",font_size=10)
        p=GridLayout(cols=2)
        k=GridLayout(cols=1) 
        k.add_widget(popupLabel)
        p.add_widget(image)
        p.add_widget(k)  
        closeButton = MDRoundFlatButton(text = "done",size_hint=(.15, 0.1) ) 
        layout.add_widget(p) 
        layout.add_widget(closeButton)         
        popup = Popup(title ='DEVELOPER',  
                      content = layout, 
                      size_hint =(0.7, 0.5),size =(700,500),background ='E:\monkuyoert.jpg')
        popup.open()    

        closeButton.bind(on_press = popup.dismiss)  
    def loknath(self,yu):
        if len(yu)!=0:
            f=open("power.txt","w")
            f.write(str(yu))
            f.close()
    def suri(self,text):
        try:
            k=open("power.txt","r")
            if text==str(k.read()):
                k.close()
                playout=GridLayout(rows=3)
                con=GridLayout(cols=2,size_hint=(1,0.3))
                ser=Popup(title='Login',size_hint=(0.7,0.5),background ='E:\dcadc.jpg')
                h=Label(text="enter new passcode",text_color=(0, 1, 0, 0))
                lo=TextInput(size_hint=(0.7,0.3))
                playout.add_widget(h) 
                playout.add_widget(lo)
                btn=Button(text="cancle")
                btn2=Button(text="confirm pass code")
                con.add_widget(btn)
                con.add_widget(btn2)
                playout.add_widget(con) 
                ser.content=playout
                ser.open() 
                btn.bind(on_press=ser.dismiss)
                btn2.bind(on_press=lambda l:self.loknath(lo.text))
                btn2.bind(on_press=ser.dismiss)
            else:
                if self.count1 != 1 :
                    self.count1=self.count1-1
                    return self.sonik()
                else:
                    print("hi")
        except:
            if text=="6532":
                playout=GridLayout(rows=3)
                con=GridLayout(cols=2,size_hint=(1,0.3))
                ser=Popup(title='Login',size_hint=(0.7,0.5),background ='E:\dcadc.jpg')
                h=Label(text="enter new passcode")
                lo=TextInput(size_hint=(0.7,0.3)) 
                playout.add_widget(h)
                playout.add_widget(lo)
                btn=Button(text="cancle")
                btn2=Button(text="confirm pass code")
                con.add_widget(btn)
                con.add_widget(btn2)
                playout.add_widget(con)
                ser.content=playout
                ser.open() 
                btn.bind(on_press=ser.dismiss)
                btn2.bind(on_press=lambda t:self.loknath(lo.text))
                btn2.bind(on_press=ser.dismiss)
            else:
                if self.count1 != 1 :
                    self.count1=self.count1-1
                    return self.sonik()
                else:
                    print("hi")

    def sonik(self): 
        playout1=GridLayout(rows=3)
        con=GridLayout(cols=2,size_hint=(1,0.3))
        cuser=Popup(title='Passcode',content=playout1,size_hint=(0.7,0.5),background ='E:\dcadc.jpg')
        if self.count1==3:
            ant=TextInput(text='',size_hint=(1,0.3),multiline=False,hint_text="Enter pin to change passcode",on_text_validate=cuser.dismiss)
            playout1.add_widget(Label(text='          4 digit\n      superviser code\n only'+' '+str(self.count1)+' trial are allowed',size_hint=(1,1)))
        else:
            ant=TextInput(text='',size_hint=(1,0.3),multiline=False,hint_text="enter again",on_text_validate=cuser.dismiss)
            playout1.add_widget(Label(text='          4 digit\n      superviser code\n only'+' '+str(self.count1)+' trial are allowed\nwrong pin',size_hint=(1,1)))
        playout1.add_widget(ant)
        b=Button(text='close')
        d=Button(text='login')
        con.add_widget(b)
        con.add_widget(d)
        playout1.add_widget(con) 
        cuser.open()
        b.bind(on_press=cuser.dismiss)
        d.bind(on_release=lambda x:self.suri(ant.text))
        d.bind(on_release=cuser.dismiss)
    def login(self,ant):
        try:
            jawd=open("power.txt","r")
            if ant==str(jawd.read()):
                jawd.close()
                self.count1=3
                popup = Popup(title='ATTANDANCE SHEET', size_hint=(0.9,0.8), auto_dismiss=False,background ='E:\monkuyoert.jpg')
                g=[]
                try:
                    address=open("address.txt","r")
                except:
                    pass
                if len(str(self.ids.mokilali.text))==0 : 
                    yt=address.read()
                else:
                    address=open("address.txt",'w')
                    address.write(str(self.ids.mokilali.text))
                    address.close() 
                    address=open("address.txt","r")
                    yt=address.read()
                book=pd.read_csv(str(yt))
                address.close()
                bookno=list(book['no.'])
                bookname=book['monk']
                m2=GridLayout(cols=1)
                btn2=Button(text='close',size_hint=(.3, 0.3))
                m2.add_widget(btn2)
                self.truth=[]
                for j in range(len(bookno)):
                    self.truth.append(bookname[j])
                layout = GridLayout(cols=2, spacing=10, size_hint_y=len(bookno)/10)
                layout.bind(minimum_height=layout.setter('height'))    
                kfom=SelectableGrid(cols=1, touch_multiselect=True,multiselect=True)   
                submit=Button(text='submit',size_hint=(0.3, 0.3)) 
                rt=open("ntn.txt","w")
                rt.write(str(submit))
                rt.close
                kfom.add_widget(submit)  
                for iuy in range(len(bookno)):
                    word=str(self.truth[iuy:iuy+1])
                    m2.add_widget(Label(text=word))
                    self.btn7 =CheckBox(active=False)
                    g.append(str(self.btn7)+"\n")
                    kfom.add_widget(self.btn7)
                layout.add_widget(m2)
                layout.add_widget(kfom)
                ht=open("button.txt","w")
                ht.writelines(g)
                ht.close
                root = ScrollView(size_hint=(1, 1), size=(popup.width, popup.height))
                root.add_widget(layout)
                popup.content=root
                btn2.bind(on_press=popup.dismiss)
                submit.bind(on_press=popup.dismiss) 
                popup.open()
                self.impoiu()
            else:
                if self.count1 != 1 :
                    self.count1=self.count1-1
                    return self.am()
                else:
                    print("hi")
        except:     
            if ant=="6532":
                self.count1=3
                popup = Popup(title='ATTANDANCE SHEET', size_hint=(0.8,1), auto_dismiss=False,background ='E:\monkuyoert.jpg')
                g=[]
                try:
                    address=open("address.txt","r")
                except:
                    pass
                if len(str(self.ids.mokilali.text))==0 : 
                    yt=address.read()
                else:
                    address=open("address.txt",'w')
                    address.write(str(self.ids.mokilali.text))
                    address.close() 
                    address=open("address.txt","r")
                    yt=address.read()
                book=pd.read_csv(str(yt))
                address.close()
                bookno=list(book['no.'])
                bookname=book['monk']
                m2=GridLayout(cols=1)
                btn2=Button(text='close',size_hint=(.3, 0.3))
                m2.add_widget(btn2)
                layout = GridLayout(cols=2, spacing=10, size_hint_y=len(bookno)/10)
                layout.bind(minimum_height=layout.setter('height'))    
                kfom=SelectableGrid(cols=1, touch_multiselect=True,multiselect=True)   
                submit=Button(text='submit',size_hint=(0.3, 0.3)) 
                rt=open("ntn.txt","w")
                rt.write(str(submit))
                rt.close
                kfom.add_widget(submit)  
                for iuy in range(len(bookno)):
                    m2.add_widget(Label(text=str(book["monk"][iuy])))
                    self.btn7 =CheckBox(active=False)
                    g.append(str(self.btn7)+"\n")
                    kfom.add_widget(self.btn7)
                layout.add_widget(m2)
                layout.add_widget(kfom)
                ht=open("button.txt","w")
                ht.writelines(g)
                ht.close
                root = ScrollView(size_hint=(1, 1), size=(popup.width, popup.height))
                root.add_widget(layout)
                popup.content=root
                btn2.bind(on_press=popup.dismiss)
                submit.bind(on_press=popup.dismiss) 
                popup.open()
                self.impoiu()
            else:
                
                if self.count1 != 1 :
                    self.count1=self.count1-1
                    return self.am()
                else:
                    print("hi")
            
    def kam(self,l,h):
        l.remove(l[0])
        t=monk()
        Url = 'https://www.sms4india.com/api/v1/sendCampaign'
        j=0
        t=0
        oi=[]
        mylines=[]
        with open("button.txt","r") as myfile:
            for myline in myfile:
                mylines.append(myline.replace("\n",""))
        te=sorted(list(set(mylines)-set(l)))
        for i in mylines:
            if i==te[j]:
                oi.append(0)
                j=j+1
            else:
                oi.append(1)
        yru=[]
        try:
            s=4
            with open("klesf.txt","r") as ttu:
                for mt in ttu:
                    yru.append(mt)
        except:
            s=5
        if s==4    :
            for ju in oi:
                if ju==0:
                    req_params = {
                                    'apikey':str(yru[0]),
                                    'secret':str(yru[1]),
                                    'usetype':"stage",
                                    'phone': str(int(h["no."][t])),
                                    'message':"your warden havent attend the class",
                                    'senderid':str(yru[2])
                                     }
                    requests.post(Url, req_params) 
                t=t+1 
            h[str(datetime.date.today()).replace("-"," ")]=oi
            liuoou=open("address.txt","r")
            h.to_csv(str(liuoou.read()), index=False)
            liuoou.close()

        else:
            pass
    def am(self): 
        playout=GridLayout(rows=3)
        con=GridLayout(cols=2,size_hint=(1,0.3))
        cuser=Popup(title='Login',content=playout,size_hint=(0.7,0.5),background ='E:\dcadc.jpg')
        if self.count1==3:
            ant=TextInput(text='',size_hint=(1,0.3),multiline=False,hint_text="Enter pin",on_text_validate=cuser.dismiss)
            playout.add_widget(Label(text='          4 digit\n      superviser code\n only'+' '+str(self.count1)+' trial are allowed',size_hint=(1,1)))
        else:
            ant=TextInput(text='',size_hint=(1,0.3),multiline=False,hint_text="enter again",on_text_validate=cuser.dismiss)
            playout.add_widget(Label(text='          4 digit\n      superviser code\n only'+' '+str(self.count1)+' trial are allowed\nwrong pin',size_hint=(1,1)))
        playout.add_widget(ant)
        b=Button(text='close')
        d=Button(text='login')
        con.add_widget(b)
        con.add_widget(d)
        playout.add_widget(con)
        cuser.open()
        b.bind(on_press=cuser.dismiss)
        d.bind(on_release=lambda x:self.login(ant.text))
        d.bind(on_release=cuser.dismiss)
    def good(self):
        date_dialog = MDDatePicker(callback=lambda x:self.get_date(date_dialog.sel_day,date_dialog.sel_month,date_dialog.sel_year))
        date_dialog.md_bg_color=[0.1,0.1,0,1]
        date_dialog.open()
    def get_date(self,p,q,w):
        try:    
            if len(str(p))!=2:
                p=str(0)+str(p)
            if len(str(q))!=2:
                q=str(0)+str(q)
            popup = Popup(title='ATTANDANCE SHEET', size_hint=(0.7,0.7), auto_dismiss=True,background ='E:\lkom.jpg')
            try:
                address=open("address.txt","r")
            except:
                pass
            if len(str(self.ids.mokilali.text))==0 : 
                yt=address.read()
            else:
                address=open("address.txt",'w')
                address.write(str(self.ids.mokilali.text))
                address.close() 
                address=open("address.txt","r")
                yt=address.read()
            book=pd.read_csv(str(yt))
            address.close()
            bookno=list(book['monk'])
            m2=GridLayout(cols=2)
            layout = GridLayout(cols=2, spacing=10, size_hint_y=len(bookno)/10)
            layout.bind(minimum_height=layout.setter('height'))     
            for iuy in range(len(bookno)):
                m2.add_widget(Label(text=str(book["monk"][iuy])))
                m2.add_widget(Label(text=str(book[str(w)+" "+str(q)+" "+str(p)][iuy])))
            layout.add_widget(m2)
            root = ScrollView(size_hint=(1, 1), size=(popup.width, popup.height))
            root.add_widget(layout)
            popup.content=root
            popup.open()
        except:
            popup = Popup(title='ATTANDANCE SHEET', size_hint=(0.5,0.5), auto_dismiss=True,background ='E:\lkom.jpg')
            popup.content=Label(text="no such data exist")
            popup.open()


    def impoiu(self):
        k=[]
        k.append(str(self.ids.mokila.text)+"\n")
        k.append(str(self.ids.mokilal.text)+"\n")
        k.append(str(self.ids.mokilall.text))
        try:
            rt=[]
            lk=0
            with open("klesf.txt","r") as f:
                for uy in f:
                    rt.append(f.read())
            for i in rt:
                if str(i)!=str(k[lk]) and len(str(k[lk]))>4:
                    k=0/0

        except:
            f=open("klesf.txt","w")
            f.writelines(k)
            f.close()
        f=open("klesf.txt","r")
        if len(str(f.read()))==0:
            self.ju("api ,seckret key,email")
            f=open("klesf.txt","w")
            f.writelines(k)
            f.close()


        
    def ju(self,rt):
        p=Popup(title="warning",size_hint=(0.5,0.3),background ='E:\monkuyoert.jpg')
        h=Label(text="your previously saved \n"+str(rt)+"\n   are missing\n   you can skip \nexcel student file if \nyou have filed it's showing",font_size=10)
        o=GridLayout(rows=2)
        rt=Button(text="close")
        o.add_widget(h)
        o.add_widget(rt)
        p.content=o
        rt.bind(on_press=p.dismiss)      
        p.open() 
class AnotherScreen(Screen): 
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button=ObjectProperty(None)
        self.tap_target_view = MDTapTargetView(
            outer_circle_color=(1,1,1),
            widget=self.ids.button,
            title_text="    tutorials",
            draw_shadow=True,
            title_text_size=50,
            title_text_color=(255,255,0,1),
            widget_position="right_top",
            description_text="  most part of our\n  life is always wasted \n    due to lack of knowledge",
            description_text_color=(100,100,0,1),
        )
    def monk(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()
    def lonk(self):
        p=monk()
        self.add_widget(p)
    def rongr(self):
        print("hi")
class SelectableGrid(FocusBehavior, CompoundSelectionBehavior, GridLayout):   
    def get_index_of_node(self, node, selectable_nodes):
        return super(SelectableGrid).get_index_of_node(node, selectable_nodes)
    def keyboard_on_key_down(self, popup, key, text, modifiers):
        if super(SelectableGrid, self).keyboard_on_key_down(
            popup, key, text, modifiers):
            return True
        if self.select_with_key_down(Popup, key, text, modifiers):
            return True
        return True

    def keyboard_on_key_up(self, popup, key):
        if super(SelectableGrid, self).keyboard_on_key_up(popup, key):
            return True
        if self.select_with_key_up(popup, key):
            return True
        return False

    def add_widget(self, widget):
        widget.bind(on_touch_down=self.CheckBox_touch_down,
                    on_touch_up=self.CheckBox_touch_up)
        return super(SelectableGrid, self).add_widget(widget)

    def CheckBox_touch_down(self, CheckBox, touch):
        if CheckBox.collide_point(*touch.pos):
            self.select_with_touch(CheckBox, touch)
            


    def CheckBox_touch_up(self, CheckBox, touch):
        if not (CheckBox.collide_point(*touch.pos) or
                self.touch_multiselect): 
            self.deselect_node(CheckBox)
            return (CheckBox)

    def select_node(self, node):
        node.background_color = (1, 0, 0, 1)
        return super(SelectableGrid, self).select_node(node)

    def get_index_of_node(self, node, selectable_nodes):
        return super(SelectableGrid).get_index_of_node(node, selectable_nodes) 

    def deselect_node(self, node):
        node.background_color = (1, 1, 1, 1)
        super(SelectableGrid, self).deselect_node(node)

    def on_selected_nodes(self, gird, nodes):    
        k=[]
        jk=open("address.txt","r")
        tur=pd.read_csv(str(jk.read()))
        jk.close()
        isj=list(tur['no.'])
        for t in nodes:
            k.append(str(t))
        k=sorted(k)
        m=open("ntn.txt","r")
        if k[0]==m.read():
            oi=Popup(title="warning",size_hint=(0.7,0.5),auto_dismiss=False,background ='E:\monkuyoert.jpg')
            h=GridLayout(rows=2)
            trt=Button(text="submit",size_hint=(1,0.5))
            h.add_widget(Label(text="submit response"))
            h.add_widget(trt)
            oi.content=h
            oi.open()
            trt.bind(on_press=oi.dismiss)
            hero=monk()
            m.close
            trt.bind(on_press=lambda dt:hero.kam(k,tur))


class ludo( MDApp):
    def build(self): 
        return  AnotherScreen()


if __name__=="__main__":
    ludo().run()
