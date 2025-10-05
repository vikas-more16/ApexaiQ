# Python and API Development Documentation

---

### Part A — Python Fundamentals

### 1) Python Syntax, Variables, and Data Types

**Syntax** is the set of rules that defines how Python code is written.

- **Variables** store values. You don’t declare a type; Python infers it.
- Assignment uses `=`; equality check uses `==`.

**Built‑in data types:**

- `int` – whole numbers
- `float` – decimal numbers
- `str` – text
- `list` – ordered, changeable collection
- `tuple` – ordered, **unchangeable** collection
- `dict` – key–value pairs
- `set` – unordered collection of **unique** items

```python
age = 21                 # int
pi = 3.14159             # float
name = "Vikas"           # str

nums = [1, 2, 3]         # list (mutable)
point = (10, 20)         # tuple (immutable)
student = {"name": "Vikas", "roll": 101}  # dict
unique_ids = {101, 102, 103, 103}         # set -> {101, 102, 103}
```

**Quick checks:**

```python
type(name)   # <class 'str'>
len(nums)    # 3
```

---

### 2) Conditional Statements (if–elif–else)

Conditional statements are used to make **decisions** in your program.  
They help you execute specific blocks of code depending on whether a condition is **True** or **False**.

Use them to make decisions.

```python
score = 72
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)   # B
```

**Tip:** Conditions must evaluate to True/False.

---

### 3) Loops (for, while, break, continue)

**for** loops iterate over a sequence; **while** loops run until a condition becomes False.
**break** Stops the loop immediately, even if the condition is still True.
**continue** Skips the current iteration and moves to the next one.

```python
# for + continue (skip)
for i in range(5):
    if i == 3:
        continue
    print(i)   # 0,1,2,4

# while + break (stop)
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break   # stops at 0,1,2
```

---

### 4) Functions (parameters, return, default args, \*args, \*\*kwargs)

**Function** - A function is a block of code that performs a specific task and can be reused.
-- Parameters are inputs that you pass to a function.
-- A function can return a value using the return keyword.
-- We can provide default values for parameters. If the argument is not passed, the default is used.
-- If we want to pass multiple values without knowing how many, use *args.
*args collects arguments as a tuple.
-- If we want to pass named arguments dynamically, use **kwargs.
**kwargs collects arguments as a dictionary.

```python
def greet(name="World"):                 # default argument
    return f"Hello, {name}"              # return value

def add(*numbers):                       # *args: any number of positional args
    return sum(numbers)

def profile(**info):                     # **kwargs: any number of keyword args
    return ", ".join(f"{k}={v}" for k, v in info.items())

print(greet())                 # Hello, World
print(add(1, 2, 3))            # 6
print(profile(name="Vikas", city="Shegaon"))
```

**Parameter order rule:** `positional, *args, default/keyword, **kwargs`.

---

### 5) Exception Handling (try–except–finally)

**Exception Handling** is used to **handle errors** that occur while running a program, so that the program doesn’t crash.

- Errors during program execution are called **exceptions**.
- Python provides `try`, `except`, `else`, and `finally` to handle exceptions.

- try block → Code that might cause an error goes here.
  except block → Executes if an error occurs.
  The else block runs only if no exception occurs in the try block.
  The finally block always runs, whether an exception occurs or not.
  Specific exceptions like ZeroDivisionError or ValueError can be caught.

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
finally:
    print("This always runs (cleanup, close files, etc.)")
```

**Custom exception:**

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
```

---

### 6) Decorators (wrap behavior around functions)

A decorator takes a function, adds extra behavior, and returns a new function—**without** changing the original code.

```python
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return value
    return wrapper

@timeit
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

slow_add(2, 3)  # prints time taken, returns 5
```

---

### 7) OOPS (Object-Oriented Programming Concepts)

- **Class** – blueprint; **Object** – instance of a class
- **Attributes** – data of the object; **Methods** – functions on the object
- **Encapsulation** – hide internal details
- **Inheritance** – child class gets features of parent class
- **Polymorphism** – same method name, different behaviors
- **Abstraction** – expose what’s needed, hide the rest

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):                    # inheritance
    def speak(self):                  # polymorphism (override)
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

pets = [Dog(), Cat()]
for p in pets:
    print(p.speak())   # Woof, Meow
```

---

### 8) List & Dictionary Comprehensions

Short, readable one‑liners to create lists/dicts.

```python
squares = [x*x for x in range(6)]                     # [0,1,4,9,16,25]
evens = [x for x in range(10) if x % 2 == 0]          # filter

word = "python"
codes = {ch: ord(ch) for ch in word}                  # {'p':112, ...}
```

---

### 9) Iterators & Generators

**Iterator**: object with `__iter__()` and `__next__()`.
**Generator**: a function using `yield` to produce a sequence lazily.

```python
def countdown(n):
    while n > 0:
        yield n      # pauses here, resumes next call
        n -= 1

for i in countdown(3):
    print(i)         # 3,2,1
```

**Why generators?** Efficient memory (streaming large data).

---

### 10) Virtual Environments & `pip`

Keep project dependencies isolated.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install requests==2.32.3
pip freeze > requirements.txt
```

Deactivate with `deactivate`.

---

### 11) Python Standard Libraries

Python comes with many **pre-installed standard libraries**. Here are the most important and commonly used:

---

## Math and Random

| Library  | Purpose                                                       |
| -------- | ------------------------------------------------------------- |
| `math`   | Mathematical functions like `sqrt`, `sin`, `cos`, `factorial` |
| `random` | Generate random numbers, choices, shuffling                   |

---

## Data Structures & Utilities

| Library       | Purpose                                                       |
| ------------- | ------------------------------------------------------------- |
| `collections` | Specialized containers like `Counter`, `deque`, `OrderedDict` |
| `itertools`   | Iterator building tools (combinations, permutations)          |
| `functools`   | Higher-order functions (`wraps`, `reduce`)                    |

---

## File & OS Handling

| Library   | Purpose                                               |
| --------- | ----------------------------------------------------- |
| `os`      | Interacting with operating system, files, directories |
| `shutil`  | High-level file operations (copy, move, delete)       |
| `pathlib` | Object-oriented file system paths                     |
| `csv`     | Read/write CSV files                                  |
| `json`    | Encode/decode JSON data                               |

---

## Date & Time

| Library    | Purpose                          |
| ---------- | -------------------------------- |
| `datetime` | Work with dates and times        |
| `time`     | Time-related functions and sleep |
| `calendar` | Calendar-related operations      |

---

## Networking & Internet

| Library   | Purpose                            |
| --------- | ---------------------------------- |
| `socket`  | Low-level networking (TCP/IP, UDP) |
| `urllib`  | Fetch data from URLs               |
| `smtplib` | Sending emails via SMTP            |

---

## System & Debugging

| Library    | Purpose                                 |
| ---------- | --------------------------------------- |
| `sys`      | Python interpreter and system functions |
| `logging`  | Logging messages for debugging          |
| `argparse` | Command-line argument parsing           |

---

This list covers the **essential standard libraries** that are used in most Python programs.

```python
from collections import Counter
print(Counter("banana"))        # Counter({'a':3,'n':2,'b':1})
```

---

## Part B — Coding Standards (Clean, Readable, Reliable)

### 1) Naming Conventions (PEP 8)

- **Variables/Functions**: `snake_case` → `total_price`
- **Classes**: `PascalCase` → `OrderItem`
- **Constants**: `UPPER_CASE` → `MAX_RETRIES`
- Avoid ambiguous names (`l`, `O`, `I`).

### 2) Docstrings

Use triple quotes with a short summary + params + returns.

```python
def area(radius):
    """Compute the area of a circle.

    Args:
        radius (float): Radius in meters.

    Returns:
        float: Area in square meters.
    """
    from math import pi
    return pi * radius * radius
```

### 3) Comments

- Good: **why** something is done or tricky logic.
- Avoid obvious comments.

```python
# Convert rupees to paise to avoid floating-point issues
amount_paise = int(amount_rupees * 100)
```

### 4) Types of Testing

- **Unit** – functions/classes in isolation (e.g., `pytest`)
- **Integration** – modules working together
- **System/End‑to‑End** – whole app
- **User Acceptance (UAT)** – validates with users
- **Test Pyramid** – more unit tests, fewer E2E

### 5) PEP 8 (style guide highlights)

- 4 spaces indentation (no tabs)
- Max line length: 79/88 (depending on tool)
- Imports at top, grouped: stdlib, third‑party, local
- Spaces around operators: `a + b`, not `a+b`
- Use `black`, `ruff`, or `flake8` to automate

### 6) SOLID and DRY Principles

- **S**ingle Responsibility – each module/class does one thing well
- **O**pen/Closed – extend behavior without modifying existing code
- **L**iskov Substitution – subclasses must be usable as base class
- **I**nterface Segregation – small, focused interfaces
- **D**ependency Inversion – depend on abstractions, not concrete classes
- **DRY** – don’t duplicate logic; extract reusable functions/classes

**DRY example:**

```python
# Bad
tax1 = price * 0.18
tax2 = discount * 0.18

# Good
def gst(amount, rate=0.18):
    return amount * rate
```

---

## Part C — APIs

### 1) What is an API?

An **API** (Application Programming Interface) lets one program talk to another using defined requests and responses.

**Everyday analogy:** Restaurant menu = API. You ask (request), kitchen returns food (response).

### 2) Types of APIs

- **Open/Public** – available to external developers (e.g., GitHub API)
- **Internal/Private** – only inside your company
- **Partner** – shared with specific partners under agreements
- **Composite** – bundles multiple API calls into one

### 3) HTTP Status Codes (most used)

- **2xx Success** – request worked (200 OK, 201 Created, 204 No Content)
- **3xx Redirect** – resource moved
- **4xx Client Error** – problem in your request (400, 401, 403, 404, 409)
- **5xx Server Error** – problem on the server (500, 502, 503)

```text
200 OK            → GET /users/1
201 Created       → POST /users
400 Bad Request   → Missing required field
401 Unauthorized  → Invalid/missing token
403 Forbidden     → Valid token but not allowed
404 Not Found     → Resource doesn't exist
409 Conflict      → Duplicate, version clash
422 Unprocessable → Validation failed
429 Too Many Requests → Rate limit hit
```

### 4) Response Formats

- **JSON** (most common):

```json
{
  "status": "success",
  "data": { "id": 1, "name": "Vikas" }
}
```

- **XML**:

```xml
<user><id>1</id><name>Vikas</name></user>
```

- **YAML** (config):

```yaml
user:
  id: 1
  name: Vikas
```

### 5) Types of API Authentication

- **API Key** – simple token in header; good for server‑to‑server
- **Basic Auth** – `username:password` (base64); use only over HTTPS
- **OAuth 2.0** – delegated access via providers (Google, GitHub)
  - Flows: Authorization Code (web apps), Client Credentials (service-to-service), PKCE (mobile/SPA)
- **JWT (JSON Web Token)** – signed token containing claims

**JWT example (Python):**

```python
import jwt, datetime
payload = {
    "sub": "user_101",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}
token = jwt.encode(payload, "secret_key", algorithm="HS256")
```

### 6) Versioning & Security

- **Versioning**: `/api/v1/users` or header `Accept: application/vnd.myapp.v1+json`
- **Security basics**:
  - Always use **HTTPS**
  - Validate & sanitize inputs
  - **Rate limiting** & **throttling**
  - Use **scopes/roles** in tokens
  - Avoid sensitive data in URLs
  - Enable **CORS** carefully
  - Log securely; never log secrets
  - Prefer **idempotent** PUT/DELETE

### 7) CRUD Operations (with REST endpoints)

| Operation | HTTP   | Example Endpoint      | Body/Notes             |
| --------- | ------ | --------------------- | ---------------------- |
| Create    | POST   | `/api/users`          | JSON body for new user |
| Read      | GET    | `/api/users/{id}`     | Query a single user    |
| Read-all  | GET    | `/api/users?limit=50` | Pagination             |
| Update    | PUT    | `/api/users/{id}`     | Full update            |
| Patch     | PATCH  | `/api/users/{id}`     | Partial update         |
| Delete    | DELETE | `/api/users/{id}`     | Remove resource        |

### 8) Explore Postman (optional)

- Create a **Collection** and **Environment** (base URL, tokens)
- Add **Examples** to auto‑document responses
- Use **Tests** tab for scripts (status code, schema checks)
- Run **Collection Runner** for automation

### 9) Optimization & Efficiency

- Pagination & filtering: `?page=2&limit=50`
- Caching: `ETag`, `Cache-Control`
- Compression: `gzip`
- Avoid N+1 DB queries; use `JOIN`/batch fetch
- Timeouts, retries with **exponential backoff**
- Use **asynchronous** workers for heavy tasks

### 10) Python `requests` Library (practical patterns)

```python
import requests

BASE = "https://jsonplaceholder.typicode.com"

# GET with params and timeout
r = requests.get(f"{BASE}/posts", params={"userId": 1}, timeout=5)
r.raise_for_status()
print(r.json()[:1])

# POST with JSON body and headers
payload = {"title": "Hello", "body": "World", "userId": 1}
r = requests.post(f"{BASE}/posts", json=payload, timeout=5)
print(r.status_code, r.json())

# Robust pattern with session + retry (simple)
s = requests.Session()
s.headers.update({"User-Agent": "Vikas-Client/1.0"})
resp = s.get(f"{BASE}/todos/1", timeout=5)
print(resp.json())
```

### 11) RBAC (Role‑Based Access Control) (optional but useful)

- **Role**: a named group of permissions (e.g., `admin`, `teacher`, `student`)
- **Permission**: an action allowed on a resource (e.g., `attendance:read`)

```python
PERMISSIONS = {
    "admin": {"users:create", "users:delete", "attendance:*"},
    "teacher": {"attendance:read", "attendance:mark"},
    "student": {"attendance:read_own"}
}

def can(role, permission):
    perms = PERMISSIONS.get(role, set())
    return permission in perms or any(p.endswith(":*") and permission.startswith(p[:-1]) for p in perms)

print(can("teacher", "attendance:mark"))     # True
print(can("student", "attendance:mark"))     # False
```

---

## Part D — Extra Topics

### 1) SDLC (Software Development Life Cycle)

Phases:

1. **Requirement Analysis** – understand the problem and constraints
2. **Design** – architecture, database schema, API contracts
3. **Implementation** – coding
4. **Testing** – unit/integration/system/UAT
5. **Deployment** – release to users (CI/CD pipelines)
6. **Maintenance** – bug fixes, improvements

**Tip:** Keep documentation updated in every phase.

### 2) Agile Basics (Scrum in short)

- Timeboxed **Sprints** (1–4 weeks)
- Roles: **Product Owner**, **Scrum Master**, **Developers**
- Ceremonies: **Sprint Planning**, **Daily Stand‑up**, **Review**, **Retrospective**
- Artifacts: **Product Backlog**, **Sprint Backlog**, **Increment**

### 3) Version Control (Git essentials)

```bash
git init
git status
git add .
git commit -m "feat: initial project"
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

**Branching tips:**

- `main` (stable), feature branches (`feat/login`), `fix/bug-123`
- Pull Requests + code reviews
- Protect `main` with CI checks

### 4) Software Architecture (clear mental models)

- **Monolith** – one deployable unit; simple to start, harder to scale teams
- **Microservices** – many small services; independent deploys; more ops complexity
- **Layered (N‑tier)** – presentation → business → data
- **Hexagonal/Clean** – domain‑centric, ports & adapters (easier testing)
- **MVC** – Model, View, Controller (common in web frameworks)
- **Communication** – REST (simple), GraphQL (flexible), gRPC (fast, typed)

**Design Guidelines:**

- Separate concerns (layers/modules)
- Keep boundaries explicit (don’t leak DB models everywhere)
- Prefer **composition** over inheritance for flexibility
- Add **observability** (metrics, logs, traces)

---

## Final Checklist (Practical)

- Use a **virtualenv** per project
- Enforce style with **black** + **ruff**
- Write **docstrings** & meaningful **tests**
- Design APIs with **clear contracts** and **proper status codes**
- Secure with **HTTPS, auth, validation, rate limits**
- Monitor performance; cache; paginate

---

### Useful Mini Cheat Sheet

- List comprehension: `[f(x) for x in items if cond(x)]`
- Dict comprehension: `{k: f(v) for k, v in d.items()}`
- Generator: `def gen(): yield something`
- Decorator: `@decorator` above a function
- Requests: `requests.get(url, params=..., headers=...)`
- Git: `clone → branch → add → commit → push → PR`

---
