## RMLFNMLTC0200

**Title**: Constant function execution can omit logical source

**Description**: Test a Triples Map with only constant expressions in a function execution can omit logical source

**Error expected?** No

**Mapping**
```
@prefix rml: <http://w3id.org/rml/>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#>.

<http://example.com/base/TriplesMap1> a rml:TriplesMap;
  rml:subjectMap [ rml:constant <http://example.com/Gaston> ];
  rml:predicateObjectMap [
    rml:predicate rdfs:label;
    rml:objectMap [
      rml:functionExecution [
        rml:function grel:toUppercase;
        rml:input [
          rml:parameter grel:valueParam;
          rml:inputValueMap [
            rml:constant "Gaston Lagaffe"
          ];
        ];
      ];
      rml:return grel:stringOut;
      rml:language "fr-BE" ;
    ];
  ].


```

**Output**
```
<http://example.com/Gaston> <http://www.w3.org/2000/01/rdf-schema#label> "GASTON LAGAFFE"@fr-BE .
```

