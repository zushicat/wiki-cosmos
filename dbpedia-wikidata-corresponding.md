## Getting corresponding ID/resource between Wikidata and DBpedia


### Case 1: You know the wikidata ID and like to know the corresponding DBpedia resource

#### Use Sparql
Request URL: https://query.wikidata.org/

```
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?dbpedia_resource ?wikidata_id {
    VALUES ?wikidata_id {wd:Q44}
    SERVICE <http://dbpedia.org/sparql> {
        ?dbpedia_resource owl:sameAs ?wikidata_id .
    }
}
```

Result:
| dbpedia_resource                   | wikidata_id |
|------------------------------------|-------------|
| <http://dbpedia.org/resource/Beer> | wd:Q44      |



#### Use Wikidata API request
Get Wikipedia title (which corresponds to DBpedia resource name)

```
https://www.wikidata.org/w/api.php?
action=wbgetentities&
ids=Q44&
format=json&
props=sitelinks
```

Get english Wikipedia title (enwiki.title) in response JSON (see drastically shortened version below)
```
{
  "entities": {
    "Q44": {
      "type": "item",
      "id": "Q44",
      "sitelinks": {
        "enwiki": {
          "site": "enwiki",
          "title": "Beer",
          "badges": [
            "Q17437798"
          ]
        }
      }
    }
  },
  "success": 1
}
```

Go to: http://dbpedia.org/page/Beer


### Case 2: You know the DBpedia resource and like to know the corresponding wikidata ID

#### Request DBpedia 
Request URL: http://dbpedia.org/sparql

```
SELECT distinct ?wikidata_id_link
WHERE {dbr:Beer owl:sameAs ?wikidata_id_link

      FILTER(regex(str(?wikidata_id_link), "www.wikidata.org" ) )
}
```

Result:
| wikidata_id_link                   |
|------------------------------------|
| http://www.wikidata.org/entity/Q44 |


#### Request Wikidata
Request URL: https://query.wikidata.org/

```
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>

SELECT ?dbpedia_id ?wikidata_id {
    VALUES ?dbpedia_id {dbr:Beer}
    SERVICE <http://dbpedia.org/sparql> {
        ?dbpedia_id owl:sameAs ?wikidata_id .
    }
    FILTER(regex(str(?wikidata_id), "www.wikidata.org" ) )
}
```

Result:
| dbpedia_id                         | wikidata_id |
|------------------------------------|-------------|
| <http://dbpedia.org/resource/Beer> | wd:Q44      |
