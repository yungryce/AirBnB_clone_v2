<h1 align="center">HBNB - AirBnB Clone</h1>

![AirBnB Logo](https://i.imgur.com/QiU1LdE.png)

This repository contains a student project to build a clone of the AirBnB website. The project has evolved from a simple console application to a more robust web application with database storage and deployment capabilities.

## Project Overview

- **Version 1**: Backend console to manage program data with JSON serialization/deserialization
- **Version 2**: Enhanced with MySQL database storage, Flask web application, and deployment automation

## Technology Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python 3.x |
| **Database** | MySQL, SQLAlchemy ORM |
| **Web Framework** | Flask |
| **Deployment** | Fabric, Nginx |
| **Frontend** | HTML5, CSS3 |
| **Storage** | JSON File Storage, MySQL Database |
| **Testing** | unittest framework |

## Repository Contents

| Component | Description |
| ----- | ------ |
| [/models](https://github.com/justinmajetich/AirBnB_clone/tree/dev/models) | Class definitions for all models with ORM integration |
| [/models/engine](https://github.com/justinmajetich/AirBnB_clone/tree/dev/models/engine) | Storage engines for file and database persistence |
| [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | Unit tests for all classes and storage engines |
| [/web_flask](https://github.com/justinmajetich/AirBnB_clone_v2/tree/master/web_flask) | Flask web application routes and templates |
| [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Command interpreter to manage objects |

## Getting Started

### Installation
```bash
git clone https://github.com/username/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

### Database Setup
```bash
mysql -u root -p < setup_mysql_dev.sql
```

## Usage

### Interactive Console

Start the command interpreter:
```bash
./console.py
```

#### Available Commands

* **create**: Creates a new instance of a class
  ```
  (hbnb) create BaseModel
  3aa5babc-efb6-4041-bfe9-3cc9727588f8
  ```

* **show**: Displays an instance based on class and ID
  ```
  (hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
  ```

* **destroy**: Removes an instance based on class and ID
  ```
  (hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
  ```

* **all**: Shows all instances or instances of a class
  ```
  (hbnb) all
  (hbnb) all BaseModel
  ```

* **update**: Updates an instance by adding or changing attribute
  ```
  (hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
  ```

* **quit/EOF**: Exits the program

#### Alternative Syntax

Commands can also be executed with class-specific syntax:

```
(hbnb) User.all()
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
(hbnb) User.destroy("38f22813-2753-4d42-b37c-57a17f1e4f88")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {"first_name": "John", "age": 89})
```

### Running Flask Web Application
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.0-hello_route
```

### Deploying to Servers
```bash
python3 3-deploy_web_static.py
```

## Testing
```bash
python3 -m unittest discover tests
```

## Authors
See the list of [contributors](./AUTHORS) who participated in this project.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.