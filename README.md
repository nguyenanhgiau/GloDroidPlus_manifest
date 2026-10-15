# GloDroid+ LineageOS
Getting started
To get started with Android/LineageOS, you'll need to get familiar with Source Control Tools.

To initialize your local repository using the LineageOS trees, use a command like this:
```bash
mkdir GlodroidPlus_LineageOS && cd GlodroidPlus_LineageOS
repo init -u https://github.com/LineageOS/android.git -b lineage-24.0 --git-lfs
git clone https://github.com/nguyenanhgiau/GloDroidPlus_manifest.git -b rpi4-lineage-24.0 .repo/local_manifests
```
Then to sync up:
```bash
repo sync
```

# Build instruction
1. Set up the Android build environment:

```bash
. build/envsetup.sh
```

2. Select the build target (one of them: `rpi4` for tablet UI, `rpi4_tv` for Android TV, or `rpi4_car` for Android Automotive):

```bash
lunch rpi4-aosp_current-userdebug
#lunch rpi4_tv-aosp_current-userdebug
#lunch rpi4_car-aosp_current-userdebug
```
Note: not tested rpi4_tv and rpi4_car yet.

3. Build the images:

If you want to integrate GMS into your build, run the cmd below:
```bash
export WITH_GMS=true
```
Refer to [microG Mobile Services](https://github.com/lineageos4microg/android_vendor_partner_gms/blob/master/README.md) to get more information.

Then, compile your product:
```bash
make images -j$(nproc) # The output will be generated at $OUT/images.tar.gz
make sdcard -j$(nproc) # The output will be generated at $OUT/sdcard.img
```

## How to Flash an Image to an RPi 4 Device (Choose One of the Methods Below)

### Write the Full Image to an SD Card

1. Insert your SD card into a card reader and connect it to your Linux PC.

2. Identify your SD card's device node (for example, `/dev/sdc` or `/dev/mmcblk0`) using `lsblk`.

⚠️ **WARNING:** Be absolutely certain that you have identified the correct device node before running the `dd` command. Specifying the wrong drive will permanently erase your system data!

3. Flash the image to your SD card:
```bash
# Replace /dev/sdX with your actual device node
sudo umount /dev/sdX*
cd $OUT
sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress conv=fsync
```

4. Insert the flashed SD card into your Raspberry Pi 4.

5. (Optional but recommended) Connect a UART serial cable to the GPIO pins to capture low-level boot logs from U-Boot and the kernel (`dmesg`).

6. Connect the Raspberry Pi to your PC using a USB Type-C cable to power it on.

7. Monitor the serial output and wait for the Android UI to boot.

### Write the Bootloader to an SD Card, then Flashing via fastboot

1. Insert your SD card into a card reader and connect it to your Linux PC.

2. Identify your SD card's device node (for example, `/dev/sdc` or `/dev/mmcblk0`) using `lsblk`.

⚠️ **WARNING:** Be absolutely certain that you have identified the correct device node before running the `dd` command. Specifying the wrong drive will permanently erase your system data!

3. Flash the image to your SD card:
```bash
# Replace /dev/sdX with your actual device node
sudo umount /dev/sdX*
cd $OUT
sudo dd if=deploy-sd.img of=/dev/sdX bs=1M status=progress conv=fsync
```

4. Insert the flashed SD card into your Raspberry Pi 4.

5. (Optional but recommended) Connect a UART serial cable to the GPIO pins to capture low-level boot logs from U-Boot and the kernel (`dmesg`).

6. Connect the Raspberry Pi to your PC using a USB Type-C cable to power it on.

7. Wait for the RPi 4 to enter bootloader mode.

8. On your PC, run the following commands:
```bash
cd $OUT
./flash-sd.sh
```

9. Wait for the flashing process to finish.

# Acknowledgements & License
This project is heavily based on the outstanding work of upstream projects:
* [GloDroid](https://github.com/GloDroidCommunity/raspberry-pi)
* [Raspberry-vanilla](https://github.com/raspberry-vanilla/android_local_manifest)
* [LineageOS](https://github.com/LineageOS/android)

GloDroid+ does not claim ownership of the original codebases. All modifications and integrated source codes strictly inherit the respective open-source licenses of their original upstream projects (primarily the Apache License 2.0 for AOSP components and GNU GPLv2 for Kernel/U-Boot components). Please refer to the specific repositories for detailed licensing information.

***

Have fun building!