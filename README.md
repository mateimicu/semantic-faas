# Function as a service Ontology
Ontology to interact and parse function as a service providers and also define application that can be deployed.

## Questions / usecase we want to support

For Phase I (release 0.1.0):

* Basic query / compression of FaaS providers
* Ability to define an application and using SPARQL query to find a list of suitable providers
  * RAM requirements
  * CPU requirements
  * Storage Requirements
  * Supported Languages (and versions)
  * Geographical restrictions
  * Cost restrictions
  * Available metrics (not every platform offers the same metrics)
  * Concurrency requirements


For Phase II (release 0.2.0):

* What services can the FaaS provider interact with ?
  * here for example Lambda can interact with S3, DynamoDB etc ... we should create another ontology for (Object storage, databases etc ...)
* invocation methods
  * HTTP
  * QUEUE invocation
* SLA provided by the platform

For Phase III (release 0.3.0):

* Here we should start looking at providing an abstraction over multiple FaaS providers using our model


# Raw Objects
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
