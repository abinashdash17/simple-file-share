Steps:
1. Install python 3
2. open this directory in CMD and run 
    pip install --user -r requirements.txt
3. copy the file 'simple-file-share.py' and paste it in the directory to be shared
4. Open the directory in CMD and run
    python .\simple-file-share.py

Note:
Based on the background color of the terminal, the default print_ascii may not work.
So I have used the invert parameter in print_ascii funtion to generate ascii qr code for dark bg consoles.
ref:https://github.com/lincolnloop/python-qrcode/blob/main/qrcode/main.py#L292

todo:
get wifi ip
https://groups.google.com/g/comp.lang.python/c/tF-SXWvBVjk?pli=1

sources:
https://pypi.org/project/qrcode/
