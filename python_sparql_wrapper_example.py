
'''
See examples: https://rdflib.github.io/sparqlwrapper/

Request http://dbpedia.org/sparql with question: In which categories falls the resource "Cheeseburger"?
Limit (filter) response to english categoryName results

Result print out:
categoryUri: http://dbpedia.org/resource/Category:Hamburgers_(food) categoryName: Hamburgers (food) (en)
categoryUri: http://dbpedia.org/resource/Category:American_sandwiches categoryName: American sandwiches (en)
categoryUri: http://dbpedia.org/resource/Category:Culture_of_Denver categoryName: Culture of Denver (en)
'''

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

sparql.setQuery("""
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?categoryUri ?categoryName
    WHERE {
        <http://dbpedia.org/resource/Cheeseburger> dcterms:subject ?categoryUri.
        ?categoryUri rdfs:label ?categoryName.
        FILTER (lang(?categoryName) = "en")
    }
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(f'categoryUri: {result["categoryUri"]["value"]} categoryName: {result["categoryName"]["value"]} ({result["categoryName"]["xml:lang"]})')
