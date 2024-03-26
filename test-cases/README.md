# FNML Test Cases

Each test case is within a subfolder of this folder.

If no output.nq file is present, an error is expected.

All function descriptions are locally available under [functions.ttl](./functions.ttl).

Some test cases are under discussion, proposed alternatives are noted via a suffix `b`. 

## Open issues for which there are no test cases

|                              title                              |                                                                  purpose                                                                 |
|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|
| Function on object, 1 constant parameter                        | Tests if a constant parameter can be used                                                                                                |
| Function on object, wrong type parameter                        | Tests a function with a wrong type parameter cannot be used                                                                              |
| Function on object returns null                                 | Tests that no triple should be generated when the result is null.                                                                        |
| Function on object returns empty string                         | Tests that a triple is generated when the results is an empty string.                                                                    |
| Function on object, the output termType is Literal              | Tests if the output of the function is assigned the correct termType                                                                     |
| Function on subject returns invalid IRI                         | Tests that no triples are generated for a subject that gets an invalid IRI as the result from a function.                                |
| Function on predicate returns invalid IRI                       | Tests that no triples are generated for a predicate that gets an invalid IRI as the result from a function.                              |
| Nested function - Test B                                        | Tests if a composite function of form f(g(x1),h(x2)) works (i.e., two different inner functions are the arguments of the outer function) |
| Nested function - Test C                                        | Tests if a composite function of form f(g(h(x1),x2),x3) works (i.e., the inner function is also a composite function)                    |
| Function on graph, 1 parameter                                  | Tests if a function can be used on a graph                                                                                               |
| Function on languageMap                                         | Tests that function on LanguageMap is handled                                                                                            |
| Function on graph returns invalid IRI                           | Tests that no triples are generated for a graph that gets an invalid IRI as the result from a function.                                  |
| Function using non-constant shortcut property function          | Tests that a non-constant FNML Function map also works                                                                                   |
| Function using non-constant shortcut property return            | Tests that a non-constant FNML Return map also works                                                                                     |
| Function as equal join condition                                | Tests that functions can be used similar to R2RML (equal) join conditions                                                                |
| Function as other type of join condition                        | Tests that functions can be used for other types of join conditions (eg. string_contains or listContainsElement)                         |
| Function, parameter as array                                    | Tests that list-style parameters are handled                                                                                             |
| Function, array_get                                             | Tests that list-style of returned data values are handled correctly by FnO                                                               |

## Table

| new_id |                              title                              |                                                            purpose                                                            | data format | error expected? |    input file 1   |
|:------:|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|:-----------:|:---------------:|:-----------------:|
| 0000   | Function on object, 0 parameters                                | Tests (1) if a function without parameters can be used (FnO) (2) if a function on an object map can be used (Term)            | CSV         |      FALSE      | student.csv       |
| 0000b  | Function on object, 0 parameters (replaces 0000)                | Tests (1) if a function without parameters can be used (FnO) (2) if a function on an object map can be used (Term)            | CSV         |      FALSE      | student.csv       |
| 0000   | Function on object, default termType                            | Tests if the output of the function is assigned the correct termType by default                                               |             |                 |                   |
| 0001   | Function on object, 1 reference parameter                       | Tests: (1) if a function with one parameter can be used, (FnO) (2) a reference parameter can be used (Term)                   | CSV         |      FALSE      | student.csv       |
| 0001   | Function using non-constant shortcut property parameter         | Tests that a non-constant FNML Parameter map also works                                                                       | CSV         |      FALSE      | student_param.csv |
| 0002   | Function on object, 1 false reference parameter                 | Tests if a false reference parameters is caught                                                                               | CSV         |       TRUE      | student.csv       |
| 0003   | Function on object, 1 reference parameter, 1 constant parameter | Tests if a function with multiple parameters can be used                                                                      | CSV         |      FALSE      | student.csv       |
| 0004   | Function on predicate, 1 parameter                              | Tests if a function can be used on a predicate                                                                                | CSV         |      FALSE      | student.csv       |
| 0004b  | Function on predicate, 1 parameter (replaces 0004)              | Tests if a function can be used on a predicate                                                                                | CSV         |      FALSE      | student.csv       |
| 0005   | Function on subject, 1 parameter                                | Tests if a function can be used on a subject                                                                                  | CSV         |      FALSE      | student.csv       |
| 0005   | Function on subject, default termType                           | Tests if the default termType assigned to the output of the function to be correct                                            |             |                 |                   |
| 0006   | Function on object, the output termType is IRI                  | Tests if the output of the function is assigned the correct termType                                                          |             |                 |                   |
| 0008   | Function on object, 1 template parameter                        | Tests if a function with a template parameter can be used                                                                     | CSV         |      FALSE      | student.csv       |
| 0009   | Nested function - Test A                                        | Tests if a composite function of form f(g(x1),x2) works (i.e., the inner function is only one argument of the outer function) | CSV         |      FALSE      | student.csv       |