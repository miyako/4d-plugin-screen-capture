![version](https://img.shields.io/badge/version-17%2B-3E8B93)
![platform](https://img.shields.io/static/v1?label=platform&message=mac-intel%20|%20mac-arm%20|%20win-64&color=blue)
[![license](https://img.shields.io/github/license/miyako/4d-plugin-screen-capture)](LICENSE)
![downloads](https://img.shields.io/github/downloads/miyako/4d-plugin-screen-capture/total)

A 4D plugin that adds two commands for capturing screenshots directly from 4D code, without shelling out to the OS or relying on third-party utilities. Both commands return a native 4D `Picture` that you can display, store in a field, paste to the pasteboard, or write to disk using 4D's standard picture commands.

| Command | Returns | Purpose |
|---|---|---|
| [`Capture screen`](#capture-screen) | Picture | Captures a monitor / the desktop |
| [`Capture window`](#capture-window) | Picture | Captures a single 4D window |

**Platforms:** Windows and macOS (Universal / Intel & Apple Silicon).

---

## Requirements & platform notes

Read this before using either command — the two platforms implement capture differently, and it affects what you get back.

- **Windows** uses the modern *Windows.Graphics.Capture* API (the same engine behind the Windows 10/11 built-in screen-recording tools). This requires **Windows 10 version 1803 or later**. The captured image is encoded as **PNG**.
- **macOS** uses Apple's `CGWindowListCreateImage` API. The captured image is encoded as **TIFF**. Starting with **macOS 10.15 Catalina**, macOS requires the host application (4D) to be granted **Screen Recording** permission under *System Settings → Privacy & Security → Screen Recording* — without it, captures of windows belonging to other applications will come back blank/black. Capturing 4D's own windows generally works regardless.
- Either way, the command simply returns a 4D `Picture` variable — your 4D code doesn't need to care whether the bytes underneath are PNG or TIFF.
- Both commands take **one mandatory Longint parameter** — there's no optional/omitted-parameter form.
- If a capture cannot be completed (invalid target, permission denied, or the OS never delivers a frame), the command does not raise an error — it simply doesn't return a usable picture. See [Error handling](#error-handling--troubleshooting) below for how to guard against this.

---

## Capture screen

**Capture screen ( monitor ) → Picture**

| Parameter | Type | Description |
|---|---|---|
| `monitor` | Longint | Index of the monitor to capture |
| Result | Picture | The captured screenshot |

### Description

`Capture screen` grabs a screenshot of a physical monitor and returns it as a `Picture`.

- **On Windows**, `monitor` is a **1-based index** into the set of displays currently connected to the machine, in system enumeration order (1 = first monitor, 2 = second monitor, and so on). If you pass an index that doesn't correspond to any connected monitor (`0`, a negative number, or a number higher than the monitor count), the command falls back to capturing the **primary monitor** rather than failing.
- **On macOS**, the `monitor` parameter is currently **ignored** — `Capture screen` always captures the entire desktop across all connected displays as a single combined image, regardless of what you pass in. Keep this in mind if you're writing cross-platform code: on Windows you get one monitor, on macOS you always get everything.

### Example

From the plugin's own test method (`TEST_desktop.4dm`) — capture the (first) screen and put it on the system pasteboard:

```4d
 //%attributes = {}
$image:=Capture screen(1)

SET PICTURE TO PASTEBOARD:C521($image)
```

### More usage

Capture a specific secondary monitor on Windows (index 2), and display it in a form's picture variable:

```4d
 // Capture the second monitor and show it in a form picture field
vPicture:=Capture screen(2)
```

Loop through several monitor indexes and store each as a separate picture (Windows only — remember macOS ignores the index and will just return the same combined desktop image every time):

```4d
 ARRAY PICTURE($screens;0)
For ($i;1;4)  // adjust to however many monitors you expect
	$pic:=Capture screen($i)
	APPEND TO ARRAY($screens;$pic)
End for
```

---

## Capture window

**Capture window ( window ) → Picture**

| Parameter | Type | Description |
|---|---|---|
| `window` | Longint | Reference number of the 4D window to capture |
| Result | Picture | The captured screenshot of that window |

### Description

`Capture window` grabs a screenshot of a single 4D window (not an arbitrary OS window belonging to another application) and returns it as a `Picture`. The `window` parameter is a standard 4D **window reference number**, exactly like the values returned by commands such as `Frontmost window`, or the window numbers you manage yourself when opening windows with `Open window`/`New window`.

- **On Windows**, the plugin resolves the window reference to a native `HWND` internally and captures its current on-screen content, including content that would normally be excluded from a plain screen scrape (the capture is composited by the OS, so it reflects what's actually on screen at the time of the call).
- **On macOS**, the plugin resolves the window reference to the window's `CGWindowID` and captures just that window's content, cropped to its bounds.
- If the window reference doesn't resolve to a currently-open window, the command does not return a picture.

### Example

From the plugin's own test method (`TEST_window.4dm`) — capture whatever is the frontmost window and put it on the pasteboard:

```4d
 //%attributes = {}
$image:=Capture window(Frontmost window:C447)

SET PICTURE TO PASTEBOARD:C521($image)
```

### More usage

Capture a specific window you opened yourself, using its stored window reference:

```4d
 $winRef:=Open window(100;100;800;600)
 // ... draw/populate the window's content here ...

$shot:=Capture window($winRef)

CLOSE WINDOW($winRef)
```

Capture the current window and store it in a record's picture field:

```4d
$image:=Capture window(Current window)

[Screenshots]Image:=$image
SAVE RECORD([Screenshots])
```

---

## Error handling & troubleshooting

Neither command reports failure with a 4D error signal — a failed or empty capture simply results in the target variable not being (usefully) set. Practical guidance:

- **Always initialize the receiving variable before the call** (e.g. `$image:=New picture` or simply rely on 4D's default empty-picture value for an uninitialized `Picture` variable) so you have something predictable to test against afterward.
- If you need to confirm a capture actually produced content, compare the resulting picture's size/dimensions against an empty picture, or simply check whether subsequent operations on it (pasting, displaying, saving) behave as expected — the exact inspection command you use will depend on your 4D version, so check your Language Reference for the picture-inspection commands available to you.
- **On macOS**, an all-black or blank result from `Capture window` (for windows outside your own 4D windows) almost always means Screen Recording permission hasn't been granted to the 4D application/runtime — check *System Settings → Privacy & Security → Screen Recording*.
- **On Windows**, if a capture never returns, verify you're on Windows 10 version 1803 or later; the underlying Graphics Capture API isn't available on older builds.
- If you pass an out-of-range monitor index to `Capture screen` on Windows, you'll silently get the **primary** monitor rather than an error — don't rely on a specific index existing without first confirming your target machine's monitor layout.

---

## Quick reference

```4d
 // Capture the primary/first monitor
$screen:=Capture screen(1)

 // Capture the frontmost window
$window:=Capture window(Frontmost window:C447)

 // Either result is a normal 4D Picture:
SET PICTURE TO PASTEBOARD:C521($screen)
FORM.myPicture:=$window
```
