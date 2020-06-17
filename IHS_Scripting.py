import sys
import os
input_file =  sys.argv[1]
#input_file = 'mapfile.txt'
kvdict = {}
with open(input_file,'r') as f:
    input_data = f.read().split('\n')
    for key_value in input_data:
        key_value=key_value.split()
        if len(key_value) >= 2:
            ky= key_value[0]
            val= key_value[1]
            kvdict[ky] = val

mapping_file_dir = sys.argv[2]
#mapping_file_dir = 'mapdir'
subdir = []
for root, dirs, files in os.walk(mapping_file_dir):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read().split('\n')
            new_file = os.path.join(root, "tmp.tmp")
            for key_value in content :
                key_value = key_value.split()
                if len(key_value) >= 2 :
                    ky = key_value[0]
                    val = key_value[1]
                    if kvdict.get(ky,'notfound') != "notfound":
                        new_val = kvdict.get(ky)
                        string = ky+' '+new_val + '\n'
                        with open(new_file, "a+") as f2 :
                            f2.write(string)
                    else:
                        string = ky + ' ' + val + '\n'
                        with open(new_file, "a+") as f2 :
                            f2.write(string)
            tmpfile = file_path
            os.remove(file_path)
            os.rename(new_file, tmpfile)
del input_data
del content
kvdict.clear()
print('Task Completed!')