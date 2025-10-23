# Project Management Tools Specification

## Overview

This specification details the implementation of a simple, zero-dependency project management system consisting of a `help.py` script in the source folder and a configuration folder `config/` for easy project management. The system provides four essential commands: `run`, `test`, `install`, and `build`.

## Core Requirements

### REQ-1: Zero Dependency Implementation
- **Description**: The help.py system shall use only Python standard library modules
- **Implementation**: No external dependencies beyond Python 3.9+ standard library
- **Scenarios**:
  - Given a fresh Python installation, when help.py is executed, then it runs without requiring pip install
  - Given an environment without internet access, when help.py is used, then all functions work normally
  - Given a system with only Python standard library, when any command is executed, then no import errors occur

### REQ-2: Simplified Command Interface
- **Description**: The help.py script shall provide exactly four commands: run, test, install, build
- **Implementation**: Command-line interface with `python help.py <command> [options]`
- **Scenarios**:
  - Given the command `python help.py run`, when executed, then the main application starts
  - Given the command `python help.py test`, when executed, then the test suite runs
  - Given the command `python help.py install`, when executed, then dependencies are installed
  - Given the command `python help.py build`, when executed, then the project is built for distribution
  - Given an invalid command, when help.py is executed, then usage help is displayed
  - Given no command, when help.py is executed, then available commands are listed

### REQ-3: Configuration Management
- **Description**: The system shall use a config/ folder for storing configuration files
- **Implementation**: Structured configuration directory with environment-specific files
- **Scenarios**:
  - Given a new project, when help.py runs for the first time, then config/ directory is created
  - Given missing config files, when help.py is executed, then default configurations are generated
  - Given environment variables, when configuration is loaded, then environment overrides take precedence
  - Given invalid configuration, when help.py is executed, then clear error messages are displayed

### REQ-4: Intelligent Caching System
- **Description**: The system shall implement intelligent caching for dependencies, build artifacts, and test results
- **Implementation**: Hash-based caching with automatic invalidation
- **Scenarios**:
  - Given unchanged dependencies, when install command runs, then cached packages are used
  - Given modified source files, when test command runs, then cache is invalidated and tests re-run
  - Given unchanged code, when test command runs, then cached test results are displayed
  - Given disk space constraints, when cache grows large, then oldest entries are automatically cleaned
  - Given corrupted cache, when any command runs, then cache is rebuilt transparently
  - Given cache hit, when build command runs, then build time is significantly reduced
  - Given dependency changes, when install runs, then only modified dependencies are processed

### REQ-5: Selective Testing Capabilities
- **Description**: The test command shall support flags for running specific test suites
- **Implementation**: Command-line flags: --server, --python-client, --js-client
- **Scenarios**:
  - Given the command `python help.py test --server`, when executed, then only server tests run
  - Given the command `python help.py test --python-client`, when executed, then only Python client tests run  
  - Given the command `python help.py test --js-client`, when executed, then only JavaScript client tests run
  - Given multiple flags, when test command runs, then specified test suites run in sequence
  - Given no flags, when test command runs, then all test suites execute
  - Given invalid flags, when test command runs, then error message and valid flags are shown
  - Given cached results, when selective tests run, then only specified suites are checked for cache validity

### REQ-6: Cross-Platform Compatibility
- **Description**: The system shall work consistently across Windows, macOS, and Linux
- **Implementation**: Platform-agnostic path handling and command execution
- **Scenarios**:
  - Given Windows environment, when any command runs, then paths use correct separators
  - Given macOS environment, when commands execute, then file permissions are handled correctly  
  - Given Linux environment, when help.py runs, then all features work as expected
  - Given different Python installations, when commands execute, then correct interpreter is used
  - Given various terminal emulators, when commands run, then output displays correctly

### REQ-7: Development Server Management
- **Description**: The run command shall start and manage the FastAPI development server
- **Implementation**: Server process management with graceful startup/shutdown
- **Scenarios**:
  - Given the run command, when executed, then FastAPI server starts on configured port
  - Given server already running, when run command is executed, then existing server is detected
  - Given invalid configuration, when run command is executed, then clear error message is shown
  - Given Ctrl+C signal, when server is running, then graceful shutdown occurs
  - Given auto-reload enabled, when source files change, then server restarts automatically
  - Given environment variables, when server starts, then configuration is properly loaded

### REQ-8: Dependency Installation Management
- **Description**: The install command shall manage Python and Node.js dependencies efficiently
- **Implementation**: Multi-language package management with caching
- **Scenarios**:
  - Given requirements.txt changes, when install runs, then Python dependencies are updated
  - Given package.json changes, when install runs, then Node.js dependencies are updated
  - Given no changes, when install runs, then cached dependencies are validated
  - Given network issues, when install runs, then cached packages are used if available
  - Given version conflicts, when install runs, then clear resolution guidance is provided
  - Given virtual environment, when install runs, then packages are installed in correct environment

### REQ-9: Build Artifact Management
- **Description**: The build command shall create distribution packages for all project components
- **Implementation**: Multi-format build system with caching and validation
- **Scenarios**:
  - Given source changes, when build runs, then server package is created
  - Given client library changes, when build runs, then Python and JavaScript packages are built
  - Given no changes, when build runs, then cached artifacts are validated and reused
  - Given build errors, when build runs, then detailed error messages are provided
  - Given successful build, when artifacts are created, then version information is embedded
  - Given build command with --clean flag, when executed, then cache is cleared before building

### REQ-10: Configuration File Structure
- **Description**: The config/ directory shall contain structured configuration files for different environments
- **Implementation**: YAML-based configuration with environment inheritance
- **Scenarios**:
  - Given config/default.yaml, when loaded, then base configuration is applied
  - Given config/development.yaml, when in dev mode, then dev settings override defaults
  - Given config/production.yaml, when in prod mode, then prod settings override defaults
  - Given config/test.yaml, when running tests, then test settings override defaults
  - Given environment variables, when configuration loads, then env vars take highest precedence
  - Given missing config files, when help.py runs, then default configurations are auto-generated

### REQ-11: Logging and Output Management
- **Description**: The system shall provide clear, structured output and logging
- **Implementation**: Configurable logging with different verbosity levels
- **Scenarios**:
  - Given normal operation, when commands run, then progress is clearly indicated
  - Given --verbose flag, when commands execute, then detailed information is shown
  - Given --quiet flag, when commands execute, then minimal output is produced
  - Given errors, when commands fail, then specific error messages and solutions are provided
  - Given long-running operations, when commands execute, then progress indicators are shown
  - Given log files, when enabled, then structured logs are written to config/logs/

### REQ-12: Cache Management and Cleanup
- **Description**: The system shall efficiently manage cache storage and provide cleanup utilities
- **Implementation**: Automatic cache management with manual cleanup options
- **Scenarios**:
  - Given cache size limits, when cache grows large, then oldest entries are automatically removed
  - Given --clear-cache flag, when any command runs, then all caches are cleared
  - Given corrupted cache entries, when detected, then entries are automatically invalidated
  - Given disk space warnings, when cache operations occur, then cleanup is triggered
  - Given cache statistics request, when --cache-info flag is used, then cache usage is displayed
  - Given cache validation, when startup occurs, then integrity checks are performed

### REQ-13: Virtual Environment Detection and Management
- **Description**: The system shall automatically detect and work with virtual environments
- **Implementation**: Environment detection with automatic activation and management
- **Scenarios**:
  - Given virtual environment active, when commands run, then correct Python interpreter is used
  - Given no virtual environment, when install runs, then warning about system installation is shown
  - Given multiple environments, when commands execute, then active environment is correctly identified
  - Given conda environment, when commands run, then conda-specific paths are used
  - Given pipenv environment, when commands run, then pipenv commands are used appropriately
  - Given venv environment, when commands run, then venv activation is handled correctly

### REQ-14: Help and Documentation System
- **Description**: The system shall provide comprehensive help and usage information
- **Implementation**: Built-in help system with command-specific documentation
- **Scenarios**:
  - Given --help flag, when used with any command, then detailed usage information is shown
  - Given invalid arguments, when commands are executed, then usage help is automatically displayed
  - Given help.py without arguments, when executed, then overview and available commands are shown
  - Given command examples request, when --examples flag is used, then practical examples are provided
  - Given version request, when --version flag is used, then version information is displayed
  - Given configuration help, when requested, then configuration options are documented

### REQ-15: Error Handling and Recovery
- **Description**: The system shall handle errors gracefully and provide recovery suggestions
- **Implementation**: Comprehensive error handling with actionable recovery guidance
- **Scenarios**:
  - Given network connectivity issues, when commands fail, then offline alternatives are suggested
  - Given permission errors, when file operations fail, then permission fix instructions are provided
  - Given missing dependencies, when commands fail, then installation instructions are shown
  - Given configuration errors, when startup fails, then specific configuration fixes are suggested
  - Given process conflicts, when server start fails, then port conflict resolution is provided
  - Given recovery from errors, when retry occurs, then previous state is properly restored

### REQ-16: Performance Monitoring and Optimization
- **Description**: The system shall monitor performance and optimize operations automatically
- **Implementation**: Performance tracking with automatic optimization suggestions
- **Scenarios**:
  - Given slow operations, when commands execute, then performance warnings are displayed
  - Given cache hit/miss statistics, when operations complete, then cache efficiency is reported
  - Given resource usage monitoring, when high usage detected, then optimization suggestions are provided
  - Given timing information request, when --timing flag is used, then detailed timing is shown
  - Given performance degradation, when detected, then cache cleanup is automatically triggered
  - Given benchmark mode, when --benchmark flag is used, then performance metrics are collected

### REQ-17: Integration with Development Workflow
- **Description**: The system shall integrate seamlessly with common development workflows and tools
- **Implementation**: IDE integration, Git hooks, and CI/CD pipeline support
- **Scenarios**:
  - Given Git repository, when help.py is used, then Git status and branch information is considered
  - Given pre-commit hooks, when installed, then help.py commands can be used as hooks
  - Given CI/CD pipeline, when help.py is used, then appropriate exit codes and output formats are provided
  - Given IDE integration, when commands are executed, then output is IDE-friendly
  - Given Docker environment, when commands run, then containerized execution is properly handled
  - Given development vs production detection, when commands execute, then appropriate modes are used

## Implementation Guidelines

### File Structure
```
/
├── help.py              # Main script with four commands
└── config/              # Configuration directory
    ├── default.yaml     # Default configuration
    ├── development.yaml # Development overrides
    ├── production.yaml  # Production overrides
    ├── test.yaml       # Test environment settings
    └── cache/          # Cache storage directory
        ├── deps/       # Dependency cache
        ├── builds/     # Build artifact cache
        └── tests/      # Test result cache
```

### Command Specifications

#### Run Command
- **Usage**: `python help.py run [--port PORT] [--reload] [--env ENV]`
- **Function**: Start the FastAPI development server
- **Options**:
  - `--port`: Specify server port (default from config)
  - `--reload`: Enable auto-reload on file changes
  - `--env`: Set environment (development/production)

#### Test Command  
- **Usage**: `python help.py test [--server] [--python-client] [--js-client] [--verbose] [--coverage]`
- **Function**: Run test suites with selective execution
- **Options**:
  - `--server`: Run only server tests
  - `--python-client`: Run only Python client tests
  - `--js-client`: Run only JavaScript client tests
  - `--verbose`: Show detailed test output
  - `--coverage`: Generate coverage reports

#### Install Command
- **Usage**: `python help.py install [--dev] [--force] [--cache-only]`
- **Function**: Install project dependencies efficiently
- **Options**:
  - `--dev`: Include development dependencies
  - `--force`: Force reinstallation ignoring cache
  - `--cache-only`: Use only cached packages

#### Build Command
- **Usage**: `python help.py build [--clean] [--target TARGET] [--version VERSION]`
- **Function**: Build distribution packages
- **Options**:
  - `--clean`: Clear cache before building
  - `--target`: Specify build target (server/python-client/js-client/all)
  - `--version`: Set build version

### Cache Strategy

#### Dependency Cache
- **Location**: `config/cache/deps/`
- **Key**: Hash of requirements.txt and package.json
- **Invalidation**: File modification time and content hash changes
- **Cleanup**: LRU eviction when cache size exceeds 1GB

#### Build Cache
- **Location**: `config/cache/builds/`
- **Key**: Hash of source files and build configuration
- **Invalidation**: Source file changes and build config modifications
- **Cleanup**: Remove builds older than 30 days

#### Test Cache
- **Location**: `config/cache/tests/`
- **Key**: Hash of test files and source dependencies
- **Invalidation**: Test file changes and related source modifications
- **Cleanup**: Keep last 10 test runs per test suite

### Configuration Schema

#### Default Configuration
```yaml
server:
  host: "0.0.0.0"
  port: 8000
  reload: true
  
database:
  url: "sqlite:///./test.db"
  echo: false
  
testing:
  parallel: true
  timeout: 300
  coverage_threshold: 80
  
build:
  target_dir: "dist"
  version_from_git: true
  
cache:
  enabled: true
  max_size_gb: 1
  ttl_days: 30
```

## Success Criteria

1. **Simplicity**: Four commands handle all development tasks
2. **Performance**: Caching reduces operation time by 60%+
3. **Reliability**: Zero-dependency operation in any Python 3.9+ environment
4. **Usability**: Clear error messages and helpful guidance
5. **Flexibility**: Selective testing and configurable behavior
6. **Maintainability**: Self-documenting code with comprehensive help system

## Testing Strategy

### Unit Tests
- Test each command independently
- Mock file system operations for cache testing
- Validate configuration loading and merging
- Test error handling and recovery scenarios

### Integration Tests  
- End-to-end command execution
- Cache invalidation and cleanup
- Cross-platform compatibility verification
- Performance benchmarking

### User Acceptance Tests
- Developer workflow simulation
- CI/CD pipeline integration testing
- Documentation accuracy verification
- Error message clarity assessment