## RMLFNOTC0009-CSV

**Title**: Function on object, 1 constant parameter

**Description**: Tests if a constant parameter can be used

**Error expected?** No

**Input**
```
Id,Name,Comment,Class
1,M Venus,A&B,A

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.com/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rml: <http://w3id.org/rml/> .
@prefix fno: <https://w3id.org/function/ontology#> .
@prefix morph-kgc: <https://github.com/morph-kgc/morph-kgc/function/built-in.ttl#> .
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
@prefix idlab-fn: <http://example.com/idlab/function/> .

@base <http://example.com/base/> .

<#Person_Mapping>
    rml:logicalSource [
        rml:source [ a rml:RelativePathSource;
          rml:root rml:MappingDirectory;
          rml:path "student.csv"
        ];
        rml:referenceFormulation rml:CSV
    ];
    rml:subjectMap [
        rml:template "http://example.com/{Name}"
    ];
    rml:predicateObjectMap <#NameMapping> .

<#NameMapping>
    rml:predicate foaf:name ;
    rml:objectMap [
        rml:functionExecution <#Execution> ;
    ]; .

<#Execution> a rml:FunctionExecution ;
    rml:function grel:toUpperCase ;
    rml:input
        [
            a rml:Input ;
            rml:parameter grel:valueParam ;
            rml:inputValueMap [
                rml:functionExecution <#Execution2> ;
                rml:return grel:stringOut
            ]
        ] .

<#Execution2> a rml:Execution ;
    rml:function grel:string_replace ;
    rml:input
        [
            a rml:Input ;
            rml:parameter grel:valueParam ;
            rml:inputValueMap [
                rml:reference "Name"
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

**Output**
```
<http://example.com/M%20Venus> <http://xmlns.com/foaf/0.1/name> "M-VENUS" .

```

