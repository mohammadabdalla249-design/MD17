[app]
title = MD17 Store
package.name = md17store
package.domain = com.md17.store
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = arm64-v8a
p4a.branch = master
