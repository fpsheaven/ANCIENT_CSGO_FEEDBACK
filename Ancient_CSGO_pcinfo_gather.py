import os,sys,datetime,shutil,webbrowser,time
from ftplib import FTP
path="C:\\frequencycs"
if os.path.isdir(path)==1:
    shutil.rmtree(path)

date=str(datetime.date.today())
os.mkdir("C:\\frequencycs");os.chdir("C:\\frequencycs");
print ("run this program only if you are having issues on ancient.only!")
print ("It will export the system specs to a folder on the c drive.")
print ("are you sure you are having issues ONLY on ANCIENT?")
quit=input("If you do have issues press Y to continue or if you dont, press N to exit the utility \n ")
if quit!="y" and quit!="Y":
    sys.exit()
else:
    print ("Gathering report. Please wait 30 seconds.")
    username=os.getlogin()
    os.system('cmd /C "MSInfo32 /report C:\\frequencycs\\report.txt"')
    date=date.replace(" ","");date=date.replace("/","-");date=date.replace(":","-")
    os.rename("report.txt",username+"_"+"ANCIENT_"+date+".txt")
    print ("Uploading report to my server")
    user_file=os.listdir(path)[0] #OUTPUT NAMEy
    ftp=FTP()#HIDDEN SSH DATA
    ftp.login() #HIDDEN SSH DATA
    ftp.cwd("/ANCIENT")
    with open(user_file, "rb") as file:
        ftp.storbinary(f"STOR {user_file}", file)
    ftp.quit()
    print ("Upload done. Goodbye")
    time.sleep(3)
