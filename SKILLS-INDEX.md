This document maps specific skills demonstrated in the AirBnB clone v2 project to code components and features.

## Programming Fundamentals

### Object-Oriented Programming
- **Enhanced Class Models**: [`models/*.py`](models/) - Updated models with SQLAlchemy integration
- **ORM Implementation**: [`models/engine/db_storage.py`](models/engine/db_storage.py) - Database storage engine
- **Dual Storage Support**: [`models/__init__.py`](models/__init__.py) - Factory pattern for storage selection

### Database Design
- **Schema Creation**: [`setup_mysql_dev.sql`](setup_mysql_dev.sql) - Database and user setup
- **ORM Relationships**: [`models/city.py`](models/city.py) - Foreign key relationships and backref
- **Query Optimization**: [`models/engine/db_storage.py`](models/engine/db_storage.py) - Efficient database queries

## Web Development

### Flask Application
- **Route Definition**: [`web_flask/*.py`](web_flask/) - Various Flask route handlers
- **Template Rendering**: [`web_flask/templates/`](web_flask/templates/) - Jinja2 templates
- **Application Factory**: [`web_flask/100-hbnb.py`](web_flask/100-hbnb.py) - Complete Flask application

### Server Configuration
- **Nginx Setup**: [`0-setup_web_static.sh`](0-setup_web_static.sh) - Web server configuration
- **Static File Serving**: Configured static file paths and aliases

## Deployment Operations

### Automation Scripts
- **Archive Creation**: [`1-pack_web_static.py`](1-pack_web_static.py) - Packaging static files
- **Remote Deployment**: [`2-do_deploy_web_static.py`](2-do_deploy_web_static.py) - Deployment to web servers
- **End-to-End Deployment**: [`3-deploy_web_static.py`](3-deploy_web_static.py) - Full deployment workflow
- **Cleanup Operations**: [`100-clean_web_static.py`](100-clean_web_static.py) - Managing deployment archives

### Shell Scripting
- **Environment Setup**: [`0-setup_web_static.sh`](0-setup_web_static.sh) - Server preparation script
- **Configuration Management**: Using Fabric and shell commands for consistent deployments

## System Integration

### Console Enhancement
- **Key-Value Parsing**: [`console.py`](console.py) - Updated create command with parameter handling
- **ORM Integration**: Console operations supporting both storage types

### Storage Abstraction
- **Engine Selection**: Environment variable based storage engine selection
- **Interface Standardization**: Common methods across storage engines
- **Session Management**: Database connection and session handling

## Testing and Quality Assurance
- **ORM Unit Testing**: [`tests/test_models/`](tests/test_models/) - Testing with database backend
- **Storage Validation**: Tests for both file and database storage engines
- **PEP8 Compliance**: Style checking for clean code