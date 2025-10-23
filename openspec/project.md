# Project Context

## Purpose
NTT Authentication Server is a comprehensive authentication solution that provides:
- Centralized user authentication and authorization for microservices
- JWT-based token management with refresh token support
- RESTful API for user management (register, login, profile updates)
- Support login from other thirdparty system like github, gmail, etc.
- Client libraries for Python and JavaScript/TypeScript to enable easy integration
- Secure password hashing and token validation
- Production-ready deployment with Docker and CI/CD pipeline

The goal is to create a reusable authentication service that other projects can easily integrate with, reducing the need to implement authentication from scratch in each service.

## Tech Stack
- **Backend Framework:** FastAPI (Python 3.9+)
- **Database:** MySQL (production), SQLite (development/testing)
- **ORM:** SQLAlchemy with Alembic migrations
- **Authentication:** JWT tokens with self implementation
- **Password Hashing:** bcrypt via passlib
- **Validation:** Pydantic v2 with email validation
- **API Documentation:** Auto-generated OpenAPI/Swagger docs
- **Client Libraries:** Python SDK, JavaScript/TypeScript SDK
- **Testing:** pytest, pytest-asyncio, httpx for API testing, and fastapi test client
- **Containerization:** Docker with multi-stage builds
- **CI/CD:** GitHub Actions, Jenkins flow
- **Code Quality:** Black, isort, flake8, mypy, pre-commit hooks

## Project Conventions

### Code Style
- **Python:** Follow PEP 8 with Black formatting (88 character line length)
- **Import Organization:** Use isort with Black profile
- **Type Hints:** Mandatory for all functions and methods (enforced by mypy)
- **Logging:** Use standard logging module with structured logs
- **Parameter:** One parameter per line for functions with multiple parameters, must have trailing comma, and type hints for each parameter
- **Naming Conventions:**
  - CamelCase for variables
  - UpperCamelCase for functions, methods, classes.
  - PascalCase for classes and Pydantic models
  - UPPER_CASE for constants
  - Kebab-case for API endpoints and file names
- **Documentation:** Docstrings required for all public functions and classes

### Architecture Patterns
- **Clean Architecture:** Separate layers for API routes, business logic, and data access
- **Dependency Injection:** Use FastAPI's dependency system for database sessions and auth
- **Repository Pattern:** Abstract database operations behind service classes
- **Schema Separation:** Distinct Pydantic models for requests, responses, and database operations
- **Error Handling:** Standardized HTTP exception handling with proper status codes
- **Configuration Management:** Environment-based settings using Pydantic Settings

### Testing Strategy
- **Unit Tests:** Test business logic in isolation using mocks
- **Integration Tests:** Test API endpoints with test database
- **End-to-End Tests:** Test complete workflows including client libraries
- **Test Database:** Use SQLite in-memory for fast test execution
- **Coverage Target:** Maintain >90% code coverage
- **Test Structure:** Mirror source code structure in tests directory
- **Fixtures:** Use pytest fixtures for common test data and database setup

### Git Workflow
- **Branching Strategy:** GitFlow with main/develop branches
- **Commit Messages:** Use conventional commits format (feat:, fix:, docs:, etc.)
- **Pull Requests:** Required for all changes to main/develop branches
- **Code Reviews:** All PRs require at least one approval
- **Pre-commit Hooks:** Run linting, formatting, and type checking before commits
- **Release Tags:** Use semantic versioning (v1.0.0, v1.1.0, etc.)

## Domain Context
- **Users:** Central entity with email as unique identifier
- **Authentication:** JWT access tokens (short-lived) + refresh tokens (long-lived)
- **Authorization:** Role-based access control with user and superuser roles
- **Token Security:** Tokens contain minimal user info and are stateless
- **Password Security:** Bcrypt hashing with configurable rounds
- **Session Management:** Refresh tokens can be revoked for security
- **Multi-tenancy:** Single instance serves multiple client applications

## Important Constraints
- **Security Requirements:** 
  - All passwords must be hashed with bcrypt
  - JWT tokens must have expiration times
  - Sensitive data should not be logged
- **Performance Requirements:**
  - Token validation must be < 100ms
  - Support for 1000+ concurrent users
- **Compliance:**
  - GDPR-compliant user data handling
  - Secure password storage requirements
- **Backward Compatibility:**
  - API versioning for breaking changes
  - Client library compatibility across versions

## External Dependencies
- **Database:** MySQL 8.0+ for production storage
- **Container Registry:** Docker Hub or private registry for image storage
- **CI/CD Platform:** GitHub Actions for automated testing and deployment
- **Monitoring:** Optional integration with logging and metrics systems
- **Load Balancer:** Support for horizontal scaling behind load balancers
- **TLS/SSL:** Requires HTTPS in production environments
