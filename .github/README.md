# Manual source and release workflows

`Bump version` and `Build` are independent manual workflows. Bump has one
required `patch`/`minor`/`major` choice (default `patch`); Build has no custom
inputs. Select the branch or tag using GitHub's built-in ref selector.
Neither workflow dispatches the other. There are no tag or push triggers.
Every checkout uses the immutable event SHA.

## Source authority

The intake is `6870666ef3c83a7240bace9d17f9d92438192d26`, with canonical
version **3.0.5**. The rename-follow Bump history initially preferred marketing
version (`2dc96e542e024be9a200b407017c3b4c9cfbdb0d`), but
`ce8a1e2b25df92397c22295b1021ac36f5e4d5c9` explicitly superseded that with
coordinated MARKETING_VERSION, CURRENT_PROJECT_VERSION and plist versions.
Its implementation accidentally updated only marketing version. This migration
aligns the six stale source CURRENT tokens from 3.0.3 to 3.0.5, without
incrementing the existing authority.

The six configurations are Development, Deployment and Default at project and
target levels in `screen-capture.xcodeproj/project.pbxproj`. `Info.plist` requires
CFBundleShortVersionString; its absent CFBundleVersion stays absent.
`English.lproj/InfoPlist.strings` is actually copied into the native bundle and
overrides display metadata, so its stale 3.0.2 display tokens are aligned and
co-bumped. Prebuilt destination metadata is not authority and remains untouched.
Known version references are retained; invalid, cyclic, duplicate, missing,
unresolved or drifting metadata aborts before any writes. Edits replace only
version token spans, preserving encodings, line endings, modes and other bytes.

## Bump safety

The committed executable `.github/hooks/pre-push` is mandatory before editing
and rechecked before pushing. Every check rejects symlinks and requires the
guard's raw bytes and executable Git mode to match its HEAD blob, including
after the final remote read. Bump compares the selected event SHA to the exact
remote branch, creates one nonempty source-only direct child with explicit
Actions bot identities and the co-author trailer, then checks Git's actual
old-SHA advertisement. There is exactly one nonforce branch update; followed
tags are disabled through both configuration and `--no-follow-tags`.
An advance, rewind, deletion or same-result race fails rather than retrying.
It never builds, tags, releases or dispatches anything.

## Build and publication safety

Build retains Windows Release x64 MSBuild followed by macOS Default universal
arm64+x86_64, deployment override 11.0, existing frameworks/static libraries,
resources and the `test/Plugins/screen-capture.bundle` package root. It does not
run 4D or add another runtime/dependency policy. Cleanup is selective and fatal
on errors; it does not delete entire bundles or unrelated Default siblings.
Built plist and the actual copied/compiled English localization are validated.
Signing is strictly verified; both notarization exit status and JSON Accepted
status are required, followed by stapling.
The existing custom Xcode credential phase runs only for Deployment; the selected
Default configuration leaves it inactive and unchanged. Disabling Xcode signing
alone does not suppress custom shell phases.

A constant repository-wide publication concurrency group has cancellation
disabled. This is serialization, not a FIFO guarantee. There is no new
default-branch-only restriction. Explicit GH_TOKEN authentication and early
availability checks precede native work. Final checks follow signing,
notarization and stapling. Source/configuration index entries and raw worktree
bytes must still match selected HEAD, independently; only exact generated
outputs and proven native intermediates may differ at the final gate.
Pre-existing ignored build databases fail the initial gate; freshly generated
XCBuildData is retained at the final gate, not reset to fake cleanliness.
Only the exact build database/WAL/SHM and 32-hex `.xcbuilddata` descendants are
allowed there. Every final packaged generated leaf, including executable and
signature, must remain nonempty, regular and nonsymlink. Copied resources and
downloaded/merged Windows bytes are rechecked. The unsigned pre-sign gate does
not require a signature that has not been generated yet.

Build inherits scoped `core.autocrlf=false` before every checkout without
changing global Git configuration. On Windows only, regular worktree executable
bits may differ when the raw blob is identical; selected/index modes, hidden
flags, symlinks and reparse points remain strict.
Both `git ls-files -v` and `-f` are checked: fsmonitor-valid can appear as `H`
to `-v` while only `-f` exposes its lowercase `h` marker.

Publication checks all release pages through the empty page, including drafts,
the exact API tag ref and exact Git advertisement. Reads fail closed. It then
uses separate create-only POSTs for the tag at selected SHA, a new public
release ID, and each asset. The original empty-body/no-generated-notes policy
is retained. Local assets are `screen-capture-X.Y.Z.zip` and `.dmg`; GitHub's
actual remote names remain `screen-capture-X.Y.Z.zip` and `.dmg`.
Existing tags/releases are never reused, updated, clobbered or deleted.
The intake already has a v3.0.5 release, so Build on this unchanged source
version deliberately refuses publication. Run Bump separately before a new
release; this migration itself does not consume a version.

**Manual recovery:** any failure after a POST may leave a tag, release or
assets, including a request whose successful response was lost. Inspect the
reported tag/release ID and retained uploads manually. No automatic rollback,
deletion or retry occurs; a same-SHA tag race also fails. Resolve partial state
deliberately before another Build attempt.

## Offline validation

Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`
and `actionlint` (requires PowerShell for native workflow regressions).
Tests use local bare Git origins and closed-PATH native/credential/API doubles,
never real signing, notarization, compilers or 4D. Original fixtures are pinned
to the immutable intake; live version expectations also work after a genuine
guarded Bump. Reference provenance is recorded in `tests/reference-pins.json`.
