/* --------------------------------------------------------------------------------
 #
 #	4DPlugin-screen-capture.h
 #	source generated by 4D Plugin Wizard
 #	Project : screen-capture
 #	author : miyako
 #	2020/08/13
 #  
 # --------------------------------------------------------------------------------*/

#ifndef PLUGIN_SCREEN_CAPTURE_H
#define PLUGIN_SCREEN_CAPTURE_H

#include "4DPluginAPI.h"

#if VERSIONMAC
#import <Cocoa/Cocoa.h>
#else
#include <windows.h>
#include <vector>
#endif

#pragma mark -

void Capture_screen(PA_PluginParameters params);
void Capture_window(PA_PluginParameters params);

#endif /* PLUGIN_SCREEN_CAPTURE_H */