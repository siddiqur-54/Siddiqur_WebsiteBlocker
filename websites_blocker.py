import ctypes
import sys
from tkinter import *
from tkinter.messagebox import *

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    host_files = {
        'Windows': r"C:\Windows\System32\drivers\etc\hosts",
        'Linux': '/etc/host'
    }
    localhost = '127.0.0.1'

    def block(win):
        def block_websites(websites):
            host_file = host_files['Windows']
            sites_to_block = list(websites.split(' , '))

            with open('blocked_websites.txt', 'r+') as blocked_websites_txt:
                blocked_websites_txt.seek(0, 2)
                for site in sites_to_block:
                    blocked_websites_txt.write(site)

            with open(host_file, 'r+') as hostfile:
                content_in_file = hostfile.read()

                for site in sites_to_block:
                    if site not in content_in_file:
                        hostfile.write(localhost + '\t' + site + '\n')
                        showinfo('Websites blocked!', message='We have blocked the websites you wanted blocked!')
                    else:
                        showinfo('Website Already blocked!', 'A website you entered is already blocked')

        blck_wn = Toplevel(win, background='Cyan')
        blck_wn.title("Block Websites")
        blck_wn.geometry('300x200')
        blck_wn.resizable(False, False)

        Label(blck_wn, text='Block Websites', background='Cyan', font=("Georgia", 16)).place(x=80, y=0)
        Label(blck_wn, text='Enter the URLs(www.site_name.com)', background='Cyan', font=('Times', 13)).place(
            x=0, y=70)

        sites = Text(blck_wn, width=35, height=3)
        sites.place(x=0, y=100)

        submit_btn = Button(blck_wn, text='Submit', bg='Cyan', command=lambda: block_websites(sites.get('1.0',END)))
        submit_btn.place(x=100, y=160)

    root = Tk()
    root.title("Siddiqur Website Blocker")
    root.geometry('400x200')
    root.wm_resizable(False, False)

    Label(root, text='Siddiqur Website Blocker', font=("Times", 16)).place(x=45, y=0)
    Button(root, text='Block a Website', font=('Times', 16), bg='Cyan', command=lambda: block(root)).place(x=110, y=90)

    root.update()
    root.mainloop()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)