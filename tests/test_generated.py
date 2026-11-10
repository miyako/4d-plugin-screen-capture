"""The final publication exemption is smaller than the bundle or build roots."""

import unittest

from helper_support import source
import native


class GeneratedOutputTests(unittest.TestCase):
    def test_exact_native_files_and_controlled_directory_descendants(self):
        expected = (
            "test/Plugins/screen-capture.bundle/Contents/MacOS/screen-capture",
            "test/Plugins/screen-capture.bundle/Contents/Info.plist",
            "test/Plugins/screen-capture.bundle/Contents/Resources/English.lproj/InfoPlist.strings",
            "test/Plugins/screen-capture.bundle/Contents/_CodeSignature/CodeResources",
            "test/Plugins/screen-capture.bundle/Contents/Windows64/screen-capture.4DX",
            "test/Plugins/screen-capture.bundle/Contents/Resources/constants.xlf",
            "test/Plugins/screen-capture.bundle/Contents/Resources/manifest.json",
            "build/XCBuildData/build.db",
            "build/XCBuildData/build.db-wal",
            "build/XCBuildData/build.db-shm",
            "build/XCBuildData/0123456789abcdef0123456789abcdef.xcbuilddata/build-request.json",
            "build/screen-capture.build/Objects-normal/arm64/main.o",
            "build/Default/screen-capture.build/build.db",
            "test/Plugins/screen-capture.build/Objects/file.o",
            "test/Plugins/Default/screen-capture.build/Objects/file.o",
        )
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(native.generated(path))

    def test_every_resource_source_or_unproven_output_stays_protected(self):
        excluded = (
            "test/Plugins/screen-capture.bundle/Contents/MacOS/runtime.dylib",
            "test/Plugins/screen-capture.bundle/Contents/QuickLook/Thumbnail.png",
            "test/Plugins/Default/screen-capture.bundle/Contents/Info.plist",
            "test/Plugins/Default/keep", "build/XCBuildData-evil/build.db",
            "build/unexpected-source.cpp",
            "build/XCBuildData/unexpected-source.cpp",
            "build/XCBuildData/build.db-evil",
            "build/XCBuildData/evil.xcbuilddata/build-request.json",
            "build/screen-capture.build-evil/injected.cpp",
            "test/Plugins/screen-capture.bundle/Contents/_CodeSignature-evil/file",
            "test/Plugins/screen-capture.bundle/Contents/Info.plist.backup",
            *map(str, source.SOURCE_PATHS),
        )
        for path in excluded:
            with self.subTest(path=path):
                self.assertFalse(native.generated(path))
