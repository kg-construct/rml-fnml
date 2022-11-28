## Advanced usage

### Nested functions

As the values of a function are represented using [=term map=]s,
it is possible to nest functions: you generate a term in a first function, and that term is used as an parameter value in a second function.

<p class="issue" data-format="markdown">
For an old example, see [RMLFNOTC0018](https://github.com/RMLio/rml-fno-test-cases/tree/master/RMLFNOTC0018-CSV).
</p>

<p class="issue" data-number="3" data-format="markdown">
For now, it is unclear how to handle a nested function where that nested triplesmap contains a join condition.
</p>

```turtle "example": "use nested function"
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix fnml: <http://semweb.mmlab.be/ns/fnml#> .
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
        fnml:execution <#Execution> ;
        fnml:output grel:stringOut
    ] ;
    .

<#Execution> a fnml:Execution ;
    fnml:function grel:toUppercase ;
    fnml:input
        [
            a fnml:Input ;
            fnml:parameter grel:valueParam ;
            fnml:valueMap [
                fnml:execution <#Execution2> ; # Link to another function-valued term map to nest functions
                fnml:output grel:stringOut
            ]
        ] .

<#Execution2> a fnml:Execution ;               # First, replace spaces with dashes from the `name` reference
    fnml:function grel:string_replace ;
    fnml:input
        [
            a fnml:Input ;
            fnml:parameter grel:valueParam ;
            fnml:valueMap [
                rml:reference "name"
            ]
        ] ,
        [
            a fnml:Input ;
            fnml:input grel:param_find ;
            fnml:value " "
        ] ,
        [
            a fnml:Input ;
            fnml:input grel:param_replace  ;
            fnml:value "-"
        ] .
```
