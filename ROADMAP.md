
## Questions / usecase we want to support

#### For Phase I (release 0.1.0):

* [x] Ability to define an application and using SPARQL query to find a list of suitable providers
    * [x] RAM requirements
    * [x] CPU requirements
    * [x] Storage Requirements
    * [x] Supported Languages (and versions)
    * [x] Geographical restrictions
    * [x] Cost restrictions
    * [x] Available metrics (not every platform offers the same metrics)
    * [x] Concurrency requirements
* [x] Model 2
    *  [x] AWSLambda
        * [x] model all datacenters
        * [x] model pricing
        * [x] model concurenty
        * [x] model exection time restrictions
        * [x] model memory capability
        * [x] model storage capability
        * [x] what can it run
    *  [x] LocalCloudFaaS (implemanted using OpenFaaS for example)
        * [x] model the single region
        * [x] model pricing
        * [x] model concurenty model
        * [x] model concurenty
        * [x] model exection time restrictions
        * [x] model memory capability
        * [x] model storage capability
* [x] Model 2 functions
    * [x] EchoServer
        * [x] CPU requirement x86
        * [x] Max 10s of runtime
        * [x] At least 100 concurrent replicas
        * [x] Max 512MB ram
        * [x] Packaging Docker
    * [x] CovidTracker
        * [x] Geographical restriction only for Romania
        * [x] Max 30s of runtime
        * [x] Packaging Python
        * [x] Specify sourcecode
* [x] Example SPARQL query's
    * [x] Get all execution environments
    * [x] Get all execution environments that have at least two datacenters
    * [x] Get a suitable execution environment for CovidTracker
    * [x] Get a suitable execution environment for EchoServer
* [x] Tool to fetch all label from WikiData (this is used to make working with protege more intuit)

  * SLA requirements
  * SLA Requirements
    * disturbance
    * penalty requirements
* Abox
* SPARQL query that includes filters for SLA requirements


#### For Phase II (release 0.2.0):

* [ ] Generic SPARQL query (Given any application provide all suitable execution environment) (can use something like VALUES)
    * [ ] Integrate with WikiData for more geographical information (SERVICE)
    * [ ] Link existing data centers with WikiData locations
* [ ] Model what services can the FaaS provider interact with ?
    * [ ] here for example Lambda can interact with S3, DynamoDB etc ... we should create another ontology for (Object storage, databases etc ...)
* [ ] invocation methods
    * [ ] HTTP
    * [ ] QUEUE invocation
* [x] Model SLA provided by the platform
    * [x] Implement SLA specification for AWS Lambda
* [x] Model SLA requirements
    * [x] SLA penalty
    * [x] SLA refund (also with refund types)
    * [x] Implement SLA requirements for Echo Server
* [ ] split info about individuals and ontology/vocabulary (Abox and Tbox)

#### For Phase III (release 0.3.0):

* [ ] Here we should start looking at providing an abstraction over multiple FaaS providers using our model
