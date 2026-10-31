# Chain reorganization handling (proposed)

A block observed by an RPC endpoint is not necessarily final. A future ChainWatch history or event watcher must account for reorganizations rather than treating the first observation as permanent truth.

## Stored block identity

Keep chain ID, block height, and block hash together. Height alone is not a stable block identity because competing branches can contain different blocks at the same height. Any cached transaction or event derived from a block should retain the block hash that produced it.

## Confirmation policy

Expose confirmation depth as an explicit policy and show the observed head height used to calculate it. Do not label a block final unless the selected network and policy provide a defensible finality signal. For networks without deterministic finality, use terms such as confirmed or sufficiently deep and document the residual reorganization risk.

## Detecting and handling a reorganization

When a previously observed height returns a different block hash:
1. Find the last common ancestor using bounded RPC requests.
2. Mark observations on the displaced branch as orphaned or reverted; do not silently delete the history.
3. Roll back derived cursors and cached data to the ancestor.
4. Re-read the replacement branch in bounded batches.
5. Emit correction events with references to the original observations so consumers can reconcile their state.

If the common ancestor cannot be found within the configured bound, stop advancing the cursor and report that reconciliation is incomplete. Do not continue as though the chain were consistent.

## Tests

Use synthetic block fixtures with a shared ancestor and two competing branches. Cover a reorganization before and after the configured confirmation threshold, duplicate notifications, RPC timeouts during ancestor lookup, and restart from a persisted cursor. Tests must use a fake RPC transport and must never submit transactions.