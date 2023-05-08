## Advanced usage

### Nested functions

As the values of a function are represented using [=expression map=]s,
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.

<p class="issue" data-format="markdown">
For an old example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).
</p>

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested triplesmap contains a join condition.
</p>

```turtle "example": "use nested function"
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rr:subjectMap <#SubjectMap> ;
    rr:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rr:predicate dbo:title ;
    rr:objectMap [
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
