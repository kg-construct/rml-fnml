## RMLFNOTC0004-CSV

**Title**: Function on object, 1 reference parameter, 1 constant parameter

**Description**: Tests if a function with multiple parameters can be used

**Error expected?** No

**Input**
```
Id,Name,Comment,Class
1,Venus,A&B,A

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

<TriplesMap1>
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
    rml:predicateObjectMap [
        rml:predicateMap [
            rml:functionExecution <#Execution> ;
        ];
        rml:object foaf:name;
    ] .

<#Execution>
    rml:function idlab-fn:toUpperCaseURL ;
    rml:input
        [
            rml:parameter idlab-fn:str ;
            rml:inputValueMap [
                rml:reference "Name"
            ];
        ] .

```

**Output**
```
<http://example.com/Venus> <http://VENUS> <http://xmlns.com/foaf/0.1/name> .

```

