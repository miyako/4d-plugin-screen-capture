![version](https://img.shields.io/badge/version-17%2B-3E8B93)
![platform](https://img.shields.io/static/v1?label=platform&message=mac-intel%20|%20mac-arm%20|%20win-64&color=blue)
[![license](https://img.shields.io/github/license/miyako/4d-plugin-screen-capture)](LICENSE)
![downloads](https://img.shields.io/github/downloads/miyako/4d-plugin-screen-capture/total)

4d-plugin-screen-capture
========================

Screen capture the desktop or a specified window

**Important**: versions prior to ``2.1.0`` have serious memory leak on Mac, because of [``TIFFRepresentation``](https://developer.apple.com/documentation/appkit/nsimage/1519841-tiffrepresentation?language=objc).

## Syntax

```4d
image:=Capture screen
image:=Capture window (window)
```

Parameter|Type|Description
------------|------------|----
image|PICTURE|Captured image
window|LONGINT|Window reference
