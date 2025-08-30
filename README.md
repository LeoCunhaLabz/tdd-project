# Store API - Test-Driven Development Project

A comprehensive RESTful API for product management built with FastAPI and MongoDB, developed using Test-Driven Development (TDD) methodology to demonstrate modern Python software engineering practices.

## 📋 Project Overview

This project serves as a practical implementation of Test-Driven Development (TDD) principles, showcasing how to build robust, maintainable, and thoroughly tested applications. The Store API provides a foundation for product management systems with modern asynchronous architecture.

### Key Features & Learning Objectives
- **TDD Implementation**: Red-Green-Refactor cycle with comprehensive test coverage
- **Clean Architecture**: Clear separation of concerns across layers
- **Async Programming**: Full async/await implementation with FastAPI and Motor
- **Type Safety**: Comprehensive type hints with Pydantic v2 models
- **Modern Tooling**: Poetry, pytest, pre-commit hooks, and Docker integration

## 🛠️ Technology Stack

**Core Technologies:**
- **Python 3.12+** - Modern Python with enhanced type system
- **FastAPI** - High-performance async web framework with automatic API documentation
- **MongoDB** - Document-based NoSQL database
- **Motor** - Async MongoDB driver for Python
- **Pydantic v2** - Data validation and serialization with type hints

**Development Tools:**
- **Poetry** - Dependency management and packaging
- **Pytest + pytest-asyncio** - Advanced testing framework with async support
- **Pre-commit** - Git hooks for code quality enforcement
- **Docker Compose** - Container orchestration for development

## 🏗️ Project Architecture

The project follows Clean Architecture principles with clear separation of concerns:

```
store/                           # Main application package
├── main.py                      # FastAPI application entry point
├── core/config.py               # Environment-based settings
├── db/mongo.py                  # MongoDB client and connection management
├── schemas/                     # Data models and validation
│   ├── base.py                  # Base schema with common fields (ID, timestamps)
│   └── product.py               # Product-specific schemas (Input/Output models)
└── usecases/product.py          # Product business operations and data access

tests/                           # Comprehensive test suite
├── conftest.py                  # Pytest configuration and shared fixtures
├── factories.py                 # Test data factories for consistent test data
├── schemas/test_product.py      # Product schema validation tests
└── usecases/test_product.py     # Product usecase integration tests
```

**Architecture Layers:**
1. **Presentation** (`main.py`): FastAPI application and route definitions
2. **Business Logic** (`usecases/`): Core business operations and rules
3. **Data Access** (`db/`): Database connections and abstractions
4. **Domain** (`schemas/`): Entity definitions and data validation
5. **Configuration** (`core/`): Application settings and environment management

## 🚀 Product Management Features

### Core Operations
- **CRUD Operations**: Create, read, update, and delete products
- **Data Validation**: Automatic input validation with detailed error messages
- **Audit Trail**: Automatic timestamp tracking (created_at, updated_at)
- **Unique Identification**: UUID4 generation for globally unique product IDs

### Product Data Model
```python
{
    "id": "550e8400-e29b-41d4-a716-446655440000",  # UUID4 - Auto-generated
    "name": "iPhone 14 Pro Max",                    # String - Required
    "quantity": 10,                                 # Integer - Stock quantity  
    "price": 8500.00,                              # Float - Product price
    "status": true,                                # Boolean - Active/Inactive
    "created_at": "2025-08-29T10:30:00Z",          # DateTime - UTC timestamp
    "updated_at": "2025-08-29T10:30:00Z"           # DateTime - UTC timestamp
}
```

### Technical Features
- **Async Operations**: Non-blocking I/O for high concurrency
- **Type Safety**: Full type hints for development-time error detection
- **Schema Validation**: Automatic request/response validation with Pydantic
- **Error Handling**: Comprehensive error responses with detailed messages
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation

## 📦 Quick Start Guide

### Prerequisites
- **Python 3.12+** - [Download](https://python.org)
- **Poetry** - [Installation guide](https://python-poetry.org/docs/#installation)
- **Docker & Docker Compose** - [Get Docker](https://docs.docker.com/get-docker/)

### Installation Steps

```bash
# 1. Clone and setup
git clone https://github.com/LeoCunhaLabz/tdd-project.git
cd tdd-project

# 2. Install dependencies
poetry install

# 3. Setup environment
echo "DATABASE_URL=mongodb://localhost:27017/store" > .env

# 4. Start MongoDB
docker-compose up -d

# 5. Run the application
poetry run uvicorn store.main:app --reload --host 0.0.0.0 --port 8000
# OR: make run

# 6. Access the API
# - API: http://localhost:8000/
# - Docs: http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
```

### Docker Management
```bash
# Container operations
docker-compose up -d        # Start MongoDB
docker-compose ps           # Check status
docker-compose logs db      # View logs
docker-compose down         # Stop containers
```

## 🧪 Testing Strategy

The project implements comprehensive TDD with tests written before implementation, ensuring robust code coverage and reliability.

### Test Execution
```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=store --cov-report=html

# Run specific test categories
poetry run pytest tests/schemas/     # Schema validation
poetry run pytest tests/usecases/   # Business logic

# Advanced options
poetry run pytest -v               # Verbose output
poetry run pytest -n auto          # Parallel execution
poetry run pytest --lf             # Last failed tests only
```

### Test Structure
- **Unit Tests** (`tests/schemas/`): Data model validation
- **Integration Tests** (`tests/usecases/`): Business logic with database
- **Fixtures** (`conftest.py`): Shared test configuration and data
- **Factories** (`factories.py`): Consistent test data generation

### TDD Workflow Example
```python
# 1. Write failing test (Red)
async def test_create_product_should_return_success():
    product_data = ProductIn(name="Test Product", quantity=5, price=99.99)
    result = await product_usecase.create(body=product_data)
    assert isinstance(result, ProductOut)

# 2. Minimal implementation (Green)
async def create(self, body: ProductIn) -> ProductOut:
    product = ProductOut(**body.model_dump())
    await self.collection.insert_one(body.model_dump())
    return product

# 3. Refactor and improve code quality
```

## 📊 Code Quality & Standards

### Pre-commit Hooks
```bash
# Install and setup
make precommit-install
# OR: poetry run pre-commit install

# Run on all files
poetry run pre-commit run --all-files

# Reset if needed
make precommit-reset
```

### Development Standards
- **Type Hints**: 100% type annotation coverage
- **Docstrings**: Comprehensive function documentation
- **Error Handling**: Explicit exception handling with meaningful messages
- **Testing**: All features must include comprehensive tests
- **Coverage**: Maintain above 90% test coverage

## � API Documentation

### Interactive Documentation
FastAPI automatically generates comprehensive API documentation:
- **Swagger UI**: `http://localhost:8000/docs` - Interactive testing interface
- **ReDoc**: `http://localhost:8000/redoc` - Clean documentation format
- **OpenAPI Schema**: `http://localhost:8000/openapi.json` - API specification

### API Endpoints (Planned)
```http
# Product Management
POST   /products           # Create new product
GET    /products/{id}      # Retrieve product by ID
PUT    /products/{id}      # Update existing product
DELETE /products/{id}      # Delete product
GET    /products           # List all products (with pagination)
```

### Request/Response Examples

**Create Product:**
```http
POST /products
Content-Type: application/json

{
    "name": "iPhone 14 Pro Max",
    "quantity": 10,
    "price": 8500.00,
    "status": true
}
```

**Response:**
```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "iPhone 14 Pro Max",
    "quantity": 10,
    "price": 8500.00,
    "status": true,
    "created_at": "2025-08-29T10:30:00Z",
    "updated_at": "2025-08-29T10:30:00Z"
}
```

## 🔄 Test-Driven Development (TDD)

### TDD Cycle Implementation
The project demonstrates the classic **Red-Green-Refactor** cycle:

1. **Red Phase**: Write a failing test that defines the desired functionality
2. **Green Phase**: Write minimal code to make the test pass
3. **Refactor Phase**: Improve code quality while keeping tests green

### TDD Benefits
- **Design-First Approach**: Tests define interfaces before implementation
- **Regression Prevention**: Existing tests ensure changes don't break functionality
- **Living Documentation**: Tests serve as executable documentation
- **Refactoring Confidence**: Tests enable safe code improvements

### Best Practices Applied
- Small, focused tests validating specific behaviors
- Descriptive test names explaining expected behavior
- Fast execution for immediate feedback
- Independent tests that can run in any order
- Clear Arrange-Act-Assert structure

## 🤝 Contributing

### Development Workflow
```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/tdd-project.git
cd tdd-project

# 2. Setup environment
poetry install
make precommit-install
docker-compose up -d

# 3. Create feature branch
git checkout -b feature/new-feature-name

# 4. Follow TDD cycle: Write test → Implement → Refactor
poetry run pytest

# 5. Commit and push
git commit -m "feat: add new feature with tests"
git push origin feature/new-feature-name
```

### Requirements
- Include comprehensive test coverage
- Follow TDD methodology
- Maintain type hints and documentation
- Ensure pre-commit hooks pass
- Update README if needed

### Commit Convention
```bash
feat(scope): description     # New feature
fix(scope): description      # Bug fix
test(scope): description     # Add tests
docs(scope): description     # Documentation
refactor(scope): description # Code refactoring
```

## � Roadmap

### Current Status (Phase 1)
- [x] Project structure and TDD setup
- [x] Product schema definitions
- [x] Database integration with MongoDB
- [x] Test infrastructure and fixtures
- [ ] Complete CRUD operations
- [ ] API endpoint implementation

### Planned Features

**Phase 2 - Core Features:**
- Authentication & Authorization (JWT, RBAC)
- Advanced Product Management (categories, search, filtering)
- Enhanced validation and business rules

**Phase 3 - Production Ready:**
- Performance optimization (caching, indexing)
- Monitoring & observability (logging, metrics)
- Security enhancements (rate limiting, sanitization)

**Phase 4 - Advanced:**
- Microservices architecture
- CI/CD pipeline automation
- Advanced analytics and reporting

## 👨‍💻 Author

**Leonardo** - *Lead Developer & TDD Practitioner*
- GitHub: [@LeoCunhaLabz](https://github.com/LeoCunhaLabz)
- Project: [TDD Store API](https://github.com/LeoCunhaLabz/tdd-project)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Key Dependencies:**
- FastAPI, Pydantic, Motor, Pytest: MIT License
- MongoDB: Server Side Public License (SSPL)

---

## 🎯 Why This Project?

### Educational Value
- **TDD Learning**: Practical implementation of Test-Driven Development
- **Modern Python**: Async programming with FastAPI and MongoDB
- **Clean Architecture**: Professional software engineering practices
- **Production Patterns**: Real-world development workflows

### Perfect For
- Learning TDD methodology and best practices
- Understanding modern Python web development
- Exploring FastAPI and async programming
- Studying clean architecture principles
- Building portfolio projects with professional standards
