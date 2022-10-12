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

- An <dfn>RML mapping</dfn>: defined in [[RML]] at <https://rml.io/specs/rml/#rml-mapping>.
- A <dfn>Triples map</dfn>: defined in [[RML]] at <https://rml.io/specs/rml/#triples-map>.
- A <dfn>Term map</dfn>: defined in [[RML]] at <https://rml.io/specs/rml/#term-map>.
<!-- - An <dfn>RML processor</dfn> is a tool that interprets the <a>RML mapping</a> and executes its rules to generate RDF triples. -->
- A <dfn>constant shortcut property</dfn>: defined in [[R2RML]] at <https://www.w3.org/TR/r2rml/#dfn-constant-shortcut-property>

### FNML

- An <dfn>Output Term map</dfn>: a [=Term map=], where the generated term is one specific output (of an [=Execution=]).
  - This allows to reuse the same execution in different locations of the [=Triples map=], and potentially use different outputs of the same execution.
  - It links to an [=FNML Execution=] and a [=FNML Return map=].
- A <dfn>FNML Return map</dfn>: a [=Term map=] that MUST generate a named node. That named node specifies the [=Return=] of the referenced [=Function=].
  - This can also be specified using a [=constant shortcut property=].
  - This can also be omitted, if so, the first return value as specified in the [=Function=] is used.
- An <dfn>FNML Execution</dfn>: a construct that provides a way to bind concrete values to [=Parameter=]s of a [=Function=].
  The [=Function=] is specified using an [=FNML Function map=] and the [=Parameter=]s are specified using [=FNML Input=]s.
  - As such, an FNML Execution can be seen as a way to describe [=Execution=]s.
- An <dfn>FNML Function map</dfn>: a [=Term map=] that MUST generate a named node. That named node specifies the referenced [=Function=].
  - This can also be specified using a [=constant shortcut property=].
- An <dfn>FNML Input</dfn>: a construct to pairwise connect a value (via a [=Term map=]) to a [=FNML Parameter map=].
  - This [=Term map=] generates the input value that should be bound to the [=Parameter=] of the referenced [=Function=].
  - This [=Term map=] refers to values from the [=Triples map=]s iteration.
    Note that these [=Term map=]s are handled just like regular [=Term maps=] within a [=Triples map=]:
    [The references of all term maps of a triples map (subject map, predicate maps, object maps, graph maps) must be references to rows/records/elements/objects that exist in the triples map's logical source](https://rml.io/specs/rml/#mapping-logical-sources).
- An <dfn>FNML Parameter map</dfn>: a [=Term map=] that MUST generate a named node. That named node specifies the referenced [=Parameter=].
  - This can also be specified using a [=constant shortcut property=].

<p class="note" data-format="markdown">
It is currently assumed that an [=Output Term map=] always returns an RDF term [[rdf-concepts]].
How a list of RDF terms is handled, is out of scope of this spec, but discussed at [[[CollectionsContainers]]].
</p>
