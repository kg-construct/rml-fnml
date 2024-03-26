## Definitions

<!-- - <dfn>FnO</dfn>: the Function Ontology. Describes implementation-independent functions' inputs and outputs, and execution descriptions. -->
<!-- - <dfn>RML</dfn>: RDF Mapping Language. Describes schema transformations from heterogeneous data sources to RDF. -->
<!-- - <dfn>FNML</dfn>: describes how to integrate data transformations in schema transformations using <a>FnO</a> in <a>RML</a>. -->

### Generic

[[RML]]-independent defintions:

- A <dfn>Function</dfn>: an implementation-independent declaration of a function,
  specified using multiple parameters and multiple returns.
  For example, a [=Function=] can be declared as follows: `function int sum(int a, int b) throws StackOverFlowException`, namely,
  the [=Function=] `sum` has two input parameters, `int a` and `int b`, and returns an `int` or throws a `StackOverFlowException`.
- A <dfn>Parameter</dfn>: an input parameter of a [=Function=].
- A <dfn>Return</dfn>: an output return of a [=Function=].
- An <dfn>Execution</dfn>: an invocation of a [=Function=].
  Concrete values are bound to the input [=Parameter=]s,
  and concrete values are bound to the [=Return=]s after execution.
  For example, `sum(2, 4) = 6` is an execution,
  where `2` is bound to the `a` [=Parameter=], `4` is bound to the `b` [=Parameter=], and `6` is bound as [=Return=] value.

### RML

Definitions taken from [[RML]] or [[[R2RML]]]:

- An <dfn>RML mapping</dfn>: defined in [[RML]] at <http://w3id.org/rml/core/spec/>.
- A <dfn>Triples Map</dfn>: defined in [[RML]] at <http://w3id.org/rml/core/spec/>.
- A <dfn>Term Map</dfn>: defined in [[RML]] at <http://w3id.org/rml/core/spec/>.
- a <dfn>Expression Map</dfn>: defined in [[RML]] at <http://w3id.org/rml/core/spec/>.
<!-- - An <dfn>RML processor</dfn> is a tool that interprets the <a>RML mapping</a> and executes its rules to generate RDF triples. -->
- A <dfn>constant expression shortcut property</dfn>: defined in [[RML]] at <http://w3id.org/rml/core/spec/>.

Within this specification, the [=Expression Map=] definition is extended by adding new possible properties and thus also a new type of Expression Map.
The change is included below with changes highlighted in bold.

---

An [=Expression Map=] can have the following properties:

- 0 or 1 rml:constant
- 0 or 1 rml:reference
- 0 or 1 rml:template
- **0 or 1 rml:functionExecution**

---

### FNML

- A <dfn>Function-valued Expression Map</dfn>: an [=Expression Map=], where the generated term is one specific returned output (of an [=Execution=]).
  - This allows to reuse the same execution in different locations of the [=Triples Map=], and potentially use different outputs of the same execution.
  - It links to a [=Function Execution=] and a [=Return Map=].
- A <dfn>Return Map</dfn>: a [=Term Map=] that MUST generate a named node. That named node specifies the [=Return=] of the referenced [=Function=].
  - This can also be specified using a [=constant expression shortcut property=].
  - This can also be omitted, if so, the first return value as specified in the [=Function=] is used.
- A <dfn>Function Execution</dfn>: a construct that provides a way to bind concrete values to [=Parameter=]s of a [=Function=].
  The [=Function=] is specified using an [=Function Map=] and the [=Parameter=]s are specified using [=Input=]s.
  - As such, an Function Execution can be seen as a way to describe [=Execution=]s.
- An <dfn>Function Map</dfn>: a [=Term Map=] that MUST generate a named node. That named node specifies the referenced [=Function=].
  - This can also be specified using a [=constant expression shortcut property=].
- An <dfn>Input</dfn>: a construct to pairwise connect a value (via a [=Term Map=]) to a [=Parameter Map=].
  - This [=Term Map=] generates the input value that should be bound to the [=Parameter=] of the referenced [=Function=].
  - This [=Term Map=] refers to values from the [=Triples Map=]s iteration.
    Note that these [=Term Map=]s are handled just like regular [=Term Maps=] within a [=Triples Map=]:
    [The references of all Term Maps of a Triples Map (Subject Map, Predicate Maps, Object Maps, Graph Maps) must be references to records that exist in the Triples Map's logical source](http://w3id.org/rml/core/spec/).
- A <dfn>Parameter Map</dfn>: a [=Term Map=] that MUST generate a named node. That named node specifies the referenced [=Parameter=].
  - This can also be specified using a [=constant expression shortcut property=].

<p class="note" data-format="markdown">
It is currently assumed that a [=Function-valued Expression Map=] always returns an RDF term [[rdf-concepts]].
How a list of RDF terms is handled, is out of scope of this spec, but discussed at [[[CollectionsContainers]]].
</p>
