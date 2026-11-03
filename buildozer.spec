name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build APK
        uses: digreatbrian/buildozer-action@v2
        with:
          command: buildozer android debug
          buildozer_version: stable
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: MD17-APK
          path: bin/*.apk
