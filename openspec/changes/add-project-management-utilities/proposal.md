# Add Project Management Utilities

## Why

The NTT Authentication Server project needs developer-friendly utilities to streamline common development tasks and project management. Currently, developers must manually handle dependency installation, requirements management, environment setup, and other routine tasks.

This change introduces a lightweight project management system that:
1. Simplifies dependency management and requirements.txt updates
2. Provides easy project setup and configuration management
3. Automates common development tasks without external dependencies
4. Ensures consistent development environment across team members

The utilities will use only Python built-in libraries to avoid bootstrapping issues and ensure they work immediately after project clone.

## What

This change introduces project management utilities consisting of:

### help.py - Simplified Project Helper
A minimal command-line interface with just four essential commands:
- **run**: Start the development server with auto-reload and proper configuration
- **test**: Execute test suite with selective project testing and intelligent caching
- **install**: Install packages and automatically update requirements.txt
- **build**: Create distribution packages, upload to repositories, and deploy to GitHub

### config/ Directory - Configuration Management
- Environment-specific configuration templates
- Development, testing, and production config presets
- Database connection configuration helpers
- Secret key generation utilities
- Deployment configuration management
- CI/CD configuration templates

### Intelligent Caching System
- Virtual environment detection and reuse across server and client library folders
- Dependency installation caching to avoid redundant package downloads
- Test result caching for unchanged code sections
- Build artifact caching for faster subsequent builds
- Smart cache invalidation based on file changes and dependency updates

All utilities will use only Python standard library (subprocess, os, json, etc.) to ensure zero-dependency operation.

## Success Criteria

- Developers can run `python help.py run` to start development server with auto-reload
- `python help.py test` executes complete test suite with coverage and quality checks
- `python help.py test --server` runs only server tests for faster feedback loops
- `python help.py test --python-client` or `--js-client` runs specific library tests
- `python help.py install <package>` installs packages and updates requirements.txt automatically
- `python help.py build` creates distribution packages and handles deployment to GitHub
- Intelligent caching dramatically reduces setup time for repeated operations
- Virtual environments are detected and reused across server/client library folders
- Simple, intuitive interface with just four essential commands plus selective flags
- Zero external dependencies required for project management utilities
- Each command handles all related sub-tasks automatically (database setup, migrations, etc.)

## Impact

**Positive:**
- Extremely simple interface - only 4 commands to learn
- Selective testing enables faster development cycles (test only what changed)
- Intelligent caching dramatically reduces repetitive setup time
- Significantly reduces onboarding time for new developers
- Standardizes development workflow with minimal cognitive overhead
- Eliminates manual requirements.txt maintenance errors
- Each command intelligently handles all related sub-tasks automatically
- Reduces context switching between different tools and commands

**Negative:**
- Adds small amount of project complexity with additional utility files
- Requires maintenance of custom tooling alongside main application
- May duplicate some functionality available in existing tools

## Alternatives Considered

1. **Use Existing Tools (Makefile, Poetry, pipenv)**
   - Pro: Battle-tested, feature-rich
   - Con: Additional dependencies, learning curve, less customization

2. **Shell Scripts**
   - Pro: Simple, no Python dependency
   - Con: Platform-specific, harder to maintain, less portable

3. **Task Runners (invoke, nox)**
   - Pro: Python-based, powerful
   - Con: External dependency, overkill for simple tasks

**Decision:** Custom Python utilities provide the right balance of simplicity, zero dependencies, and project-specific customization.