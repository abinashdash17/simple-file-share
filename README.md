Steps:
1. Install python 3
2. Open this directory in CMD and run 
      pip install --user -r requirements.txt
3. Copy the file 'simple-file-share.py' and paste it in the directory to be shared
4. Open the directory in CMD and run
      python .\simple-file-share.py
5. Scan the qr code to browse all the files in the directory and download your desired file.

Note:
1. Based on the background color of the terminal, 
   If you are using a terminal with "white background", the default qr_code output may not work. In that case, use the below command 
      python .\simple-file-share.py w
2. Your device may contain more than 1 network interface. Try using a diferent value for "nw_interface_id", if the default qr code doesn't work.

todo:

sources:
https://pypi.org/project/qrcode/
https://groups.google.com/g/comp.lang.python/c/tF-SXWvBVjk?pli=1
ref:https://github.com/lincolnloop/python-qrcode/blob/main/qrcode/main.py#L292
