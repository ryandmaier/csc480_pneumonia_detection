


# import os

# base_dir = 'chest_xray/'

# train_dir = os.path.join(base_dir, 'train')
# validation_dir = os.path.join(base_dir, 'val')

# train_NORMAL_dir = os.path.join(train_dir, 'NORMAL')
# train_PNEUMONIA_dir = os.path.join(train_dir, 'PNEUMONIA')

# train_NORMAL_fnames = os.listdir(train_NORMAL_dir)
# train_PNEUMONIA_fnames = os.listdir(train_PNEUMONIA_dir)

# # need to move 2/7ths of train data to val folder
# # currently val is the same as test, prob not the best for testing

# print(train_NORMAL_fnames)

import os
import random
import subprocess

# os.system() # make train dir or clear if not made
# sys.path.append('chest_xray')

base_dir = 'chest_xray/'

dir = os.path.join(base_dir, 'all_data')

NORMAL_dir = os.path.join(dir, 'NORMAL')
PNEUMONIA_dir = os.path.join(dir, 'PNEUMONIA')

fnames = [os.listdir(NORMAL_dir) , os.listdir(PNEUMONIA_dir) ]
types = ['NORMAL', 'PNEUMONIA']
folders = ['train', 'val', 'test']

print(len(fnames[0]) + len(fnames[1]))

train_val_test_split = [0.8, 0.8+0.1, 0.8+0.1+0.1]

data = [[[],[]] , [[],[]] , [[],[]]] # train, val, test, with NORMAL, PNEUMONIA inside
for type in range(2):
    print(type)
    for image in fnames[type]:
        orig_path = base_dir+'all_data/'+types[type]+'/'+image
        new_path = types[type]
        r = random.random()

        if r < train_val_test_split[0]:
            data[0][type].append(image)
            new_path = folders[0] + '/' + new_path
        elif r < train_val_test_split[1]:
            data[1][type].append(image)
            new_path = folders[1] + '/' + new_path
        elif r < train_val_test_split[2]:
            data[2][type].append(image)
            new_path = folders[2] + '/' + new_path

        new_path = base_dir + new_path
        sys_cmd = 'MOVE '+orig_path+' '+new_path
        
        # os.system(sys_cmd)
        subprocess.call('C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe '+sys_cmd, shell=True)
        print(sys_cmd)

print(len(data[0][0]))
print(len(data[1][0]))
print(len(data[2][0]))
print(len(data[0][1]))
print(len(data[1][1]))
print(len(data[2][1]))