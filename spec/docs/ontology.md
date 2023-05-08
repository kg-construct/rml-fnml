## FNML

We use terms defined in the FNML ontology to link [[RML]] with [[FNO]].

The ontology namespace is [http://w3id.org/rml/](http://w3id.org/rml/),
the preferred prefix is `rml:`.
See below for how FNML introduced terms align with RML Core.

<figure id="figure-diagram">
  <img src="./diagrams/diagram.png" alt="FNML diagram" />
  <figcaption>Visual overview of how FNML introduced terms align with RML Core</figcaption>
</figure>

### Function-valued Expression Map

A [=Function-valued Expression Map=] is an [=Expression Map=] that is represented by a resource that has exactly one `rml:functionExecution`.
The value of the `rml:functionExecution` property must be a valid [=Execution=].

As a consequence, the default [[RML]] processing **is extended**,
specifically concerning the [default term type depending on whether the Term Map is an Object Map or not](https://w3id.org/rml/core/spec),
namely, the [=Function-valued Expression Map=]s default [term type](http://w3id.org/rml/core/spec) is `rml:Literal`.
The change is included below with changes highlighted in bold.

---

If the [=Term Map=] does not have a `rml:termType` property, then its [term type](http://w3id.org/rml/core/spec) is:
* `rml:Literal`, if it is an [Object Map](http://w3id.org/rml/core/) and at least one of the following conditions is true:
   * It is a [reference-valued Term Map](http://w3id.org/rml/core/spec),  **or a [=Function-valued Expression Map=]**
   * It has a `rml:languageMap` and/or `rml:language` property (and thus a [Language Map](http://w3id.org/rml/core/spec) and/or a [specified language tag](http://w3id.org/rml/core)).
   * It has a `rml:datatype` property (and thus a [specified datatype](http://w3id.org/rml/core/spec)).
* `rml:IRI`, otherwise.

---

A [=Function-valued Expression Map=] MUST have exactly one `rml:functionExecution` relation.
Further, it MAY have following relations specified:

* `rml:termType`: for processing, see paragraph above
* `rml:language` OR `rml:languageMap` OR `rml:datatype`: for processing, see [RML Language Tags](http://w3id.org/rml/core/spec/) and [RML Typed Literals](http://w3id.org/rml/core/spec/)
* `rml:return`: this relationship MUST refer to exactly one of the [=Return=]s as specified by the [=Function=]. This signifies which result of the execution to use. The default value is the first [=Return=] value as specified by the [=Function=].

<p class="issue" data-format="markdown">
A [proper term map definition in RML is pending](https://github.com/kg-construct/rml-core/issues/12).
For now, we refer to the R2RML spec, but it is assumed these references will be updated based on the evolution of RML.
This also means that all changes to existing definitions such as `term type` etc. are complementary to this specification.
</p>

### rml:ReturnMap

See [=Return map=].

### rml:FunctionExecution

See [=Function Execution=].

<!-- <dfn class="lint-ignore">rml:FunctionExecution</dfn> is a class to denote a [=Function Execution=].
It is referred from a [=rml:ExecutionTermMap=] via the predicate `rml:functionExecution`.
It refers to an FnO [=function description=] via the predicate `rml:function`,
and to zero or more input parameters via the predicate `rml:inputParameter`. -->

### rml:FunctionMap

See [=Function map=].

### rml:Input

See [=Input=].

### rml:ParameterMap

See [=Parameter map=].

### rml:functionExecution

Links [=function-valued expression map=] with [=Function Execution=].

Domain: rml:ExpressionMap

Range: rml:FunctionExecution

### rml:returnMap

Links [=function-valued expression map=] with [=Return map=].

Domain: rml:ExpressionMap

Range: rml:ReturnMap

#### rml:return

[=constant shortcut property=] of rml:returnMap.

### rml:functionMap

Links [=function-valued expression map=] with [=Function=].

Domain: rml:ExpressionMap

Range: fno:Function

#### rml:function

[=constant shortcut property=] of rml:functionMap.

### rml:input

Links [=Execution=] with [=Input=]s

### rml:parameterMap

Links [=Input=] with [=Parameter map=].

Domain: rml:Input

Range: rml:ParameterMap

#### rml:parameter

[=constant shortcut property=] of rml:parameterMap

### rml:inputValueMap

Links [=Input=] with a [=term map=].

Domain: rml:Input

Range: rml:TermMap

#### rml:inputValue

[=constant shortcut property=] of rml:inputValueMap

<div class="practice">

<span class="practicelab">Joining using data transformations</span>

<p class="practicedesc" data-format="markdown">When you specifically want to have join conditions, you should use functions within [rml:joinCondition](https://www.w3.org/TR/r2rml/#foreign-key),
see, e.g. test case [RMLFNOTC0019](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0019-CSV).
</p>
</div>
