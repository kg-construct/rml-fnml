## The Problem

Mapping languages allow us to define how knowledge graphs are generated from (semi-)structured data,
but only if the original data values can be used as-is.
Complex data transformations in mapping languages typically are
either implemented as custom solutions,
or are done by systems separate from the mapping process.
The former data transformations remain case-specific, often coupled with the mapping,
whereas the latter is not reusable across systems.

For example, we have a data source where all names are lowercase,
but we want the resulting knowledge to have uppercase values.
The following [=RML Mapping=] contains the descriptions to generate a knowledge graph from a data source,
but no data transformations.

<aside class="example" id="example-rml" title="RML Mapping without data transformations">
<aside class="ex-mapping">

```turtle
@prefix dbo: <http://dbpedia.org/ontology/> .
@prefix rml: <http://w3id.org/rml/> .

<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;       # Specify the data source
    rml:subjectMap <#SubjectMap> ;             # Specify the subject
    rml:predicateObjectMap [                   # Specify the predicate-object-map
        rml:predicate dbo:title ;              # Specify the predicate
        rml:objectMap [                        # Specify the object-map
            rml:reference "name"               # Specify the reference within the data source
        ]
    ] .
```

</aside>
</aside>
