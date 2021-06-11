# Function as a service Ontology
Ontology to describing Function as a Service providers and application requirements.

- [Function as a service Ontology](#function-as-a-service-ontology)
  * [Roadmap](./ROADMAP.md)
  * [Examples](#examples)
    + [Model AWS Lambda](#model-aws-lambda)
    + [Model an OpenFaaS environment](#model-an-openfaas-environment)
    + [CovidTracker Application](#covidtracker-application)
    + [EchoServer](#echoserver)
  * [SPARQL Examples](#sparql-examples)
    + [Get all execution environments](#get-all-execution-environments)
    + [Full list of SPARQL examples](./sparql)


Here is the [Roadmap](./ROADMAP.md) for the development

Resources we leveraged in our ontology:

* [time][time] is used to model execution times and other temporal attributes
* [locn][locn] is used to model location attributes (for example data center location or geographical restrictions)
* [dave][dave] is used to model relationships between metrics (the ones required by the application or provided by the Execution Environment)
* [wd][wd]  used to fetch existing concepts (locations, programming languages, cpu architecture)
* [wdt][wdt] used to integrate with existing properties (`part of` for example)
* [DCMI Metadata Terms][terms], [FOAF][foaf], [DCMI Metadata elements][dc], [OWL][owl], [RDF][rdf], [RDFS][rdfs], [XSD][xsd] as the base for most relationships/meta-data and restrictions

## Examples

### Model AWS Lambda

For the full ontology see [this](./faas.owl).

For now the Tbox and Abox are mixed in one file, we need to split them up for clarity.

```rdf
###  http://www.semantic-faas.com/ontology#AWSLambda
:AWSLambda rdf:type owl:NamedIndividual ,
                    :ServerlessExecutionEnvironment ;
           :cpuArch wd:Q272629 ;
           :datacenter :af-south-1a ,
                       :af-south-1b ,
                       :af-south-1c ,
                       :ap-east-1a ,
                       :ap-east-1b ,
                       :ap-east-1c ,
                       :ap-northeast-1a ,
                       :ap-northeast-1b ,
                       :ap-northeast-1c ,
                       :ap-northeast-1d ,
                       :ap-northeast-2a ,
                       :ap-northeast-2b ,
                       :ap-northeast-2c ,
                       :ap-northeast-3a ,
                       :ap-south-1a ,
                       :ap-south-1b ,
                       :ap-south-1c ,
                       :ap-southeast-1a ,
                       :ap-southeast-1b ,
                       :ap-southeast-1c ,
                       :ap-southeast-2a ,
                       :ap-southeast-2b ,
                       :ap-southeast-2c ,
                       :ca-central-1a ,
                       :ca-central-1b ,
                       :ca-central-1c ,
                       :cn-north-1a ,
                       :cn-north-1b ,
                       :cn-northwest-1a ,
                       :cn-northwest-1b ,
                       :eu-central-1a ,
                       :eu-central-1b ,
                       :eu-central-1c ,
                       :eu-north-1a ,
                       :eu-north-1b ,
                       :eu-north-1c ,
                       :eu-south-1a ,
                       :eu-south-1b ,
                       :eu-south-1c ,
                       :eu-west-1a ,
                       :eu-west-1b ,
                       :eu-west-1c ,
                       :eu-west-2a ,
                       :eu-west-2b ,
                       :eu-west-2c ,
                       :eu-west-3a ,
                       :eu-west-3b ,
                       :eu-west-3c ,
                       :me-south-1a ,
                       :me-south-1b ,
                       :me-south-1c ,
                       :sa-east-1a ,
                       :sa-east-1b ,
                       :sa-east-1c ,
                       :us-east-1a ,
                       :us-east-1b ,
                       :us-east-1c ,
                       :us-east-1d ,
                       :us-east-1e ,
                       :us-east-1f ,
                       :us-east-2a ,
                       :us-east-2b ,
                       :us-east-2c ,
                       :us-gov-east-1a ,
                       :us-gov-east-1b ,
                       :us-gov-east-1c ,
                       :us-gov-west-1a ,
                       :us-gov-west-1b ,
                       :us-gov-west-1c ,
                       :us-west-1a ,
                       :us-west-1b ,
                       :us-west-1c ,
                       :us-west-2a ,
                       :us-west-2b ,
                       :us-west-2c ,
                       :us-west-2d ;
           :pricingModel :AWSLambdaPricing ;
           :supportedPackages wd:Q15206305 ,
                              wd:Q161053 ,
                              wd:Q21622213 ,
                              wd:Q251 ,
                              wd:Q28865 ,
                              wd:Q37227 ,
                              wd:Q756100 ;
           :maxAllowedRAM "10240"^^xsd:positiveInteger ;
           :maxAllowedStorage "75"^^xsd:positiveInteger ;
           :maxConccurency "1000"^^xsd:positiveInteger ;
           :maxTimeAllowed "900"^^xsd:positiveInteger ;
           :minRequiredRAM "128"^^xsd:positiveInteger ;
           rdfs:comment "https://aws.amazon.com/lambda/"^^xsd:anyURI ;
           rdfs:label "AWS Lambda"^^xsd:string .
```

### Model an OpenFaaS environment

```ttl
###  http://www.semantic-faas.com/ontology#OpenFaaS
:OpenFaaS rdf:type owl:NamedIndividual ,
                   :ServerlessExecutionEnvironment ;
          :cpuArch wd:Q272629 ;
          :datacenter :FIIDatacenter ;
          :supportedPackages wd:Q15206305 ,
                             wd:Q28865 ;
          :maxAllowedRAM "2048"^^xsd:positiveInteger ;
          :maxAllowedStorage "10"^^xsd:positiveInteger ;
          :maxConccurency "5"^^xsd:positiveInteger ;
          :maxTimeAllowed "360"^^xsd:positiveInteger ;
          :minRequiredRAM "128"^^xsd:positiveInteger ;
          rdfs:comment "A custom instalation of OpenFaas datacenter on commodity hardware."^^xsd:string ,
                       "https://www.openfaas.com/"^^xsd:anyURI ;
          rdfs:label "OpenFaaS"^^xsd:string .
```

### CovidTracker Application

This application has geographical requirements but because of it's sensitivity we don't care about the cost.
We only impose a timeout per request of 30s as a best practice (also this is an app produced by Romania Gourmand, we don't expect it to be efficient)

```rdf
:CovidTracker rdf:type owl:NamedIndividual ,
                       :Application ;
              :code :CovidTrackerCode ;
              :requirements :Max30sRuntime ,
                            :OnlyRomaniaGeoRestriction ;
              :maxPricePerMillionExecution "0.0"^^xsd:double .


###  http://www.semantic-faas.com/ontology#CovidTrackerCode
:CovidTrackerCode rdf:type owl:NamedIndividual ,
                           :Code ;
                  :programmingLanguage wd:Q28865 ;
                  :sourceCode "cHJpbnQoJ0NvdmlkIFRyYWNrZXInKQo="^^xsd:base64Binary .

:OnlyRomaniaGeoRestriction rdf:type owl:NamedIndividual ,
                                    :GeographicalRequirement ;
                           wdt:P361 wd:Q218 .

:Max30sRuntime rdf:type owl:NamedIndividual ,
                        :ExecutionTimeRequirement ;
               :maxTimeAllowed "360"^^xsd:positiveInteger .
```

### EchoServer

This application has more complex requirements:

* max 10s of execution time
* Only x86 architecture
* Max 512MB ram
* Also a cost requirement


```rdf
:EchoServer rdf:type owl:NamedIndividual ,
                     :Application ;
            :code :EchoServerCode ;
            :requirements :AtLeast100Replicas ,
                          :Cpu_x86 ,
                          :Max10seconds ,
                          :Max512MB ;
            :maxPricePerMillionExecution "75.0"^^xsd:double .


###  http://www.semantic-faas.com/ontology#EchoServerCode
:EchoServerCode rdf:type owl:NamedIndividual ,
                         :Code ;
                :programmingLanguage wdt:Q15206305 ,
                                     wdt:Q28865 ;
                rdfs:comment "Docker File with a echo server" ;
                foaf:homepage "https://hub.docker.com/r/ealen/echo-server"^^xsd:anyURI .

:AtLeast100Replicas rdf:type owl:NamedIndividual ,
                             :ConcurrencyRequirement ;
                    :minConcurrency "100"^^xsd:positiveInteger .

:Cpu_x86 rdf:type owl:NamedIndividual ,
                  :CPURequirement ;
         :cpuArch wd:Q272629 .

:Max10seconds rdf:type owl:NamedIndividual ,
                       :ExecutionTimeRequirement ;
              :maxTimeAllowed "10"^^xsd:positiveInteger .

:Max512MB rdf:type owl:NamedIndividual ,
                   :MemoryRequirement ;
          :maxAllowedRAM "512"^^xsd:positiveInteger .
```


## SPARQL Examples

For more example see [this list](./sparql)

### Get all execution environments

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX faas: <http://www.semantic-faas.com/ontology#>
SELECT  DISTINCT ?subject
WHERE {
  ?subject rdf:type owl:NamedIndividual .
  ?subject rdf:type faas:ServerlessExecutionEnvironment .
}
```

[terms]: http://purl.org/dc/terms/
[foaf]: http://xmlns.com/foaf/0.1/
[dc]: http://purl.org/dc/elements/1.1/
[owl]: http://www.w3.org/2002/07/owl#
[rdf]: http://www.w3.org/1999/02/22-rdf-syntax-ns#
[time]: http://www.w3.org/2006/time#
[locn]: http://www.w3.org/ns/locn#
[dave]: http://theme-e.adaptcentre.ie/dave#
[wd]: http://www.wikidata.org/entity/
[wdt]: http://www.wikidata.org/prop/direct/
[xsd]: http://www.w3.org/2001/XMLSchema#
[rdfs]: http://www.w3.org/2000/01/rdf-schema#
