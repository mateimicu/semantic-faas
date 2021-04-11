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
