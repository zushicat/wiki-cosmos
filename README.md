# wiki-cosmos
Collection of scripts and links regarding dbpedia/wikidata data retrieval


## Request Links
| Project  | Used for              | URL                                                            |
|----------|-----------------------|----------------------------------------------------------------|
| DBPedia  | sparql request        | https://dbpedia.org/sparql                                     |
| DBPedia  | sparql request        | http://dbpedia.org/snorql/                                     |
| DBPedia  | request by resource   | http://dbpedia.org/resource/Sushi                              |
| Wikidata | sparql request        | https://query.wikidata.org/                                    |
| Wikidata | request by id         | https://www.wikidata.org/wiki/Q211340                          |
| Wikidata | request json by id    | https://www.wikidata.org/wiki/Special:EntityData/Q1998962.json |


There is a Python Sparql wrapper available at: https://rdflib.github.io/sparqlwrapper/ (https://pypi.org/project/SPARQLWrapper/)



## Example Requests
These are simple request examples for illustration.

### DBPedia Sparql
For more examples, see: dbpedia-sparql-request-collection.txt


Request subcategories of category "Cuisine"
https://dbpedia.org/sparql
```
PREFIX cat: <http://dbpedia.org/resource/Category:>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?page, ?subcat
WHERE {
   ?subcat skos:broader* cat:Cuisine.
   ?page dcterms:subject ?subcat
}
LIMIT 5
```

Results:
| page                                       | subcat                                             |
|--------------------------------------------|----------------------------------------------------|
http://dbpedia.org/resource/Blancmange       | http://dbpedia.org/resource/Category:Almond_dishes |
http://dbpedia.org/resource/Frutta_martorana | http://dbpedia.org/resource/Category:Almond_dishes |
http://dbpedia.org/resource/Bakewell_tart    | http://dbpedia.org/resource/Category:Almond_dishes |
http://dbpedia.org/resource/Biscuit_Tortoni  | http://dbpedia.org/resource/Category:Almond_dishes |
http://dbpedia.org/resource/Gugelhupf        | http://dbpedia.org/resource/Category:Almond_dishes |



### Wikidata Sparql
Request for beer style (Q1998962)
https://query.wikidata.org/
```
SELECT ?item ?itemLabel ?_image ?_subclass_of ?_subclass_ofLabel WHERE {
  ?item wdt:P31 wd:Q1998962.
  ?item wdt:P279 ?_subclass_of.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  OPTIONAL { ?item wdt:P18 ?_image. }
}
LIMIT 5
```

Result:
| item       | itemLabel    | _image                 | _subclass_of | _subclass_ofLabel |
|------------|--------------|------------------------|--------------|-------------------|
| wd:Q4626   | Kölsch       | commons:Koelsch.jpg    | wd:Q261105   | Helles            |
| wd:Q4626   | Kölsch       | commons:Koelsch.jpg    | wd:Q44       | Bier              |
| wd:Q27201  | Bitter       | commons:Ale Bitter.jpg | wd:Q11994509 | obergäriges Bier  |
| wd:Q131413 | Weizenbier   |                        | wd:Q11994509 | obergäriges Bier  |
| wd:Q152281 | Pilsner Bier | commons:Pilznery.jpg   | wd:Q15709638 | Pale lager        |




### Wikidata API
Request labels and aliases in english, german and italian for beer style (Q1998962) and beer (Q44)
For printer friendy result in browser: skip "format=json" in request
```
https://www.wikidata.org/w/api.php?
action=wbgetentities&
ids=Q1998962|Q44&
props=labels|aliases&
languages=en|de|it&
format=json
```

Result for this request (for beer labels/aliases in english and german)
https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q44&props=labels|aliases&languages=en|de

```
{
    "entities": {
        "Q44": {
            "type": "item",
            "id": "Q44",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "beer"
                },
                "de": {
                    "language": "de",
                    "value": "Bier"
                }
            },
            "aliases": {
                "en": [
                    {
                        "language": "en",
                        "value": "brew"
                    }
                ]
            }
        }
    },
    "success": 1
}
```