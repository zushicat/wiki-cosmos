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
| Github   | python sparql wrapper | https://rdflib.github.io/sparqlwrapper/                        |


## Example Requests
These are simple request examples for illustration.


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