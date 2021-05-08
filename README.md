# Function as a service Ontology
Ontology to interact and parse function as a service providers and also define application that can be deployed.

## Questions / usecase we want to support

#### For Phase I (release 0.1.0):

* [ ] Basic query / compression of FaaS providers
* [x] Ability to define an application and using SPARQL query to find a list of suitable providers
   *  [x] RAM requirements
   *  [x] CPU requirements
   *  [x] Storage Requirements
   *  [x] Supported Languages (and versions)
   *  [x] Geographical restrictions
   *  [x] Cost restrictions
   *  [x] Available metrics (not every platform offers the same metrics)
   *  [x] Concurrency requirements
* [ ] Model a subset of environments
   *  [ ] AWSLambda
     * [x] model all datacenters
       * [ ] link them with wikidata objects
     * [ ] model pricing
     * [ ] model concurenty model
     * [ ] model concurenty
     * [ ] model exection time restrictions
     * [ ] model memory capability
     * [ ] model storage capability
   *  [ ] GoogleFunctions
     * [ ] model all datacenters
       * [ ] link them with wikidata objects
     * [ ] model pricing
     * [ ] model concurenty model
     * [ ] model concurenty
     * [ ] model exection time restrictions
     * [ ] model memory capability
     * [ ] model storage capability
   *  [ ] LocalCloudFaaS (implemanted using Knative for example)
     * [ ] model the single region (Probably Romania)
       * [ ] link them with wikidata objects
     * [ ] model pricing
     * [ ] model concurenty model
     * [ ] model concurenty
     * [ ] model exection time restrictions
     * [ ] model memory capability
     * [ ] model storage capability
* [ ] Model 3 functions
  * [ ] TBD
  * [ ] TBD
  * [ ] TBD
* [x] Tool to fetch all label from WikiData (this is used to make working with protege more intuit)



Example:

```
    AWSLambda
    GovAwsLambda ?
    Google Functions
    LocalCloudFaaS

    EchoServer:
     - 128Mb RAM
     - time to run 5s
     - code
        - python 3.5+
     - UpTime 99.9+
     - pay up to 0.01$ per req

    GovSchedule (rest api)
     - 512Mb Ram
     - time to run 20s
     - code
       - javascript ecmascript ==5
     - uptime required 99.99
     - pay
       * up to 0.5$ per req
       * no more then 0.0000000083$ per 512 MB per 1 ms of runtime ??????
       * no more then 10 000$ / month
     - cpuArch: x86 (c++ library requirement)
     - geoRestrictions
       - only EU data centers
```





#### For Phase II (release 0.2.0):

* [ ] What services can the FaaS provider interact with ?
 * [ ] here for example Lambda can interact with S3, DynamoDB etc ... we should create another ontology for (Object storage, databases etc ...)
* [ ] invocation methods
 * [ ] HTTP
 * [ ] QUEUE invocation
* [ ] SLA provided by the platform
* [ ] split info about individuals and ontology/vocabulary (Abox and Tbox)

#### For Phase III (release 0.3.0):

* [ ] Here we should start looking at providing an abstraction over multiple FaaS providers using our model


## Raw Objects

- FaaSExecutionEnvironment
  - minRAM
  - maxRAM
  - maxTimeAllowed
  - supportedPackages -> Union[ SoftwareLanguage... ] and [wikidata:contaier]
  - maxConccurency
  - availableRegions - [ lista de concepte existente ]
  - pricingModel
  - SLA's
  - metrics

- Application
  - code -> Code
  - Requirements
  - SLA's




- Code
  - programmingLanguage -> SoftwareLanguage
  -

- SoftwareLanguage
  - InterpretedSoftware
      - version
      - <ce mai gasim despre conceptul asta public>
  - CompiledSoftware
      - version
      - <ce mai gasim despre conceptul asta public>

- Requirement
  - minRequiredRAM
  - maxAllowedRAM
  - maxTimeAllowed
  - maxConccurency
  - geoRestrictions
  - cpuArch <- daca e specificat; daca nu fallback pe Language info

- SLA's
  - <search and figure out how to model this>

- PricingModel
  - pay by CPU
    - fractie CPU / moneda
  - pay by Memory
    - x Mb / moneda

- Metrics
  - tipul de metrica; granularitatea; unitatea de masura
