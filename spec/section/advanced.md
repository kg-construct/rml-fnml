## Advanced Usage & Patterns {#advanced}

This section illustrates advanced usage patterns combining function executions with execution reuse, nested expressions, multi-valued iterations, and join conditions.

### Function Execution Reuse {#execution-reuse}

When a function produces multiple outputs, or when an expensive transformation must be shared across different mapping rules, identifying the `rml:FunctionExecution` with an IRI enables execution reuse across different locations in an RML mapping.

<div class="ednote">
<p>
<strong>TODO:</strong> Clarify processor execution reuse semantics (e.g., whether conforming processors MUST evaluate an execution once per iteration or whether it serves as an optimization hint).
</p>
</div>

The following example uses a shared execution `<#AddressExecution>` that parses a combined address field into separate street and city components, using the results across two distinct predicate-object maps:

<aside class="example" id="example-execution-reuse" title="Reusing a Function Execution across multiple outputs">
<aside class="ex-mapping">

```turtle
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap [
        rml:template "http://example.com/person/{id}"
    ] ;
    # First output: street
    rml:predicateObjectMap [
        rml:predicate ex:street ;
        rml:objectMap [
            rml:functionExecution <#AddressExecution> ;
            rml:return ex:streetOut
        ]
    ] ;
    # Second output: city
    rml:predicateObjectMap [
        rml:predicate ex:city ;
        rml:objectMap [
            rml:functionExecution <#AddressExecution> ;
            rml:return ex:cityOut
        ]
    ] .

# Shared execution identified by an IRI
<#AddressExecution> a rml:FunctionExecution ;
    rml:function ex:parseAddress ;
    rml:input [
        a rml:Input ;
        rml:parameter ex:addressParam ;
        rml:inputValueMap [
            rml:reference "fullAddress"
        ]
    ] .
```

</aside>
</aside>

Because `<#AddressExecution>` is named with an IRI, the `ex:parseAddress` function is executed only once per record iteration. Both `ex:streetOut` and `ex:cityOut` are retrieved from that single invocation, preventing redundant parsing and ensuring consistency.

### Nested Functions

As parameter input values are represented using <a data-cite="RML-Core#dfn-term-map">Term Maps</a>, functions can be arbitrarily nested: the output of one function execution serves as the input parameter to another function execution.

<aside class="example" id="example-nested-function" title="Nested Function Executions">
<aside class="ex-mapping">

```turtle
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap <#SubjectMap> ;
    rml:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rml:predicate ex:title ;
    rml:objectMap [
        # Outer function: toUppercase
        rml:functionExecution <#UppercaseExecution> ;
        rml:return grel:stringOut
    ] .

<#UppercaseExecution> a rml:FunctionExecution ;
    rml:function grel:toUppercase ;
    rml:input [
        a rml:Input ;
        rml:parameter grel:valueParam ;
        # Inner function: replace spaces with dashes
        rml:inputValueMap [
            rml:functionExecution <#ReplaceExecution> ;
            rml:return grel:stringOut
        ]
    ] .

<#ReplaceExecution> a rml:FunctionExecution ;
    rml:function grel:string_replace ;
    rml:input [
        a rml:Input ;
        rml:parameter grel:valueParam ;
        rml:inputValueMap [ rml:reference "name" ]
    ] , [
        a rml:Input ;
        rml:parameter grel:param_find ;
        rml:inputValue " "
    ] , [
        a rml:Input ;
        rml:parameter grel:param_replace ;
        rml:inputValue "-"
    ] .
```

</aside>
</aside>

### Multi-value Processing

Aligned with the other RML specifications, when an input expression yields multiple values for a single logical iteration, the function execution is evaluated for each value in sequence:

If an input expression yields `"a"`, `"b"`, and `"c"`, the function execution is evaluated against each individual item in that order, producing corresponding outputs for each item.

### Multi-value Conditions

Conditions can also evaluate over multi-valued expression results. Consider the following input record:

<aside class="ex-input">

```json
[
  {
    "id": "item1",
    "scores": [10, 0, 25]
  }
]
```

</aside>

The mapping applies an `rml:condition` checking that each score is not equal to `0`:

<aside class="example" id="example-condition-multivalue" title="Conditional Filtering on Multi-values">
<aside class="ex-mapping">

```turtle
<#Score_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap [ rml:template "http://example.com/item/{id}" ] ;
    rml:predicateObjectMap [
        rml:predicate ex:validScore ;
        rml:objectMap [
            rml:reference "scores" ;
            rml:condition [
                rml:functionExecution [
                    rml:function rml-fn:notEquals ;
                    rml:input [
                        rml:parameter rml-fn:param ;
                        rml:inputValueMap [ rml:reference "scores" ]
                    ] , [
                        rml:parameter rml-fn:compared ;
                        rml:inputValue "0"
                    ]
                ] ;
                rml:return rml-fn:boolOut
            ]
        ]
    ] .
```

</aside>
</aside>

Because only two values (`10` and `25`) satisfy the condition `score != 0`, only two triples are emitted for that iteration:

<aside class="ex-output">

```turtle
<http://example.com/item/item1> ex:validScore "10" .
<http://example.com/item/item1> ex:validScore "25" .
```

</aside>

### Joining Using Data Transformations

When performing joins across heterogeneous data sources where foreign keys do not share identical literal representations (e.g. inconsistent case, differing encodings, or extraneous prefixes), function executions can be applied within <a data-cite="RML-Core#dfn-join-condition">join conditions</a>.

Because a child map (`rml:childMap`) and parent map (`rml:parentMap`) are defined in [[RML-Core]] as <a data-cite="RML-Core#dfn-expression-map">expression maps</a>, either can be specified as a [=Function-valued Expression Map=].

The following example joins student records with their enrolled courses. In the child data source, the course identifier is stored in lowercase (e.g. `"cs101"`), whereas the parent data source stores course codes in uppercase (`"CS101"`). The join condition specifies an `rml:childMap` that executes `grel:toUppercase` on the child reference to match the parent `code`:

<aside class="example" id="example-join-transformation" title="Joining with a Function-valued Child Map">
<aside class="ex-mapping">

```turtle
<#Student_Mapping>
    rml:logicalSource <#StudentsSource> ;
    rml:subjectMap [ rml:template "http://example.com/student/{id}" ] ;
    rml:predicateObjectMap [
        rml:predicate ex:enrolledIn ;
        rml:objectMap [
            rml:parentTriplesMap <#Course_Mapping> ;
            rml:joinCondition [
                # Child map transforms lowercase 'course_code' to uppercase to match parent 'code'
                rml:childMap [
                    rml:functionExecution [
                        rml:function grel:toUppercase ;
                        rml:input [
                            rml:parameter grel:valueParam ;
                            rml:inputValueMap [ rml:reference "course_code" ]
                        ]
                    ] ;
                    rml:return grel:stringOut
                ] ;
                rml:parent "code"
            ]
        ]
    ] .

<#Course_Mapping>
    rml:logicalSource <#CoursesSource> ;
    rml:subjectMap [ rml:template "http://example.com/course/{code}" ] .
```

</aside>
</aside>
