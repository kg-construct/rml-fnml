## RML-FNML Vocabulary Definition {#fnml}

This section defines the classes, properties, and constraints of RML-FNML.

<figure id="figure-diagram">
  <img src="resources/diagram.png" alt="FNML diagram" />
  <figcaption>Visual overview of how FNML introduced terms align with RML-Core and FnO</figcaption>
</figure>

<div class="ednote" title="Diagram update">
<p>
This diagram needs to be updated to integrate <code>rml:condition</code> and Function-valued Expression Map. It also needs to reflect ongoing discussions regarding whether <code>rml:functionMap</code> and <code>rml:parameterMap</code> should be retained or removed.
</p>
</div>

### Function-valued Expression Map {#function-valued-expression-map}

A <dfn>Function-valued Expression Map</dfn> is an `rml:ExpressionMap` that generates values by executing an [[FnO]] function and capturing one of its declared return values.

A [=Function-valued Expression Map=] MUST have:
* exactly one `rml:functionExecution` property,
* zero or one `rml:returnMap` property (or `rml:return` shortcut property).

| Property | Domain | Range |
| :--- | :--- | :--- |
| `rml:functionExecution` | `rml:ExpressionMap` | `rml:FunctionExecution` |
| `rml:returnMap` | `rml:ExpressionMap` | `rml:ReturnMap` |
| `rml:return` | `rml:ExpressionMap` | `fno:Output` |

#### Return Map (`rml:ReturnMap`)

A <dfn>Return Map</dfn> (`rml:ReturnMap`) is a <a data-cite="RML-Core#dfn-term-map">Term Map</a> that MUST generate an IRI specifying the <a data-cite="FnO#dfn-output">output</a> of the referenced <a data-cite="FnO#dfn-function-declaration">function</a>.
The property `rml:return` is the <a data-cite="RML-Core#dfn-constant-shortcut-properties">constant shortcut property</a> of `rml:returnMap`.

<p class="note" title="Return Map Reference Target">
A Return Map (or its <code>rml:return</code> shortcut) refers to the <code>fno:Output</code> instance (such as <code>grel:stringOut</code>), rather than the <code>fno:predicate</code> property IRI (such as <code>grel:stringOutput</code>).
</p>

If `rml:returnMap` and `rml:return` are omitted, the first return value declared in the `fno:returns` list of the referenced <a data-cite="FnO#dfn-function-declaration">function</a> is used by default.

<p class="note">
It is currently assumed that a [=Function-valued Expression Map=] always returns a single RDF term [[[rdf11-concepts]]]. Handling collections or containers of RDF terms is out of scope of this specification, but is specified in [[[RML-CC]]].
</p>

### Conditional Expressions (`rml:condition`) {#conditions}

An `rml:ExpressionMap` MAY specify an <dfn>rml:condition</dfn> property to conditionally govern whether RDF terms are generated during mapping evaluation.

<div class="ednote" title="Alternative: Conditioned Expression Map">
<p>
As an alternative to adding <code>rml:condition</code> directly to <code>rml:ExpressionMap</code>, an explicit subclass of expression map (e.g., <code>rml:ConditionedExpressionMap</code>) could be defined to represent expression maps that specify conditional evaluation.
</p>
</div>

| Property | Domain | Range |
| :--- | :--- | :--- |
| `rml:condition` | `rml:ExpressionMap` | `rml:ExpressionMap` |

* The value of `rml:condition` MUST be an `rml:ExpressionMap`.
* The evaluated condition MUST return an `xsd:boolean` value.

#### Evaluation Semantics

During the evaluation of an expression map for a logical iteration:
1. The condition expression map is evaluated first.
2. If the condition evaluates to `true` (`"true"^^xsd:boolean`), the expression map proceeds with its normal evaluation and term generation.
3. If the condition evaluates to `false` (`"false"^^xsd:boolean`), evaluates to `null`, or produces an error, the expression map generates no value for that iteration, and term generation is omitted.

The `rml:condition` property is functionally equivalent to wrapping the expression map in a ternary conditional function execution (`rml-fn:IF`).

An expression map specifying `rml:condition`:
```turtle
[
    rml:condition [
        rml:functionExecution <#ConditionExecution> ;
        rml:return rml-fn:boolOut
    ] ;
    rml:constant "[Default Title]"
]
```

is equivalent to:
```turtle
[
    rml:functionExecution [
        rml:function rml-fn:IF ;
        rml:input [
            rml:parameter rml-fn:boolParam ;
            rml:inputValueMap [
                rml:functionExecution <#ConditionExecution> ;
                rml:return rml-fn:boolOut
            ]
        ] , [
            rml:parameter rml-fn:expressionParam ;
            rml:inputValue "[Default Title]"
        ]
    ]
]
```

### Function Execution (`rml:FunctionExecution`) {#function-execution}

A <dfn>Function Execution</dfn> (`rml:FunctionExecution`) is a construct that represents an invocation of an [[FnO]] <a data-cite="FnO#dfn-function-declaration">function</a>.
It binds concrete values to the function's <a data-cite="FnO#dfn-parameter">parameters</a> via [=Input=]s, and specifies the target function to execute via a [=Function Map=].

* An `rml:FunctionExecution` MUST have exactly one [=Function Map=] specified via the `rml:functionMap` property, or via the `rml:function` shortcut property.
* An `rml:FunctionExecution` MAY have zero or more [=Input=] properties specified via the `rml:input` property.

| Property | Domain | Range |
| :--- | :--- | :--- |
| `rml:functionMap` | `rml:FunctionExecution` | `rml:FunctionMap` |
| `rml:function` | `rml:FunctionExecution` | `fno:Function` |
| `rml:input` | `rml:FunctionExecution` | `rml:Input` |

A <dfn>Function Map</dfn> (`rml:FunctionMap`) is a <a data-cite="RML-Core#dfn-term-map">Term Map</a> that MUST generate an IRI. That IRI specifies the referenced [[FnO]] <a data-cite="FnO#dfn-function-declaration">function</a>.
The property `rml:function` is the <a data-cite="RML-Core#dfn-constant-shortcut-properties">constant shortcut property</a> of `rml:functionMap`.

#### Execution Reuse

An `rml:FunctionExecution` can be identified by an IRI or a blank node:

* **Named Execution (IRI)**: When an `rml:FunctionExecution` is identified by an IRI, it represents a shared function execution. Multiple expression maps (or multiple triples maps) can reference the same execution IRI, allowing the results of an execution to be reused across different locations for a given logical iteration.
* **Anonymous Execution (Blank Node)**: When identified by a blank node, the execution is specific to its enclosing expression map and is not shared across other expression maps.

See [Function Execution Reuse](#execution-reuse) for an example illustrating how a shared execution is used across multiple expression maps.

<div class="ednote">
<p>
<strong>TODO:</strong> Clarify processor execution reuse semantics (e.g., whether conforming processors MUST evaluate an execution once per iteration or whether it serves as an optimization hint).
</p>
</div>

#### Dynamic Function Selection (`rml:functionMap`)

When the target function is constant, the shortcut property `rml:function` is used. Alternatively, an explicit `rml:functionMap` allows the target function IRI to be determined dynamically per logical iteration from data values in the logical source (e.g., dynamically selecting a parsing, hashing, or conversion function based on a data field).

<div class="ednote" title="Issue #84: Dynamic Function Selection">
<p>
We invite user feedback on <a href="https://github.com/kg-construct/rml-fnml/issues/84">Issue #84</a> to share concrete use cases for dynamic function selection and help determine requirement levels (such as SHOULD, MUST, or optional provision).
</p>
</div>

### Inputs and Parameter Mapping (`rml:Input`) {#inputs}

An <dfn>Input</dfn> (`rml:Input`) is a construct that provides a pairwise connection between a [[FnO]] <a data-cite="FnO#dfn-parameter">parameter</a> and an input value generated from the logical iteration.

* An `rml:Input` MUST have exactly one [=Parameter Map=] specified via the `rml:parameterMap` property, or via the `rml:parameter` shortcut property.
* An `rml:Input` MUST have exactly one input value map specified via the `rml:inputValueMap` property, or via the `rml:inputValue` shortcut property.

| Property | Domain | Range |
| :--- | :--- | :--- |
| `rml:parameterMap` | `rml:Input` | `rml:ParameterMap` |
| `rml:parameter` | `rml:Input` | `fno:Parameter` |
| `rml:inputValueMap` | `rml:Input` | `rml:TermMap` |
| `rml:inputValue` | `rml:Input` | `rdfs:Resource` |

A <dfn>Parameter Map</dfn> (`rml:ParameterMap`) is a <a data-cite="RML-Core#dfn-term-map">Term Map</a> that MUST generate an IRI. That IRI specifies the referenced [[FnO]] <a data-cite="FnO#dfn-parameter">parameter</a>.
The property `rml:parameter` is the <a data-cite="RML-Core#dfn-constant-shortcut-properties">constant shortcut property</a> of `rml:parameterMap`.

<p class="note" title="Parameter Map Reference Target">
A Parameter Map (or its <code>rml:parameter</code> shortcut) refers to the <code>fno:Parameter</code> instance (such as <code>grel:valueParam</code>), rather than the <code>fno:predicate</code> property IRI (such as <code>grel:valueParameter</code>).
</p>

#### Dynamic Parameter Mapping (`rml:parameterMap`)

When the target parameter is constant, the shortcut property `rml:parameter` is used. Alternatively, an explicit `rml:ParameterMap` allows the target parameter IRI to be determined dynamically per logical iteration from data values in the logical source (e.g., when binding parameters dynamically for key-value structures or dynamic attributes).

<div class="ednote" title="Issue #84: Dynamic Parameter Mapping">
<p>
We invite user feedback on <a href="https://github.com/kg-construct/rml-fnml/issues/84">Issue #84</a> to share concrete use cases for dynamic parameter mapping and help determine requirement levels.
</p>
</div>

#### Input Value Mapping (`rml:inputValueMap`)

The property `rml:inputValueMap` links an `rml:Input` to a <a data-cite="RML-Core#dfn-term-map">Term Map</a> that generates the value to be bound to the referenced <a data-cite="FnO#dfn-parameter">parameter</a>.
This <a data-cite="RML-Core#dfn-term-map">Term Map</a> refers to values from the iteration of the enclosing triples map's logical source, handled just like any regular <a data-cite="RML-Core#dfn-term-map">Term Map</a> (e.g. using `rml:reference`, `rml:template`, or nested `rml:functionExecution`).
The property `rml:inputValue` is the <a data-cite="RML-Core#dfn-constant-shortcut-properties">constant shortcut property</a> of `rml:inputValueMap`.

### Complete Mapping Example

The following example shows an object map that executes `grel:toUppercase` on the `name` reference, capturing the `grel:stringOut` return, and using `rml:condition` to only generate terms when `name` is not null:

<aside class="example" id="example-complete-mapping" title="Function-valued Expression Map with Condition">
<aside class="ex-mapping">

```turtle
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap [
        rml:template "http://example.com/person/{id}"
    ] ;
    rml:predicateObjectMap [
        rml:predicate ex:title ;
        rml:objectMap [
            # Function-valued Expression Map
            rml:functionExecution <#UppercaseExecution> ;
            rml:return grel:stringOut ;
            # Condition shortcut: only generate when name is not null
            rml:condition [
                rml:functionExecution [
                    rml:function rml-fn:isNotNull ;
                    rml:input [
                        rml:parameter rml-fn:param ;
                        rml:inputValueMap [ rml:reference "name" ]
                    ]
                ] ;
                rml:return rml-fn:boolOut
            ]
        ]
    ] .

<#UppercaseExecution> a rml:FunctionExecution ;
    rml:function grel:toUppercase ;
    rml:input [
        a rml:Input ;
        rml:parameter grel:valueParam ;
        rml:inputValueMap [ rml:reference "name" ]
    ] .
```

</aside>
</aside>
