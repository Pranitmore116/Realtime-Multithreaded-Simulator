# Real-Time Multi-Threaded Simulator

A browser-based educational simulator that visually demonstrates **threading models, thread states, synchronization, and concurrency concepts** using **HTML, CSS, JavaScript, and HTML5 Canvas**.

> **Important:** This project simulates multithreading behavior logically. It does not create actual OS-level threads because JavaScript code running in the browser executes on a single main thread.

---

## 📌 Project Overview

The **Real-Time Multi-Threaded Simulator** is designed to make Operating System threading and synchronization concepts easier to understand through interactive visualization.

Instead of explaining threads only through theory, the simulator represents logical threads as animated circles and shows their state changes in real time.

The project demonstrates:

* Many-to-One threading model
* One-to-One threading model
* Many-to-Many threading model
* Thread state transitions
* Binary semaphore synchronization
* Producer-Consumer monitor concept
* Asynchronous execution using JavaScript
* Real-time Canvas visualization
* Event logging

---

## 🎯 Objectives

The main objectives of this project are:

1. To visually demonstrate different threading models.
2. To show thread state transitions in real time.
3. To demonstrate synchronization using a semaphore.
4. To demonstrate the Producer-Consumer concept using monitor-style waiting.
5. To provide an interactive learning tool for Operating Systems students.
6. To demonstrate how asynchronous JavaScript can be used to simulate concurrent behavior.

---

## ✨ Features

### 🧵 Threading Models

The simulator provides three threading models:

#### 1. Many-to-One

Multiple logical threads are executed sequentially.

```text
Thread 1 → RUNNING → TERMINATED
Thread 2 → RUNNING → TERMINATED
Thread 3 → RUNNING → TERMINATED
```

Only one simulated thread is running at a time.

#### 2. One-to-One

Each logical thread is started as a separate asynchronous task.

The tasks are started together using `Promise.all()` and their execution is interleaved by JavaScript's event loop.

#### 3. Many-to-Many

The simulator limits the number of simultaneously running logical threads.

For example:

```javascript
let max = 3;
```

This allows a maximum of three simulated threads to run at a time while other threads wait.

---

## 🔄 Thread States

Each logical thread can have different states:

| State      | Meaning                                         | Visualization |
| ---------- | ----------------------------------------------- | ------------- |
| READY      | Thread is ready to execute                      | Yellow        |
| RUNNING    | Thread is currently executing in the simulation | Green         |
| WAITING    | Thread is waiting for a resource/slot           | Purple        |
| TERMINATED | Thread has completed execution                  | Red           |

The state of a thread is changed using the `updateState()` function.

---

## 🔐 Semaphore Demo

The project includes a **binary semaphore simulation**.

The semaphore starts with:

```javascript
let sem = 1;
```

The logic is:

```text
Semaphore = 1
     ↓
Resource available
     ↓
Thread enters
     ↓
Semaphore = 0
     ↓
Other threads wait
     ↓
Thread exits
     ↓
Semaphore = 1
```

This demonstrates **mutual exclusion**, where only one simulated thread can enter the critical section at a time.

---

## 📦 Monitor Demo

The Monitor Demo demonstrates a simplified **Producer-Consumer synchronization concept**.

A shared resource is initially unavailable:

```javascript
let resource = false;
```

The consumer waits while the resource is unavailable.

The producer later creates the resource:

```javascript
resource = true;
```

The consumer can then continue and consume the resource.

This demonstrates **condition-based synchronization**.

---

## 🎨 Visualization

The project uses **HTML5 Canvas** to display simulated threads as circles.

Each circle contains information represented through its:

* Position
* Color
* Current state

Whenever a thread changes state, the Canvas is cleared and the current thread information is drawn again.

### Visualization Concept

```text
READY       → Yellow
RUNNING     → Green
WAITING     → Purple
TERMINATED  → Red
```

This allows users to understand thread behavior visually instead of relying only on console output or text.

---

## 📝 Event Logging

The simulator contains a live logging panel that records important events.

Example:

```text
=== Many-to-One Running ===
Thread 0: READY
Thread 1: READY
Thread 2: READY
Thread 0: RUNNING
Thread 0: TERMINATED
Thread 1: RUNNING
Thread 1: TERMINATED
```

Logs help users understand the order in which events occur and make debugging easier.

---

## 🏗️ Project Architecture

The project is divided into three logical layers:

```text
                    ┌─────────────────────┐
                    │     User Interface  │
                    │      HTML + CSS     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Simulation Engine  │
                    │     JavaScript      │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌──────────────────┐      ┌──────────────────┐
        │ Synchronization  │      │   Visualization  │
        │ Semaphore/       │      │ HTML5 Canvas +   │
        │ Monitor          │      │ Event Logs       │
        └──────────────────┘      └──────────────────┘
```

---

## 📁 Project Structure

```text
Realtime-Multithreaded-Simulator/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

### `index.html`

Contains the structure of the web application, including:

* Thread model selection
* Thread count input
* Control buttons
* Logs section
* Canvas element

### `style.css`

Controls the visual appearance of the application:

* Dark theme
* Neon styling
* Buttons
* Cards
* Layout
* Input controls

### `script.js`

Contains the main simulation logic:

* Thread creation
* Thread state management
* Threading models
* Async execution
* Semaphore simulation
* Monitor simulation
* Canvas rendering
* Event logging

---

## 🛠️ Technologies Used

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript (ES6+)**

### APIs / JavaScript Features

* HTML5 Canvas API
* `async/await`
* Promises
* `setTimeout()`
* DOM manipulation

### Development Tools

* Visual Studio Code
* Live Server
* Browser Developer Tools
* Git
* GitHub

---

## ▶️ How to Run

### Option 1 — Using VS Code Live Server

1. Clone the repository:

```bash
git clone https://github.com/Pranitmore116/Realtime-Multithreaded-Simulator.git
```

2. Open the project folder in VS Code.

3. Install the **Live Server** extension if it is not already installed.

4. Right-click `index.html`.

5. Select:

```text
Open with Live Server
```

6. The simulator will open in your browser.

---

### Option 2 — Open Directly

You can also open:

```text
index.html
```

directly in a modern web browser.

---

## 🚀 How to Use

### Run a Threading Model

1. Select a threading model.
2. Enter the number of threads.
3. Click **Run Thread Model**.
4. Observe the thread state changes.
5. Check the Canvas visualization and event logs.

### Run Semaphore Demo

Click:

```text
Semaphore Demo
```

The simulator demonstrates how multiple threads compete for a single shared resource.

### Run Monitor Demo

Click:

```text
Monitor Demo
```

The simulator demonstrates Producer-Consumer synchronization.

---

## 🧠 How the Simulation Works

The project does not create actual operating-system threads.

Instead, it represents threads as JavaScript objects.

A simplified thread object contains:

```javascript
{
    x: position,
    y: position,
    color: stateColor,
    state: "READY"
}
```

Execution is simulated using asynchronous JavaScript functions.

For example:

```javascript
await delay(900);
```

represents a simulated delay of **900 milliseconds**.

The delay is used to make state transitions visible to the user.

---

## ⚠️ Important Implementation Note

JavaScript running in the browser is primarily single-threaded.

Therefore, this project does **not** provide true CPU-level parallel execution.

Instead, it uses:

```text
async/await
      +
Promises
      +
setTimeout()
      ↓
Logical Concurrency
```

The purpose is to **visualize and explain operating-system concepts**, not to reproduce actual kernel-level thread scheduling.

---

## 📚 Concepts Demonstrated

This project demonstrates several important Operating Systems concepts:

* Threads
* Thread states
* Threading models
* Concurrency
* Asynchronous execution
* Synchronization
* Mutual exclusion
* Semaphores
* Monitors
* Producer-Consumer problem
* Critical sections
* Waiting
* Logical scheduling

---

## 🔮 Future Scope

The simulator can be extended with:

* Round Robin scheduling
* Shortest Job First (SJF)
* Priority Scheduling
* First Come First Serve (FCFS)
* CPU/core visualization
* Deadlock detection
* Deadlock prevention algorithms
* Mutex demonstration
* Multiple semaphore values
* Real-time execution statistics
* Thread execution timeline
* Gantt chart visualization
* Interactive thread creation
* More advanced synchronization problems

---

## ⚠️ Limitations

* The project uses simulated threads rather than real OS-level threads.
* Execution timing is approximate and intended for visualization.
* It does not interact with the operating system kernel.
* The synchronization mechanisms are educational simulations.
* The Canvas visualization represents thread states rather than actual CPU execution.

---

## 🎓 Educational Purpose

This project is primarily intended as an **educational tool for Operating Systems**.

It helps students understand abstract concepts by allowing them to visually observe:

```text
Thread Creation
       ↓
Thread States
       ↓
Execution
       ↓
Waiting
       ↓
Synchronization
       ↓
Termination
```

---

## 👨‍💻 Author

**Pranit**

GitHub:
**Pranitmore116**

---

## 📄 License

This project is created for educational and academic purposes.
