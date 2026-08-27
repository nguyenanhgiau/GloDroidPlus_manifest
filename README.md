# GloDroid+
An AOSP distribution for the Raspberry Pi 4, specifically designed for research, testing, and hardware prototyping for Android Platform Engineers.

The Raspberry Pi 4 is an accessible hardware platform with a vast, dynamic support community, possessing sufficient processing power to seamlessly run the Android operating system.

This project is the combination of two open-source repositories: GloDroid and Raspberry-vanilla. The goal of GloDroid+ is to eliminate existing drawbacks while inheriting the technical excellence of both original projects:
* Full support for U-Boot as the Bootloader.
* Integrated Recovery environment and Fastbootd.
* Support for Super Partitions (Dynamic Partitions) architecture.
* A clean, modular codebase architecture that is easy to maintain and expand for custom hardware development.

# Acknowledgements & License
This project is heavily based on the outstanding work of two upstream projects:
* [GloDroid](https://github.com/GloDroidCommunity/raspberry-pi)
* [Raspberry-vanilla](https://github.com/raspberry-vanilla/android_local_manifest)

GloDroid+ does not claim ownership of the original codebases. All modifications and integrated source codes strictly inherit the respective open-source licenses of their original upstream projects (primarily the Apache License 2.0 for AOSP components and GNU GPLv2 for Kernel/U-Boot components). Please refer to the specific repositories for detailed licensing information.

***

## How to build (Ubuntu 22.04 LTS)

1. Set up the [Android build environment](https://source.android.com/docs/setup/start/requirements).

2. Install required packages:

```
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

3. Initialize the repo:

```
mkdir Glodroid && cd Glodroid
repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-platform-17.0.0_r1 -m default.xml
git clone https://github.com/nguyenanhgiau/GloDroidPlus_manifest.git -b glodroid-a17 .repo/local_manifests
```

4. Sync the source code:

```
repo sync -c -j$(nproc) --no-clone-bundle
```

5. Set up the Android build environment:

```
. build/envsetup.sh
```

6. Select the build target (tablet UI, `tv` for Android TV, or `car` for Android Automotive):

```
lunch rpi4-trunk_staging-userdebug
lunch rpi4_car-trunk_staging-userdebug
lunch rpi4_tv-trunk_staging-userdebug
```

7. Build the images:

```
make images -j$(nproc)
make sdcard -j$(nproc)
```

## How to flash the image to rpi4 device

1. Insert your SD card into a card reader and connect it to your Linux PC.

2. Identify your SD card device node (e.g., /dev/sdc, /dev/mmcblk0) using lsblk.

⚠️ WARNING: Be absolutely certain you have the correct device node before running the dd command. Specifying the wrong drive will permanently erase your system data!

3. Flash the image to your SD card:
```bash
# Replace /dev/sdX with your actual device node
sudo umount /dev/sdX* 
cd $OUT
sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress conv=fsync
```

4. Insert the flashed SD card into your Raspberry Pi 4

5. (Optional but recommended) Connect a UART serial cable to the GPIO pins to capture the low-level boot logs (U-Boot & Kernel dmesg).

6. Connect the Raspberry Pi to your PC via a USB Type-C cable to power it on.

7. Monitor the serial output and wait for the Android UI to boot up.

Have fun building!