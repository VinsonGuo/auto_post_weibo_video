import os
import sched

import time

import weibo

if __name__ == '__main__':
    files = os.listdir('res')
    fileNames = [name.split('.')[0] for name in files]
    print(fileNames)

    for i in range(files.__len__()):
        w = weibo.login("name", "pwd")
        w.update_status(fileNames[i], 'res/' + files[i], 'cover.jpg')
        time.sleep(60 * 10)
