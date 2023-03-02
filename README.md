![version](https://img.shields.io/badge/version-17%2B-3E8B93)
![platform](https://img.shields.io/static/v1?label=platform&message=mac-intel%20|%20mac-arm%20|%20win-64&color=blue)
[![license](https://img.shields.io/github/license/miyako/4d-plugin-screen-capture)](LICENSE)
![downloads](https://img.shields.io/github/downloads/miyako/4d-plugin-screen-capture/total)

4d-plugin-screen-capture
========================

Screen capture the desktop or a specified window

#### Note to self

On Windows, you must install **Graphic Tools** in 

* Apps > Optional features > Add an optional feature

This is needed for [D3D11CreateDevice](https://learn.microsoft.com/en-us/windows/win32/api/d3d11/nf-d3d11-d3d11createdevice) with `D3D11_CREATE_DEVICE_DEBUG`

## Syntax

```4d
image:=Capture screen
image:=Capture window (window)
```

Parameter|Type|Description
------------|------------|----
image|PICTURE|Captured image
window|LONGINT|Window reference
