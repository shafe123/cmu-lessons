# Common Refactoring Patterns

Refactoring improves the internal structure of code without changing its external behavior. Below are several widely‑used refactoring patterns that developers often apply.

## Extract Method / Function
- **What it does:** Pulls a block of code out of a larger method and places it into its own method with a descriptive name.  
- **Why it helps:** Improves readability, reduces duplication, and makes the original method shorter and clearer.

## Rename Variable / Method / Class
- **What it does:** Gives a more meaningful name to a symbol.  
- **Why it helps:** Makes the intent of the code obvious, reducing cognitive load for future readers.

## Inline Method / Variable
- **What it does:** Replaces a method call or variable reference with its actual implementation/value when the abstraction adds little value.  
- **Why it helps:** Eliminates unnecessary indirection and simplifies the codebase.

## Replace Magic Numbers / Strings with Constants
- **What it does:** Moves hard‑coded literals into named constants.  
- **Why it helps:** Centralizes values that may change, improves self‑documentation, and prevents accidental typos.

## Introduce Parameter Object
- **What it does:** Groups related parameters into a single object.  
- **Why it helps:** Reduces long parameter lists, clarifies relationships among arguments, and eases future extensions.

## Encapsulate Field
- **What it does:** Turns a public field into a private one accessed via getter/setter methods.  
- **Why it helps:** Allows validation, lazy initialization, or later changes to the underlying representation without breaking callers.

## Replace Conditional with Polymorphism
- **What it does:** Moves `if/else` or `switch` logic that depends on type into separate subclasses that each implement the behavior.  
- **Why it helps:** Improves extensibility and adheres to the Open/Closed Principle.

## Introduce Assertion
- **What it does:** Adds explicit checks (assertions) for conditions that should always hold true.  
- **Why it helps:** Catches bugs early and documents assumptions in the code.

## Extract Interface / Abstract Base Class
- **What it does:** Defines a contract (interface) that concrete classes implement.  
- **Why it helps:** Enables dependency injection, easier testing (mocking), and clearer separation of responsibilities.

## Replace Loop with Collection Operation
- **What it does:** Uses higher‑order functions (`map`, `filter`, `reduce`, etc.) instead of explicit loops.  
- **Why it helps:** Leads to more declarative, concise, and often more performant code.

## Split Temporary Variable
- **What it does:** Breaks a variable that holds multiple unrelated values over its lifetime into separate variables.  
- **Why it helps:** Prevents accidental reuse and clarifies each variable’s purpose.

## Remove Dead Code
- **What it does:** Deletes code paths, methods, or classes that are never used.  
- **Why it helps:** Reduces maintenance burden and eliminates confusion.

## Simplify Conditional Expression
- **What it does:** Refactors complex boolean expressions (e.g., nested `if`s) into clearer forms, possibly using guard clauses or early returns.  
- **Why it helps:** Improves readability and reduces nesting depth.

## Replace Exception with Test (or vice‑versa)
- **What it does:** Swaps exception‑driven flow control with explicit condition checks, or the opposite where appropriate.  
- **Why it helps:** Aligns error handling with the language’s idioms and performance considerations.

## Introduce Lazy Loading
- **What it does:** Defers expensive object creation until it’s actually needed.  
- **Why it helps:** Improves startup time and reduces unnecessary resource consumption.

# Refactoring Strategies

## Map Out Inputs, Outputs, and Dependencies
Create a quick “contract” diagram for the code you’re touching: list the function’s parameters, expected return values, side‑effects, and any external services or globals it relies on. This map lets you see exactly what must stay unchanged while you refactor.

## Write Good Test Cases
Ensure you have unit tests (covering normal, edge, and error cases), property‑based tests for random inputs, and a few integration tests that hit real dependencies. A solid test suite is the safety net that lets you modify code confidently.

## Change One Thing At A Time (Strangler Fig)
Break the refactor into tiny, independent steps—extract a method, rename a variable, replace a conditional, etc. After each step run the tests and commit. When you need to replace a large legacy component, route traffic through a thin façade and swap pieces incrementally (the Strangler Fig pattern).

## Manage Complexity
Measure cyclomatic complexity, nesting depth, or duplicated logic with static‑analysis tools. Anything that exceeds a modest threshold (e.g., complexity > 10) becomes a candidate for extraction, simplification, or abstraction. Keeping individual functions simple makes future refactors easier.

## Use Tools
Many IDEs have built-in refactoring tools.  Linters will also tell you if your code is too complex.