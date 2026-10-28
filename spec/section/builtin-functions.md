<!-- This file is generated from the built-in set of function ontology. -->
<!-- Do not modify by hand! -->

### `rml-fn:isNull` {#fn-isnull}

Returns true if the input is null or empty; otherwise false.

Parameters: `rml-fn:param` (`xsd:anyAtomicType`)  
Return: `rml-fn:boolOut` (`xsd:boolean`)

### `rml-fn:isNotNull` {#fn-isnotnull}

Returns true if the input is not null and not empty; otherwise false.

Parameters: `rml-fn:param` (`xsd:anyAtomicType`)  
Return: `rml-fn:boolOut` (`xsd:boolean`)

### `rml-fn:equals` {#fn-equals}

Returns true if the two inputs are equal according to SPARQL operator semantics; otherwise false.

Parameters: 
- `rml-fn:param` (`xsd:anyAtomicType`)
- `rml-fn:compared` (`xsd:anyAtomicType`)
  
Return: `rml-fn:boolOut` (`xsd:boolean`)

### `rml-fn:notEquals` {#fn-notequals}

Returns true if the two inputs are not equal; otherwise false.

Parameters: 
- `rml-fn:param` (`xsd:anyAtomicType`)
- `rml-fn:compared` (`xsd:anyAtomicType`)
  
Return: `rml-fn:boolOut` (`xsd:boolean`)

### `rml-fn:IF` {#fn-if}

Returns `thenValue` if `boolParam` evaluates to true; otherwise returns `elseValue`.

Parameters: 
- `rml-fn:boolParam` (`xsd:boolean`)
- `rml-fn:thenValue`
- `rml-fn:elseValue`
  
Return: `rml-fn:resultOut`
