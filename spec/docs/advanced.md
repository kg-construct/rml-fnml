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

```turtle "example": "use nested function"
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

### Conditions

Conditions are a shortcut to make RML documents more intuitive, but rely on existing FNML functionality.

```turtle "example": "use condition"
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
@prefix rml: <http://w3id.org/rml/> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap <#SubjectMap> ;
    rml:predicateObjectMap <#NameMapping> .

# Suggestion: add rml:condition predicate to expression map,
# and conforming mapping engines MUST support following functions:
# - isNull, isNotNull, equals, noEquals, IF
# (isNotNull and IF are defined below, rest is an excercise for the reader)
<#NameMapping>
    rml:predicate dbo:title ;
    # A condition can be defined in any expression map
    rml:objectMap [
        # new predicate that links to a function-valued expression map,
        # that function MUST return a boolean
        rml:condition [
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
        # The actual expression used if the condition returns TRUE
        rml:constant "true"
    ] .

# This is actually a shortcut to the following
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
                    rml:function fns:isNotNull ;
                    rml:input [
                        rml:parameter fns:parameter ;
                        rml:inputValueMap [
                            rml:reference "name"
                        ]
                    ]
                ]
            ] , [
                # = original expression
                rml:parameter fns:expressionParameter ;
                rml:inputValueMap [
                    rml:constant "true"
                ]
            ]
        ] ;
    ] .
# Any custom function can be used,
# or nested functions (eg AND/OR),
# depending on what the engines support
```
