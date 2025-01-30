## RMLFNOTC0010-CSV

**Title**: Function on object, wrong type parameter

**Description**: Tests a function with a wrong type parameter cannot be used

**Error expected?** No

**Input**
```
Id,Name,Comment,Class,url
1,Venus,A&B,A,http://example.com/venus

```

**Mapping**
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.com/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rml: <http://w3id.org/rml/> .
@prefix fno: <https://w3id.org/function/ontology#> .
@prefix fns: <http://example.com/functions/> .
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
        rml:predicate foaf:name;
        rml:objectMap [
            rml:functionExecution <#Execution> ;
            rml:returnMap [
                rml:constant fns:domainOutput
            ]
        ]
    ] .

<#Execution>
    rml:function fns:parseURL ;
    rml:input
        [
            rml:parameter fns:stringParameter ;
            rml:inputValueMap [
                rml:reference "url" ;
            ]
        ] .

```

**Output**
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "example.com" .

```

