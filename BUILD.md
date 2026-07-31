#### Windows

The web area is using hardware acceleration, a performance multiplier for rendering. It is not possible to sample pixels using the classic `BitBlt` API. `BitBlt` will return a black region where the GPU projects its output. It is necessary to capture the GPU representation of the window and locally convert it to bitmap.

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

### Syntax

[miyako.github.io](https://miyako.github.io/2023/03/08/4d-plugin-screen-capture.html)
