[app]
title = System Update
package.name = nemosupdate
package.domain = com.nemos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,jnius,android
orientation = portrait
fullscreen = 0
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INSTALL_PACKAGES
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a
