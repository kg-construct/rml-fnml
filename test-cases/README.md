# FNML Test Cases

Each test case is within a subfolder of this folder.

If no output.nq file is present, an error is expected.

All function descriptions are locally available under [functions.ttl](./functions.ttl).

A nicely rendered HTML page of all test cases is available at https://w3id.org/rml/fnml/test-cases.

## Functions that are used in these test cases

`@prefix idlab-fn: <https://w3id.org/imec/idlab/function#> .`
`@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .`

## Updating the metadata

The test cases publication (html pages) can be generated as followed:

1. Add the testcase description in `descriptions.csv` or fetch it from the [Google spreadsheet](https://docs.google.com/spreadsheets/d/1Ui216z2cF8bNAbdZvws-JoAhcjj4M2k_NlfzmCh1jh8/edit?gid=1793408313#gid=1793408313).
2. Execute the `make-metadata.py` script: `./make-metadata.py http://w3id.org/rml/fnml/`
   (This is based on the content of the folders with the test cases, and on the file descriptions.csv for the descriptions of the cases)
3. Download burp: `curl -LO https://github.com/kg-construct/BURP/releases/download/v0.1.1/burp.jar`
4. Generate the manifest with [Burp](https://github.com/kg-construct/BURP): `java -jar burp.jar -m manifest.rml.ttl -o manifest.ttl -b http://w3id.org/rml/fnml/test/`
5. Run list.sh and insert output in dev.html
6. Set the `prevVersion` in config.js
7. To publish the new HTML verson of the test cases, export `dev.html` as `index.html` in ./docs and in a subfolder with the date of the publication (maybe adapt the publication date)

## Open issues for which there are no test cases

| title | purpose |
| - | - |
| Function on object, default termType | Tests if the default termType assigned to the output of the function in an object position to be correct |
| Function on subject, default termType | Tests if the default termType assigned to the output of the function in a subject position to be correct |
| Function using non-constant shortcut property function | Tests that a non-constant FNML Function map also works |
| Function using non-constant shortcut property return | Tests that a non-constant FNML Return map also works |
| Nested function - Test B | Tests if a composite function of form f(g(x1),h(x2)) works (i.e., two different inner functions are the arguments of the outer function) |
| Nested function - Test C | Tests if a composite function of form f(g(h(x1),x2),x3) works (i.e., the inner function is also a composite function) |
