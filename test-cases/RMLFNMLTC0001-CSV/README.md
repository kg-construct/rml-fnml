## RMLFNOTC0000-CSV

**Title**: Function on object, 0 parameters

**Description**: Tests
(1) if a function without parameters can be used (FnO)
(2) if a function on an object map can be used (Term)

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
        rml:predicate foaf:name;
        rml:objectMap [
            rml:functionExecution <#Execution> ;
        ]
    ] .

<#Execution>
    rml:function morph-kgc:uuid .

```

**Output**
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "e4dcc7ee-8e2a-4012-92cc-9a74dd545e89" .

```

