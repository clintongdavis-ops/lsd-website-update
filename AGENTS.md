# Project instructions

Follow the engineering boundaries in README.md. Keep existing Wix commerce and Catalogue
Lab functionality and identifiers intact. Use native Wix capabilities where adequate.

The owner wants a GitHub backup for **every web app**, including Catalogue Lab. Preserve
this requirement for future work. Use a private repository for proprietary app source;
do not put it in this public migration repository. Back up complete source, lockfiles,
schema migrations, non-secret build/hosting configuration and recovery instructions.
Exclude credentials, private business registers, customer data and catalogue/database
exports. Data backups require separate secure storage; a source backup does not include
live data or runtime credentials. Verify the pushed snapshot can be fetched and its source
manifest reproduced before calling the source backup complete. Track restoration tests
separately. If source access is unavailable, report the backup as pending.

Backups do not authorize deployment or production changes. Preserve the existing app and
use its actual source rather than reconstructing it from a published frontend or chat logs.
