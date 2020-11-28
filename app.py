from tkinter import *
from fuzzywuzzy import fuzz
import matplotlib.pyplot as mp

class Message_Encrypt:
    def __init__(self,root):
        self.root=root
        self.root.title("String Visualization")
        self.root.geometry("400x475")
        self.root.iconbitmap("logo3.ico")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_visualize['background']="black"
            but_visualize['foreground']="cyan"
  
        def on_leave1(e):
            but_visualize['background']="SystemButtonFace"
            but_visualize['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        def clear():
            text_first.delete('1.0',"end")
            text_second.delete('1.0',"end")


        def visual():
            s1=text_first.get('1.0','end')
            s2=text_second.get('1.0','end')
            ratio=fuzz.ratio(s1,s2)
            partial_ratio=fuzz.partial_ratio(s1,s2)
            sort_ratio=fuzz.token_sort_ratio(s1,s2)
            wratio=fuzz.WRatio(s1,s2)

            names=['ratio','partial_ratio','sort_ratio','wratio']
            h=[ratio,partial_ratio,sort_ratio,wratio]
            mp.bar(names,h,width=0.2)
            mp.xlabel("Names of ratio")
            mp.ylabel("Ratio length for Similar Strings")
            mp.title("String Similarities Visualization")
            mp.show()


            




#===========frame==================================#

        mainframe=Frame(self.root,width=400,height=475,relief="ridge",bd=4)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=393,height=207,relief="ridge",bd=4)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=393,height=207,relief="ridge",bd=4)
        secondframe.place(x=0,y=207)

        thirdframe=Frame(mainframe,width=393,height=52,relief="ridge",bd=4,bg="gray77")
        thirdframe.place(x=0,y=415)

#===================firstframe==============================#
        
        scol=Scrollbar(firstframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text_first=Text(firstframe,height=10,width=45,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text_first.place(x=0,y=0)
        scol.config(command=text_first.yview)

#====================secondframe============================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text_second=Text(secondframe,height=10,width=45,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text_second.place(x=0,y=0)
        scol.config(command=text_second.yview)

#==================third====================================#

        but_visualize=Button(thirdframe,text="Visualize",width=13,font=('times new roman',14),cursor="hand2",command=visual)
        but_visualize.place(x=20,y=3)
        but_visualize.bind("<Enter>",on_enter1)
        but_visualize.bind("<Leave>",on_leave1)

        but_clear=Button(thirdframe,text="Clear",width=13,font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=235,y=3)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


if __name__ == "__main__":
    root=Tk()
    Message_Encrypt(root)
    root.mainloop()
