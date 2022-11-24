import os,sys,datetime,paramiko,shutil,webbrowser
path="C:\\frequencycs"


date=str(datetime.date.today())
os.mkdir("C:\\frequencycs");os.chdir("C:\\frequencycs");
print ("run this program only if you are having issues on ancient.only!")
print("The program will work for 3 days (trial ends),need to find a ftp server to upload the files.")
print ("It will export the system specs to a folder on the c drive.")
print ("are you sure you are having issues ONLY on ANCIENT?")
quit=input("If you do, press Y or if you, dont press N to exit the utility   ")
if quit=="N" or quit=="n":
    sys.exit()
else:
    username=os.getlogin()
    os.system('cmd /C "MSInfo32 /report C:\\frequencycs\\report.txt"')
date=date.replace(" ","");date=date.replace("/","-");date=date.replace(":","-")
os.rename("report.txt",username+"_"+"ANCIENT_"+date+".txt")

user_file=os.listdir(path)[0] #OUTPUT NAME

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="64.227.38.17",username="server",password="Serverpassword1",port=22)

sftp_client=ssh.open_sftp()
sftp_client.put("C:/frequencycs/"+user_file,"/ancient/"+user_file)
sftp_client.close()
ssh.close()
print("File uploaded")
exit(0)
