import base64, lzma, os, shutil, codecs, zlib
from cryptography.fernet import Fernet
from time import sleep

class FemboyWBH:

    def __init__(self):
        os.system('cls')
        print("""[ Femboy WBH ]

[+] Find webhooks in python compiled exes or python files, by your sexy man vesper obv
[+] also I made this code in like an hour, its really simple but can infact find webhooks :)
        """)

        file = input("[+] Drop file --> ")
        content = str(open(file,"rb").read())
        self.__detect__(file,content)

    def __detect__(self,f:str,c):
        extension = f.split(".")[-1]
        if extension == "exe":
            if "python" in c:
                if "python311.dll" in c:
                    input("\n[+] Python 3.11 not supported yet.")
                    self.__init__()
                else:
                    self.__decompile__(f,c)
        if extension == "py":
            self.__pyFile__(f)

    def __webhook__(self, content:str):
        try:
            try:
                f2 = content.split('https://discord.com/api/webhooks')[1]
            except:
                try:
                    f2 = content.split('https://canary.discord.com/api/webhooks')[1]
                except:
                    try:
                        f2 = content.split('https://ptb.discord.com/api/webhooks')[1]
                    except:
                        try:
                            f2 = content.split('https://discordapp.com/api/webhooks')[1]
                        except:pass
            f3 = f2.split("/")[2][:68]
            f4 = f2.split("/")[1].strip()
            return "https://discord.com/api/webhooks/" +f4 +"/"+f3
        except:
            return ""

    def __decompile__(self,f,c):
        print("\n[+] Decompiling exe...")
        sleep(1.5)
        os.system("cls")
        os.system(f"pydumpck {f}")
        dirs = os.listdir(os.getcwd())
        os.system("cls")
        print("[+] Decompiled the EXE")
        for i in dirs:
            if i.startswith("output_"):
                folder = os.getcwd()+"\\"+i
        output_folder = os.listdir(folder)
        for a in output_folder:
            if a.endswith(".pyc.cdc.py"):
                if a.startswith("pyimod") or a.startswith("struct"):
                    pass
                else:
                    filename=a
                    decomp_file = folder+"\\"+a;break
        shutil.copy(decomp_file,f"decompiled/{a}")
        print("[+] Checking python source file.")
        self.__pyFile__(f"decompiled/{a}")
        
    def __pyFile__(self,f):
        content = open(f,"r+").read()
        W=self.__webhook__(content)
        if W == "":
            self.__deobf__(content)
        else:
            input(f"[!] Found Webhook : {W}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
            self.__init__()

    def __deobf__(self,c:str):
        try:
            shit_lzma = c.split("= b'")[1].split("'\n")[0].encode().decode('unicode_escape').encode("raw_unicode_escape")
            shit_lzma = lzma.decompress(shit_lzma).decode()
            obf_code = shit_lzma.split(";__import__")[0]
            exec(f'''{obf_code}\ncode = base64.b64decode(codecs.decode(____,'rot13')+_____+______[::-1]+_______);open("RRR.txt","w+").write(str(code))''')
            code = open("RRR.txt","r+").read()
            W=self.__webhook__(code)
            if W == "":
                os.remove("RRR.txt")
            else:
                os.remove("RRR.txt")
                input(f"\n[!] Found Webhook : {W}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
                self.__init__()
        except:
            pass
        try:
            c=c.split("(base64.b64decode(b'")[1].split("'))")[0]
            shit_code = lzma.decompress(base64.b64decode(c.encode())).decode()
            shit_lzma = shit_code.split("= b'")[1].split("'\n")[0].encode().decode('unicode_escape').encode("raw_unicode_escape")
            shit_lzma = lzma.decompress(shit_lzma).decode()
            obf_code = shit_lzma.split(";__import__")[0]
            exec(f'''{obf_code}\ncode = base64.b64decode(codecs.decode(____,'rot13')+_____+______[::-1]+_______);open("RRR.txt","w+").write(str(code))''')
            code = open("RRR.txt","r+").read()
            W=self.__webhook__(code)
            if W == "":
                os.remove("RRR.txt")
            else:
                os.remove("RRR.txt")
                input(f"\n[!] Found Webhook : {W}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
                self.__init__()
        except:
            pass
        try:
            try:
                c=c.split(";eval")[0]
            except:
                c=c.split("eval")[0]
            key = c.split("Fernet('")[1].split("')")[0]
            content = c.split(".decrypt(b'")[1].split("')")[0]
            content = Fernet(f"{key}").decrypt(content.encode()).decode()
            W=self.__webhook__(content)
            if W == "":
                input()
            else:
                input(f"\n[!] Found Webhook : {W}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
                self.__init__()
        except:
            pass
        try:
            if "from config import __CONFIG__" in c:
                dirs = os.listdir(os.getcwd())
                for i in dirs:
                    if i.startswith("output_"):
                        folder = os.getcwd()+"\\"+i;break
                cont = str(open(folder+"\\PYZ-00.pyz_extract\\config.pyc.cdc.py","r+").read())
                W=self.__webhook__(cont)
                if W == "":
                    pass
                else:
                    input(f"\n[!] Found Webhook : {W}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
                    self.__init__()
                enc_wbh = cont.split(": __import__('base64')")[-1]
                try:
                    enc_wbh = enc_wbh.split(".decompress(b'")[1].split("')).decode() }")[0]
                except:
                    enc_wbh = enc_wbh.split('.decompress(b"')[1].split('")).decode() }')[0]
                wbh = base64.b64decode(zlib.decompress(enc_wbh.encode().decode('unicode_escape').encode("raw_unicode_escape"))).decode()
                input(f"\n[!] Found Webhook : {wbh}\n[!] DELETE THE OUTPUT FOLDER TO CONTINUE !\n\n[+] Press ENTER to continue..")
                self.__init__()
        except:
            pass

# install package
#os.system("pip install pydumpck")

FemboyWBH()