## The Problem {#problem}

*This section is non-normative.*

Mapping languages allow us to define how knowledge graphs are generated from (semi-)structured data, but standard mappings assume that the original data values can be used as-is.
Complex data transformations in mapping languages typically are either implemented as custom procedural functions within proprietary mapping engines, or are performed by external pre-processing pipelines prior to mapping.

The former approach produces tightly-coupled, non-interoperable mappings that cannot be executed across different tools, whereas the latter introduces brittle, multi-stage pipelines that complicate data governance and maintenance.

### Motivating Example

Consider an input data source containing person records where names are stored in lowercase, but the target ontology requires uppercase titles.

<aside class="ex-input">

```json
[
  {
    "id": "1",
    "name": "alice smith"
  },
  {
    "id": "2",
    "name": "bob jones"
  }
]
```

</aside>

The following standard [[RML-Core]] mapping generates triples from this data source, but cannot perform data transformations:

<aside class="example" id="example-rml" title="RML Mapping without data transformations">
<aside class="ex-mapping">

```turtle
<#Person_Mapping>
    rml:logicalSource <#LogicalSource> ;
    rml:subjectMap [
        rml:template "http://example.com/person/{id}"
    ] ;
    rml:predicateObjectMap [
        rml:predicate ex:title ;
        rml:objectMap [
            rml:reference "name"
        ]
    ] .
```

</aside>
</aside>

Without transformation support, executing this mapping produces knowledge graph values identical to the raw source data:

<aside class="ex-output">

```turtle
<http://example.com/person/1> ex:title "alice smith" .
<http://example.com/person/2> ex:title "bob jones" .
```

</aside>

However, the desired target knowledge graph requires transforming each name into uppercase before generating the RDF literal:

<aside class="ex-output">

```turtle
<http://example.com/person/1> ex:title "ALICE SMITH" .
<http://example.com/person/2> ex:title "BOB JONES" .
```

</aside>

RML-FNML addresses this gap by defining a standard, declarative mechanism to execute functions during the mapping evaluation process.
