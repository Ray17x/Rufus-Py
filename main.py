import psutil
import os
import subprocess

##### FUNCTIONS #####
###USB RECOGNITION###
paths=["/media", "/run/media"]
def find_usb():
    usbdict = {}    #DICTIONARY WHERE USB MOUNT PATH IS KEY AND LABEL IS VALUE
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            print(directories)
        # else:
        #     print("doesnt exist")
    for part in psutil.disk_partitions():
        for i in directories:
            mountpaths = f"/media/{i}"
            # if os.path.exists(mountpaths) and os.path.isdir(mountpaths):
            #     print(mountpaths)
            if part.mountpoint == mountpaths:
                device_node = part.device
                # break
                if device_node:
                    # -d (device only), -n (no headings), -o (output column LABEL)
                    label = subprocess.check_output(["lsblk", "-d", "-n", "-o", "LABEL", device_node], text=True).strip()   #CHECKS FOR LABELS OF A USB
                    print(f"The label for {mountpaths} is: {label}")
                    usbdict[mountpaths] = label
                    print(usbdict)
                else:
                    print("Mount point not found.")

find_usb()

