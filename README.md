### Device-specific configuration for building AOSP Android 15 for Raspberry Pi 4

***

### How to build (Ubuntu 22.04 LTS)

1. Set up the [Android build environment](https://source.android.com/docs/setup/start/requirements).

2. Install required packages:

```
sudo apt-get install dosfstools e2fsprogs fdisk kpartx mtools rsync
```

3. Initialize the repo:

```
repo init --depth=1 -u https://android.googlesource.com/platform/manifest -b android-platform-15.0.0_r3
git clone https://gitlab.com/glodroid_platform/glodroid_manifest.git -b glodroid-2.1 .repo/local_manifests
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

8.1. Use Etcher (or similar tools) to write `out/target/product/rpi4/sdcard.img` to your SD card.

8.2. Insert the SD card into the Raspberry Pi.

8.3. Connect the UART cable to capture the serial log.

8.4. Connect the Raspberry Pi to your PC via USB and power it on.

8.5. Wait for the device to enter fastboot mode.

8.6. Run the following command to flash the software:

```
cd $OUT
./flash-sd.sh
```

Also see the [Linux kernel build instructions](https://github.com/raspberry-vanilla/android_kernel_manifest/tree/android-16.0).

***

### Issues

- [Android](https://github.com/raspberry-vanilla/android_local_manifest/issues)
- [Linux kernel](https://github.com/raspberry-vanilla/android_kernel_manifest/issues)

***

### Wiki

- [Audio](https://github.com/raspberry-vanilla/android_local_manifest/wiki/Audio)
- [Desktop mode](https://github.com/raspberry-vanilla/android_local_manifest/wiki/Desktop-mode)
- [DSI display](https://github.com/raspberry-vanilla/android_local_manifest/wiki/DSI-display)
- [HDMI display](https://github.com/raspberry-vanilla/android_local_manifest/wiki/HDMI-display)
- [HDMI-CEC](https://github.com/raspberry-vanilla/android_local_manifest/wiki/HDMI-CEC)
- [Interfaces](https://github.com/raspberry-vanilla/android_local_manifest/wiki/Interfaces)
- [USB boot](https://github.com/raspberry-vanilla/android_local_manifest/wiki/USB-boot)
- [Utilities](https://github.com/raspberry-vanilla/android_local_manifest/wiki/Utilities)
- [Video decoding & encoding](https://github.com/raspberry-vanilla/android_local_manifest/wiki/Video-decoding-&-encoding)
