# Bug Types

A quick reference for the major families of bugs you’ll encounter.  
These categories overlap—many real‑world defects belong to several groups at once.

## Syntax / Compile‑Time

*Definition*: Errors that prevent the code from being translated or interpreted.  
Typical messages come from the compiler, interpreter, or linter.

### Common symptoms
- "unexpected token", "missing semicolon", "undeclared identifier".
- Build fails before any tests run.

### Typical fixes
- Correct spelling / punctuation.
- Add missing imports or type declarations.
- Adjust language version / compiler flags.

### Helpful tools
- IDE linters (VS Code, IntelliJ, PyCharm).
- Static analysers (ESLint, Pylint, clang‑tidy).
- Build logs (`make`, `npm run build`, `cargo build`).

---

## Runtime

Bugs that surface **while the program is executing**. They usually raise exceptions or corrupt state.

### Unhandled Exceptions
- Exceptions that propagate to the top level and crash the process.
- Examples: `NullReferenceException`, `IndexError`, `KeyError`.

**How to tackle**
1. Capture the full stack trace.
2. Add try/catch blocks around the risky code.
3. Log contextual data (input values, request IDs).

### Data Issues
- Invalid, missing, or malformed input that the code assumes is correct.
- Examples: empty strings where a URL is required, negative numbers where only positives make sense.

**How to tackle**
- Validate inputs early (guard clauses, schema validators).
- Write unit tests covering edge‑case data.
- Use defensive programming (`Option<T>`, `Result<T,E>`).

### Memory Management
- Leaks, double frees, use‑after‑free, buffer overruns (mostly in C/C++, Rust unsafe code, native extensions).

**How to tackle**
- Run under sanitizers (`AddressSanitizer`, `Valgrind`).
- Employ RAII / smart pointers (`std::unique_ptr`, `Arc`).
- Profile heap usage (`heaptrack`, Chrome DevTools heap snapshot).

### Concurrency / Threading (runtime subset)
- Data races, deadlocks, livelocks, priority inversion.

**How to tackle**
- Use thread‑sanitizer (`tsan`) or Helgrind.
- Prefer higher‑level primitives (channels, actors, async/await).
- Add timeouts to lock acquisition and log lock order.

---

## Logic

Defects where the program *runs* but produces the wrong result because the algorithm or decision‑making is flawed.

### Off‑by‑One / Counting Errors
- Loop iterates one time too many/too few.
- Indexing starts at 0 vs. 1 incorrectly.

**Fixes**
- Write explicit loop bounds (`for i in range(0, n)` vs. `range(n)`).
- Use language‑provided iterators (`foreach`, `map`) when possible.

### Improper Branching
- Wrong boolean condition, misplaced `else`, missing `break`.
- Example: `if (a && b || c)` when parentheses are needed.

**Fixes**
- Break complex conditions into named boolean variables.
- Add unit tests for each branch path.

### Concurrency / Threading (logic subset)
- Incorrect assumptions about ordering (e.g., "this callback will always run after that one").

**Fixes**
- Model state transitions formally (state machine diagrams).
- Use synchronization primitives or immutable data structures.

### Domain‑Specific Logic Errors
- Business‑rule misinterpretation (tax calculation, permission checks).
- Often discovered only through stakeholder review.

**Fixes**
- Write specification‑driven tests (BDD style: Given‑When‑Then).
- Keep a living document of the business rules alongside the code.

---

# General Techniques for Debugging

A toolbox of strategies you can combine in any order that fits the situation.

---

## Print‑Statement Debugging

> "If you can’t see it, you can’t fix it."

- Insert `console.log`, `printf`, `println`, or `logger.debug` at strategic points.
- Log **identifiers** (request ID, transaction ID) to correlate across services.
- Remember to **remove or downgrade** the statements after the bug is fixed to avoid log noise.

### Tips
- Structure logs as JSON for easy filtering.
- Include timestamps and severity levels (`debug`, `info`, `warn`, `error`).

---

## Interactive Debugging

- **Breakpoints**: pause execution at a line, inspect variables, evaluate expressions.
- **Watch expressions**: automatically update a variable’s value as you step.
- **Conditional breakpoints**: trigger only when a predicate holds (`i == 42 && user.id == 7`).

### Popular debuggers
| Language | Tool |
|----------|------|
| Python   | `pdb`, VS Code Debugger |
| JavaScript/Node | Chrome DevTools, `node --inspect` |
| Java     | IntelliJ/IDEA, JDB |
| Go       | Delve (`dlv`) |
| C/C++    | GDB, LLDB |

---

## Test‑Driven Isolation

1. **Write a failing test** that captures the bug’s observable behavior.
2. **Run the test suite** – it should fail only because of the bug.
3. **Fix the code** until the test passes.
4. **Commit the test** so the regression can’t reappear.

Benefits:
- Guarantees reproducibility.
- Documents the expected behavior.
- Encourages clean, modular design.

---

## Reproduce a Minimal Example

- Strip away unrelated modules, external services, and UI layers.
- Keep only the function(s) that demonstrate the defect.
- Share this snippet with teammates or on forums for quicker assistance.

### Checklist for a good minimal example
- ≤ 30 lines of code.
- No hidden global state.
- Deterministic (no random seeds unless fixed).
- Includes a clear "expected vs. actual" comment.

---

## Profiling

When performance or resource usage is the symptom:

| Aspect | Tool | Typical Insight |
|--------|------|-----------------|
| CPU    | `perf`, `py-spy`, Chrome DevTools CPU Profiler | Hot functions, call stacks |
| Memory | Heap snapshots, `valgrind --tool=massif`, `go tool pprof` | Leaks, large objects |
| I/O/Network | `strace`, Wireshark, `tcpdump`, `otel` traces | Blocking syscalls, latency spikes |
| Concurrency | Thread sanitizer, `async-profiler` | Contended locks, thread states |

**Workflow**  
1. Record a profile under normal load.  
2. Identify the top‑consuming hotspots.  
3. Add targeted logging or unit tests around those areas.  
4. Refactor/optimize, then re‑profile to confirm improvement.

---

## Log Analysis

- Centralize logs (ELK stack, Loki, Splunk) to search across services.
- Use **structured fields** (`level`, `service`, `trace_id`) for correlation.
- Create alerts for anomalous patterns (spikes in `ERROR` count, sudden latency increase).


# General Debugging Strategies
At the beginning of the day, you really only know one thing "something bad is happening".  So treat it like a mystery that needs to be solved.  Since "something bad" is happening, it's safe to assume that there is either
1. bad data
1. bad logic
   
You can use the ideas below to help narrow down the issue.

## RTFE (RTFM)
- READ THE ERROR

## Develop and Test Hypotheses (KISS)

- Start with _a_ **high‑level hypothesis**: "Maybe the environment is wrong, maybe a dependency changed, maybe a file got moved, did I save my code?"
- Begin validating the hypothesis with easy, simple verifications: "I am running the right version", "I have the correct data", "It is happening in this block".
- Repeat until you find an invalid hypothesis.

## Narrow Down the Scope of Possible Errors (Divide‑and‑Conquer)

- **Binary‑search**: try to cut the search space in half as often as possible.  Narrow problems down at the _function level_ and go from there.
- Which lines do I get to successfully?  Which lines do I not get to successfully?
- Run the program with **minimal input** and **minimal code** that still reproduces the issue.
- Use **feature flags** to isolate new functionality.

## Expand Your Scope
- Possible that the error is occurring outside of your local function
- _Backtrace_ from where you think the error is occurring to any dependencies of that line.
- Rinse and repeat