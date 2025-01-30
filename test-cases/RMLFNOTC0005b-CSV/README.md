## RMLFNOTC0005b-CSV

**Title**: Function on subject, default termType

**Description**: Tests if the default termType assigned to the output of the function to be correct

**Error expected?** No

**Input**
```
Id,Name,url
1,Venus,www.example.com

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
        rml:functionExecution <#Execution> ;
    ];
    rml:predicateObjectMap [
        rml:predicate foaf:name;
        rml:objectMap [ rml:reference "Name"]
    ] .

<#Execution>
    rml:function fns:schema ;
    rml:input
        [
            rml:parameter fns:stringParameter ;
            rml:inputValueMap [
                rml:reference "Name"
            ];
        ] .

```

**Output**
```
<https://schema.org/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .

```

