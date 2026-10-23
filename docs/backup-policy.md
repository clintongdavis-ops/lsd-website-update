# Web app GitHub backup requirement

Owner preference, recorded 2026-10-23: maintain a GitHub source backup for every web app.
Catalogue Lab is the immediate priority. This requirement does not authorize republishing
apps, changing catalogue data, or moving production storage.

## What a complete source backup includes

- The actual app source and assets, with its source/deployed revision recorded.
- Dependency manifests and lockfiles, schema migrations, non-secret build and hosting
  configuration, and any generated source necessary to rebuild.
- Recovery instructions describing toolchain, build/start commands, required binding names,
  external services and storage dependencies without credential values.
- A source-file manifest/hash receipt and a verified fetch of the pushed backup snapshot.

Preserve meaningful history and local changes. Inspect tracked files and history for
credentials, private business records and generated data before choosing what to push.
When history contains material that cannot be copied safely, preserve the original securely
and make a clearly identified sanitized source snapshot; do not silently rewrite the
original app history or delete files. A working directory copied into GitHub is not proof
that the currently deployed version has been captured.

Use private repositories for proprietary apps. Keep this public migration repository
limited to technical specifications, generic validation tools, synthetic fixtures and
public website observations. Do not create another empty repository and call it a backup.
An app backup is pending until the source is actually captured and verified.

Source backup and operational recovery are separate. Database contents, uploads and
runtime secret bindings need a separate approved secure backup/restore process. A successful
source fetch proves source preservation; a build proves rebuildability; only a supported
isolated restore test demonstrates recovery. Record those outcomes separately.
If required source assets contain embedded private records, preserve them securely and
document their restoration dependency. Do not silently omit required files, replace actual
app behavior with fixtures, or claim a sanitized snapshot rebuilds without those assets.

## Current Catalogue Lab source-access status

The owner identified the existing hosted Lab and Sites as its backend/source platform.
Related development-task history confirms an existing project; it does not provide a
current source export. The current cloud session exposes no callable Sites source tools
and cannot read the development project's filesystem on another machine.

Two plausible GitHub repositories inspected during discovery were empty; neither is a
verified copy of Catalogue Lab. No app code was reconstructed, no backup repository was
populated with partial frontend material, and no deployment was changed.

The task with source access must export the latest complete app source or push a verified,
sanitized source snapshot to a private GitHub repository. Detailed internal provenance and
the handoff are retained outside this public repository. Once source is available, inspect
the actual catalogue contracts before building any Wix V3 adapter.
