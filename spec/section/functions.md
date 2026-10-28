## Functions & Built-in Set {#functions}

This section describes how functions are declared in [[[FnO]]] and outlines the candidate built-in functions.

### Function Declarations in FnO {#fno-declarations}

Functions in RML-FNML are declared independently of any programming language or execution runtime using the Function Ontology [[[FnO]]].

A complete [[FnO]] declaration defines the function identifier, its metadata, its expected input parameters, and its declared outputs:

<aside class="example" id="example-fno-declaration" title="FnO Function Declaration for toUppercase">
<aside class="ex-mapping">

```turtle
# Function Declaration
grel:toUpperCase
    a                   fno:Function ;
    fno:name            "to Uppercase" ;
    rdfs:label          "to Uppercase" ;
    dcterms:description "Returns the input string with all letters converted to upper case." ;
    fno:expects         ( grel:valueParam ) ;
    fno:returns         ( grel:stringOut ) .

# Parameter Declaration
grel:valueParam
    a             fno:Parameter ;
    fno:name      "input value" ;
    rdfs:label    "input value" ;
    fno:type      xsd:string ;
    fno:required  "true"^^xsd:boolean .

# Output Declaration
grel:stringOut
    a             fno:Output ;
    fno:name      "output string" ;
    rdfs:label    "output string" ;
    fno:type      xsd:string .
```

</aside>
</aside>

* `fno:Function`: Declares the function entity. Its `fno:expects` property points to an RDF list of `fno:Parameter` entities; its `fno:returns` property points to an RDF list of `fno:Output` entities.
* `fno:Parameter`: Declares an input parameter entity. Conforming Parameter Maps reference this IRI.
* `fno:Output`: Declares a returned output entity. Conforming Return Maps reference this IRI.

### Built-in set of functions {#builtin-functions}

To support conditional expressions (`rml:condition`), conforming RML processors MUST support the following functions:

<div class="ednote" title="Functions for condition">
<p>
We previously mentioned that these functions were mandatory for conditions:
</p>
<ul>
  <li><code>fns:isNull</code></li>
  <li><code>fns:isNotNull</code></li>
  <li><code>fns:equals</code></li>
  <li><code>fns:notEquals</code></li>
  <li><code>fns:IF</code></li>
</ul>

| Prefix | Namespace                 |
| ------ | ------------------------- |
| `fns:` | `http://example.com/fns#` |
</div>

