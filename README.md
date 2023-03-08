![version](https://img.shields.io/badge/version-17%2B-3E8B93)
![platform](https://img.shields.io/static/v1?label=platform&message=mac-intel%20|%20mac-arm%20|%20win-64&color=blue)
[![license](https://img.shields.io/github/license/miyako/4d-plugin-screen-capture)](LICENSE)
![downloads](https://img.shields.io/github/downloads/miyako/4d-plugin-screen-capture/total)

4d-plugin-screen-capture
========================

Screen capture the desktop or a specified window.

#### Windows

The web area is using hardware acceleration, a performance multiplier for rendering. It is not possible to sample pixels using the class `BitBlt` API. `BitBlt` will return a black region where the GPU projects its output. It is necessary to capture the GPU representation of the window and locally convert it to bitmap.

On Windows, it is not possible to capture a child window of the MDI using this command. 

You can only specify a window reference in **SDI mode**. 

#### Note to self

On Windows, you must install **Graphic Tools** in 

* Apps > Optional features > Add an optional feature

in order to call [D3D11CreateDevice](https://learn.microsoft.com/en-us/windows/win32/api/d3d11/nf-d3d11-d3d11createdevice) with the  `D3D11_CREATE_DEVICE_DEBUG` flag. This is not mandatory for using the plugin.

#### Mac

[CGWindowListCreateImage](https://developer.apple.com/documentation/coregraphics/1454852-cgwindowlistcreateimage?preferredLanguage=occ) is used with `CGRectNull` to capture a window. 

The shadow is ignored (`kCGWindowImageBoundsIgnoreFraming`).

For the screen, the `kCGNullWindowID` and `kCGWindowListOptionOnScreenOnly` is used.

## Syntax

```4d
image:=Capture screen ({monitor})
image:=Capture window (window)
```

Parameter|Type|Description
------------|------------|----
image|PICTURE|Captured image
window|LONGINT|Window reference
monitor|LONGINT|Monitor index (Windows only)
