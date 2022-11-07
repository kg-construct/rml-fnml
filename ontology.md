## FNML

We use terms defined in the FNML ontology to link [[RML]] with [[FNO]].

The ontology namespace is [http://semweb.mmlab.be/ns/fnml#](http://semweb.mmlab.be/ns/fnml#),
the preferred prefix is `fnml:`.

### fnml:OutputTermMap

See [=Output Term map=].

`fnml:OutputTermMap` is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap).
<!-- to denote that this [=Term map=] is also an [=execution term map=]. -->
<!-- Specifically, this means that, when an [=execution term map=] is used within an <a>RML mapping</a>, -->
<!-- this [=Term map=] has two classes: `fnml:OutputTermMap`, and the [=Term map=] within the context of the RML Mapping, -->
<!-- namely, subject map, predicate map, object map, or graph map. -->
As a consequence, the default [[RML]] processing **is extended**,
specifically concerning the [default term type depending on whether the term map is an object map or not](https://rml.io/specs/rml/#termtype),
namely, the [=Output Term map=]s default [term type](https://rml.io/specs/rml/#term-type) is `rr:Literal`.

If the [=Term map=] does not have a `rr:termType` property, then its [term type](https://rml.io/specs/rml/#term-type) is:
* `rr:Literal`, if it is an [object map](https://www.w3.org/TR/r2rml/#dfn-object-map) and at least one of the following conditions is true:
   * It is a [reference-based term map](https://rml.io/specs/rml/#reference-valued-term-map),  **or an [=Output Term map=]**
   * It has a `rml:languageMap` and/or `rr:language` property (and thus a [language map](https://rml.io/specs/rml/#language-map) and/or a [specified language tag](https://rml.io/specs/rml/#specified-language-tag)).
   * It has a `rr:datatype` property (and thus a [specified datatype](https://rml.io/specs/rml/#specified-datatype)).
* `rr:IRI`, otherwise.

An `fnml:OutputTermMap` MUST have exactly one `fnml:execution` relation.
Further, it MAY have following relations specified:

* `rr:termType`: for processing, see paragraph above
* `rr:language` OR `rml:languageMap` OR `rr:datatype`: for processing, see [RML Language Tags](https://rml.io/specs/rml/#language-tag) and [RML Typed Literals](https://rml.io/specs/rml/#typed-literals)
* `fnml:output`: this relationship MUST refer to exactly one of the [=Return=]s as specified by the [=Function=]. This signifies which result of the execution to use. The default value is the first [=Return=] value as specified by the [=Function=].

<p class="issue" data-format="markdown">
A [proper Term map definition in RML is pending](https://github.com/kg-construct/rml-core/issues/12).
For now, we refer to the R2RML spec, but it is assumed these references will be updated based on the evolution of RML.
This also means that all changes to existing definitions such as `term type` etc. are complementary to this specification.
</p>

### fnml:ReturnMap

See [=FNML Return map=].

### fnml:Execution

See [=FNML Execution=].

<!-- <dfn class="lint-ignore">fnml:Execution</dfn> is a class to denote an [=FnML execution=].
It is referred from a [=fnml:ExecutionTermMap=] via the predicate `fnml:execution`.
It refers to an FnO [=function description=] via the predicate `fnml:function`,
and to zero or more input parameters via the predicate `fnml:inputParameter`. -->

### fnml:FunctionMap

See [=FNML Function map=].

### fnml:Input

See [=FNML Input=].

### fnml:ParameterMap

See [=FNML Parameter map=].

<!-- <dfn>fnml:ParameterMap</dfn> is a subclass of [rr:TermMap](http://www.w3.org/ns/r2rml#TermMap).
All default [[RML]] processing holds,
**with the same extension as with the [=fnml:ExecutionTermMap=]**. -->

### fnml:execution

Links [=Output Term map=] with [=FNML Execution=].

Domain: fnml:OutputTermMap

Range: fnml:Execution

<!-- fnml:execution connects the RDF dataset generating triples map via a [fnml:ExecutionTermMap] with a [=fnml:Execution=].
It has domain [=fnml:ExecutionTermMap=] and range [=fnml:Execution=]. -->

### fnml:outputMap

Links [=Output Term map=] with [=FNML Return map=].

Domain: fnml:OutputTermMap

Range: fnml:ReturnMap

#### fnml:output

[=constant shortcut property=] of fnml:outputMap.

<!-- <dfn class="lint-ignore">fnml:output</dfn> connects the RDF dataset generating triples map via a [fnml:ExecutionTermMap] with an output predicate.
It has domain [=fnml:ExecutionTermMap=]. -->

### fnml:functionMap

Links [=Output Term map=] with [=Function=].

Domain: fnml:OutputTermMap

Range: fno:Function

#### fnml:function

[=constant shortcut property=] of fnml:functionMap.

<!-- <dfn class="lint-ignore">fnml:function</dfn> connects the [fnml:Execution] with an FnO [=function description=].
It has domain [=fnml:Execution=] and range [fno:Function](https://w3id.org/function/ontology#Function). -->

### fnml:input

Links [=FNML Execution=] with [=FNML Input=]s

<!-- <dfn class="lint-ignore">fnml:inputParameter</dfn> connects the [fnml:Execution] with zero or more [=fnml:ParameterMap=]s.
It has domain [=fnml:Execution=] and range [=fnml:ParameterMap=]. -->

### fnml:parameterMap

Links [=FNML Input=] with [=FNML Parameter map=].

Domain: fnml:Input

Range: fnml:ParameterMap

<!-- <dfn class="lint-ignore">fnml:input</dfn> connects the [=fnml:ParameterMap=] with a function input parameter predicate.
It has domain [=fnml:ParameterMap=]. -->

#### fnml:parameter

[=constant shortcut property=] of fnml:parameterMap

### fnml:valueMap

Links [=FNML Input=] with a [=Term map=].

Domain: fnml:Input

Range: rr:TermMap

#### fnml:value

[=constant shortcut property=] of fnml:valueMap

<!-- <dfn class="lint-ignore">fnml:inputValue</dfn> connects the [=fnml:ParameterMap=] with a function input value.
This value is generated using [=term map=]s.
It has domain [=fnml:ParameterMap=] and range [=term map=]. -->

<!-- #### Logical source

The logical source is the same as the logical source of the triples map that refers to the [=fnml:Execution=].
It is thus passed on from the triples map over the [=fnml:Execution=] to the [=fnml:ParameterMap=].
An [=fnml:Execution=] or [=fnml:ParameterMap=] can be reused across triple maps, however,
the logical source is determined at runtime and thus is always a single logical source, namely, the one specified by the triples map that is cuurently being processed.
An engine needs to take into account which triples map is currently processed, to know which logical source's iterations to use for an [=fnml:Execution=] or [=fnml:ParameterMap=].

<p class="issue" data-format="markdown">
The assumption is that this handling of a logical source is the same behavior as, e.g., a term map definition that is being reused across triples maps, however, that doesn't seem to be clearly specified in the [currently R2RML specification](https://www.w3.org/2001/sw/rdb2rdf/r2rml/#dfn-triples-map)
</p>

<p class="issue" data-format="markdown">
For an old example on joining values across data sources, without join conditions, see test case [RMLFNOTC009](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0009-CSV).
</p>

<p class="issue" data-number="2" data-format="markdown">
It is still an open issue to joining values across data sources _with_ join conditions
</p> -->

<div class="practice">

<span class="practicelab">Joining using data transformations</span>

<p class="practicedesc" data-format="markdown">When you specifically want to have join conditions, you should use functions within [rr:joinCondition](https://www.w3.org/TR/r2rml/#foreign-key),
see, e.g. test case [RMLFNOTC0019](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0019-CSV).
</p>
</div>

<p class="issue" data-number="4" data-format="markdown">
The mapping challenge [Join on literals](https://github.com/kg-construct/mapping-challenges/pull/29) also influences this spec.
</p>
