### Device-specific configuration for building AOSP Android 16 for Raspberry Pi 4

***

### How to build (Ubuntu 22.04 LTS)

1. Set up the [Android build environment](https://source.android.com/docs/setup/start/requirements).

2. Install required packages:

```
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

3. Initialize the repo:

```
mkdir Glodroid && cd Glodroid
repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-platform-17.0.0_r1 -m default.xml
git clone https://gitlab.com/glodroid_platform/glodroid_manifest.git -b glodroid-a17 .repo/local_manifests
```

4. Sync the source code:

```
repo sync
```

5. Set up the Android build environment:

```
. build/envsetup.sh
```

6. Select the target device:

```
lunch rpi4-trunk_staging-userdebug
```

7. Build the images:

```
make images -j$(nproc)
make sdcard -j$(nproc)
```

8. Create a flashable image for the `rpi4` device:

8.1. Plug SDCard to SDCard Reader and connect it to your Linux PC.

8.2. Write `out/target/product/rpi4/sdcard.img` to your SD card.
```bash
sudo umount /dev/sdc* #Replace sdc with your device node
cd $OUT
sudo dd if=sdcard.img of=/dev/sdc bs=1M status=progress conv=fsync
```

8.3. Insert the SD card into your Raspberry Pi.

8.4. Connect the UART cable to capture the serial log.

8.5. Connect the Raspberry Pi to your PC via a USB cable and power it on.

8.6. Wait for a while to see the result.


Have fun!!!