## Advanced usage

### Nested functions

As the values of a function are represented using [=Expression Map=]s,
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.

<p class="issue" data-format="markdown">
For an old example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).
</p>

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested Triples Map contains a join condition.
</p>

<aside class="example" id="example-nested-function" title="usage of nested function">
<aside class="ex-mapping">

```turtle
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
@prefix rml: <http://w3id.org/rml/> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap <#SubjectMap> ;
    rml:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rml:predicate dbo:title ;
    rml:objectMap [
        rml:functionExecution <#Execution> ;
        rml:return grel:stringOut
    ] ;
    .

<#Execution> a rml:FunctionExecution ;
    rml:function grel:toUppercase ;
    rml:input
        [
            a rml:Input ;
            rml:parameter grel:valueParam ;
            rml:InputValueMap [
                rml:functionExecution <#Execution2> ; # Link to another function-valued expression map to nest functions
                rml:return grel:stringOut
            ]
        ] .

<#Execution2> a rml:FunctionExecution ;               # First, replace spaces with dashes from the `name` reference
    rml:function grel:string_replace ;
    rml:input
        [
            a rml:Input ;
            rml:parameter grel:valueParam ;
            rml:InputValueMap [
                rml:reference "name"
            ]
        ] ,
        [
            a rml:Input ;
            rml:parameter grel:param_find ;
            rml:inputValue " "
        ] ,
        [
            a rml:Input ;
            rml:parameter grel:param_replace  ;
            rml:inputValue "-"
        ] .
```

</aside>
</aside>

### Conditions

Conditions are a shortcut to make RML mappings more intuitive, but rely on existing FNML functionality.
It is a shortcut that is applied using the `rml:condition`: an additional ExpressionMap predicate.
To be able to use this shortcut, conforming mapping engines MUST support following functions:

- isNull
- isNotNull
- equals
- noEquals
- IF

<p class="note" title="Condition function definitions">
  isNotNull and IF are defined below, rest is an excercise for the reader.
  The actual FnO definitions are TODO.
</p>

<aside class="example" id="example-condition" title="usage of condition">
<aside class="ex-mapping">

```turtle
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix fns: <http://example.com/fns#> .
@prefix rml: <http://w3id.org/rml/> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap <#SubjectMap> ;
    rml:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rml:predicate dbo:title ;
    # A condition can be defined in any expression map
    rml:objectMap [
        # new predicate that links to a function-valued expression map,
        # that function MUST return a boolean
        rml:condition [
            rml:functionExecution [
                # isNotNull(parameter: X) / definition: X != NULL ? TRUE : FALSE ;
                rml:function fns:isNotNull ;
                rml:input [
                    # The parameter that is checked for NULL
                    rml:parameter fns:parameter ;
                    rml:inputValueMap [
                        rml:reference "name"
                    ]
                ]
            ] ;
            rml:return fns:boolOut # if fno:boolOut is the first specified return, this triple can be ommitted.
        ] ;
        # The actual expression used if the condition returns TRUE
        rml:constant "[a filled in title]"
    ] .
```
</aside>

This is actually a shortcut to the following

<aside class="ex-mapping">

```turtle
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix fns: <http://example.com/fns#> .
@prefix rml: <http://w3id.org/rml/> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap <#SubjectMap> ;
    rml:predicateObjectMap <#NameMappingExtended> .

<#NameMappingExtended>
    rml:predicate dbo:title ;
    rml:objectMap [
        rml:functionExecution [
            # IF(bool: X, expression: Y)
            # Function definition: X === TRUE ? Y : NULL
            rml:function fns:IF ;
            rml:input [
                # = original condition function
                rml:parameter fns:boolParameter ;
                rml:inputValueMap [
                    rml:functionExecution [
                        rml:function fns:isNotNull ;
                        rml:input [
                            rml:parameter fns:parameter ;
                            rml:inputValueMap [
                                rml:reference "name"
                            ]
                        ]
                    ]
                ]
            ] , [
                # = original expression
                rml:parameter fns:expressionParameter ;
                rml:inputValueMap [
                    rml:constant "[a filled in title]"
                ]
            ]
        ] ;
    ] .
# Any custom function can be used,
# or nested functions (eg AND/OR),
# depending on what the engines support
```

</aside>
</aside>
