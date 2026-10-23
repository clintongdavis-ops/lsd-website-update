# AG Hair automated accessibility baseline

Observed 2026-10-23 with axe-core 4.14.0 on Chromium 154.0.8037.57. Scope: unauthenticated
desktop and emulated Pixel 7, using the same read-only browser restrictions as the category
inspector. Current-run receipt: `evidence/accessibility-baseline.json`.

Both profiles completed. The audit command returned **1**, meaning findings require review.
It did not pass full accessibility or commerce acceptance. Rules were selected by tags
`wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa`. Missing H1 is a separate inspector
observation, not a claim that an axe WCAG rule failed.

| Profile | Violated rule IDs and affected-node counts | Incomplete rules needing manual review |
|---|---|---|
| Desktop | `button-name` 1 (critical); `color-contrast` 17; `list` 1; `listitem` 24; `target-size` 8 | `aria-hidden-focus` 3; `aria-prohibited-attr` 8; `color-contrast` 2 |
| Mobile | `aria-prohibited-attr` 1; `color-contrast` 17; `select-name` 1 (critical); `target-size` 9 | `aria-prohibited-attr` 8; `color-contrast` 4 |

Desktop has five violated-rule groups and three incomplete groups; mobile has four and
two. These are not counts of unique defects. A rule can have different violated and
incomplete nodes, and one element may appear under several rules. No conformance score
or percentage is inferred from the passed/inapplicable rule counts.

## Work's pilot remediation order

1. Inspect the unnamed desktop button at `#label-for-id_-805` and the mobile sort select
   `#sortBy`; give each a correct programmatic name through supported native settings.
2. Provide a meaningful category H1 alongside the brand imagery. Both baseline profiles
   currently expose only the `Filter by` heading among H1–H3.
3. Review the reported product-ribbon/text contrast and small navigation/control targets.
   Use the selectors in the evidence to locate them; generated CSS classes/IDs may change.
4. Inspect native filter-list markup and the mobile ARIA finding (`#comp-lii53x7i`). Prefer
   supported native component configuration/update or a Wix support escalation over a
   custom replacement of commerce functionality.
5. Resolve incomplete-rule groups manually, then repeat on the actual unpublished pilot,
   including keyboard, focus visibility, touch, zoom and screen-reader checks.

Non-GET/HEAD HTTP, WebSockets and service workers were blocked. Some asset/telemetry hosts
failed, and that can affect rendered-state findings. The report retains those limitations.
The summaries intentionally omit raw HTML and private data. They retain rule/help URLs,
impact, selectors and counts; exact contrast values and ARIA check details require a
focused browser inspection. No production page or component was modified.

Repeat with `npm run audit:accessibility`, using authorized normal NSS database access
when the filesystem sandbox restricts Chromium. Each run replaces the canonical report
at startup, records completion/error state and uses its own screenshot directory.
