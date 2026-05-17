# Python Modules

<img align="right" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDhkd2VyNHVidjgwNWlhMTduaWVneTZjMGozc3AxeTJyd2poaXVpbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UIN7Andwh7kDZGUvmt/giphy.gif" 
       style="width:400px; height:auto; border-radius:40px;"> 


This repository brings together the entire progressive learning path <br> in **Python** within milestone 02 of 42. The ecosystem extends from <br> the language fundamentals to advanced architectures, such as Data <br> Engineering, Object-Oriented Programming (OOP), Design Patterns, <br> Environment Governance, and Advanced Functional Programming, <br> applying immersive real-world scenarios.


---

## 🗺️ Modules Overview

| Module | Project Name | Context / Theme | Key Concepts Explored |
| :---: | :--- | :--- | :--- |
| **00** | **Growing Code** | Community Garden and Sustainability | First steps with Python syntax, variables, strings, arithmetic operators, conditional structures (`if/else`), loops (`while`/`for`), and introduction to *Type Hints*. |
| **01** | **Code Cultivation** | Digital Gardening Ecosystem | Systems modeling using Object-Oriented Programming (OOP): classes, instance methods, encapsulation, inheritance, and composition. |
| **02** | **Garden Guardian** | IoT Smart Agriculture | Resilient data engineering and error handling: multiple exception catching, creation of custom errors (`raise CustomError`), and use of the `finally` block. |
| **03** | **Data Quest** | Electronic Games Backend | Manipulation and optimization of data structures: lists, tuples, sets (`Sets`), dictionaries, and efficient transformations with *List/Dict Comprehensions*. |
| **04** | **Data Archivist** | Cyber Archives (Year 2087) | Secure Input/Output (I/O) operations: reading/writing text files, processing streams in blocks (*chunks*), and use of *Context Managers* (`with`). |
| **05** | **Code Nexus** | Streams in Neo-Tokyo | Advanced software engineering: implementation of abstract classes (ABC), method overriding (`override`), subtype polymorphism, and chaining with `super()`. |
| **06** | **The Codex** | Digital Alchemy Laboratory | Code architecture and imports: packages with `__init__.py`, absolute vs. relative paths, dynamic scope control, and resolution of circular dependencies. |
| **07** | **Data Deck** | Monster Battle Engine | Introduction to GoF *Design Patterns*: practical application of *Factory Method* (decoupled instantiation) and *Strategy* patterns. |
| **08** | **The Matrix** | Zion Network Infrastructure | Governance and production readiness: environment isolation with `venv`, deterministic dependency management with Poetry, and credential security with `.env`. |
| **09** | **Cosmic Data** | Cosmic Data Observatory | Data modeling and integrity: definition of rigid schemas, automatic type coercion, and complex interdependent (*cross-field*) validations via Pydantic v2. |
| **10** | **FuncMage** | Cyberpunk Mage Guild (Year 2142) | Functional paradigm and metaprogramming: anonymous functions (`lambda`), higher-order operations (`map`/`filter`/`reduce`), scope retention (*Closures*), and *Decorators*. |

---
## 🛠️ Code Quality and Mandatory Standards

To comply with the evaluation requirements (*norma*) of the 42 bootcamp, all code developed in this repository strictly adheres to the guidelines below:

```bash
# Code formatting according to the official style guide (PEP 8)
flake8 .

# Static checking and rigorous validation of type hints (Type Hinting)
mypy .
