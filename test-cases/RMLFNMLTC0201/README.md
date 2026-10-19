## RMLFNMLTC0201

**Title**: Non constant mapping, while omitting logical source

**Description**: Test a Triples Map with reference expressions in a function execution cannot omit logical source

**Error expected?** Yes

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
            rml:template "{name}"
          ];
        ];
      ];
      rml:return grel:stringOut;
      rml:language "fr-BE" ;
    ];
  ].


```

