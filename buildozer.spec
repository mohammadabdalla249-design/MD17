name: build
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y openjdk-17-jdk zip unzip python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install buildozer Cython==0.29.33
      - name: Fix Licenses and Build
        run: |
          mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          yes | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses || true
          $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --install "build-tools;33.0.2" "build-tools;37.0.0" "platforms;android-33" --verbose || true
          buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: MD17-APK
          path: bin/*.apk
