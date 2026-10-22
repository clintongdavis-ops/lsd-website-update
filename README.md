# Le Salon Dieppe website modernization

Engineering workspace for the Wix Studio migration. The existing Wix business backend remains the commerce system of record; the authoritative catalogue remains in its existing catalogue workflow.

## Engineering boundaries

- Preserve product and variant identities, inventory, prices, SKUs, barcodes and image associations.
- Separate Studio design work, Category Page migration and Catalog V3 assessment.
- Do not publish, change paid plans, migrate irreversibly, delete production data, import catalogues or apply redirects without owner approval.
- Prefer native Wix Stores functionality before CMS or custom commerce code.
- Never commit credentials, customer data, catalogue exports or private business registers to this public repository.

## Work coordination

Work owns editor and browser configuration. Codex owns code review, API compatibility, read-only preservation comparisons and technical QA. Claim a task and component before editing; avoid simultaneous changes. Each task must record owner, status, dependencies, deliverable and acceptance criteria.

## Acceptance gates

1. Confirm a real unpublished Studio branch and app parity in the editor.
2. Capture the existing page, integration and code inventories.
3. Verify the actual native category functionality available to this site.
4. Build and approve one category pilot before repeating work.
5. Test responsive navigation, product variants, cart, booking links, SEO and languages.
6. Prepare an explicit cutover and recovery plan before owner review.

No deployment pipeline or production mutation is configured by this README.

## Technical toolkit and current evidence

The read-only engineering foundation is on the `engineering/wix-migration-foundation` branch.
No production writer, deployment, catalogue migrator, order or payment automation is included.

- [Setup and toolkit commands](docs/toolkit.md)
- [Architecture and category strategy](docs/architecture.md)
- [Verified official Wix findings](docs/official-findings.md)
- [Catalogue preservation contract](docs/catalogue-contract.md)
- [Technical task register and Work handoff](docs/task-register.md)
- [QA and SEO plan](docs/qa-plan.md)
- [Validation results](evidence/validation.md)

Only public sitemap/HTTP observations and synthetic fixtures are committed.
Private source exports, normalized catalogue snapshots and runtime results belong in ignored
`artifacts/` or an approved secure store, subject to the engineering boundaries above.
