import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
                    
def main():
    access_token="sl.BId5A90ybCuJ1OgXB8dPCOJqSF3UIkSs9XLCDapk0fAPEsDy-fTKtZKBVptibC9Ovc8UVXB6ewNpplk1-E3SNtLu4lmVBb1qXDFbPfozUsodePoCZjEEkDRtc3ysjjXA2HTTCvEWMmQ"
    transferData=TransferData(access_token)
    file_from=input("Enter the file path that you want to transfer:")
    file_to=input("Enter the path of dropbox:")
    transferData.upload_file(file_from,file_to)
    print("The file has been uploaded")

main()