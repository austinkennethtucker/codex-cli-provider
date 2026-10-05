# Codex project environment review

## Applied

- `.codex/config.toml` uses project-scoped, approval-gated workspace access with
  agent shell network access disabled.
- `.codex/environments/environment.toml` replaces the former no-op setup with a
  repository-local Python virtual environment and exposes the checks documented
  by the repository and CI.

## Evidence

- `requirements.txt` is the repository's pinned pip dependency input.
- `AGENTS.md`, `README.md`, and `.github/workflows/ci.yml` define the unit,
  hygiene, Compose-render, and Compose-security checks.
- The repository is a single Python service; no nested repositories, package
  workspaces, database migrations, or private package registries were detected.

## Boundaries and assumptions

- Initial setup needs Python 3 and outbound access to the public Python package
  index. Agent shell network access remains disabled by default and should be
  enabled deliberately only for dependency installation or other reviewed work.
- Docker is required only for the Compose actions and image build; setup does
  not start containers, services, databases, or deployments.
- `.env` and `data/` are intentionally not copied or generated. They can contain
  the wrapper secret and a live container-scoped Codex login.
- The setup and actions use repository-relative paths and assume a POSIX shell.
  Windows users should configure an app-generated platform-specific override.
- No hooks, rules, MCP servers, additional writable roots, or user-level Codex
  settings are introduced.

## Validation

The project setup validator passed with no warnings. The setup command completed
successfully on macOS using Python 3.14, and the unit, hygiene, Compose-render,
and Compose-security actions passed. CI remains the authoritative Python 3.12
and Linux verification surface.

## Next safe action

Review this configuration in the Codex app and confirm the generated environment
remains selected for new worktrees.
