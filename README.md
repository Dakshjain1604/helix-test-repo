# helix-test-repo

A sandbox repository used to test the [Helix CI/CD Agent](https://github.com/Dakshjain1604/HelixCICD).

Helix watches this repo for workflow failures and automatically diagnoses and repairs them.

## Workflow

- Every push to a non-protected branch triggers the `CI` workflow
- If the workflow fails, Helix picks it up via webhook and attempts an automated fix
- Protected branches (`main`, `master`) are never modified by Helix
