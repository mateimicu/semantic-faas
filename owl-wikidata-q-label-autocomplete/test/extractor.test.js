import test from 'ava';
import extractor from '../src/extractor.js';

test('extracting Qs out of multiline string', t => {
  const multilineOwl = `
###  http://www.semantic-faas.com/ontology#cpuArch
:cpuArch rdf:type owl:ObjectProperty ,
                  owl:AsymmetricProperty ,
                  wd:Q23ricProperty ,
                  owl:IrreflexiveProperty ;
          rdfs:domain :CPURequirement ,
                      :FaaSExecutionEnvironment ;
          rdfs:range wd:Q272683;
          rdfs:comment "CPU Architectures required for the code to work"@en .
###  http://www.semantic-faas.com/ontology#cpuArch
:cpuArch rdf:type owl:ObjectProperty ,
                  owl:AsymmetricProperty ,
                  wd:Q234ricProperty ,
                  owl:IrreflexiveProperty ;
        rdfs:domain :CPURequirement ,
                    :FaaSExecutionEnvironment ;
        rdfs:range wd:Q272623;
        rdfs:comment "CPU Architectures required for the code to work"@en .
###  http://www.semantic-faas.com/ontology#cpuArch
:cpuArch rdf:type owl:ObjectProperty ,
                  owl:AsymmetricProperty ,
                  wd:Q234ricProperty ,
                  owl:IrreflexiveProperty ;
        rdfs:domain :CPURequirement ,
                    :FaaSExecutionEnvironment ;
        rdfs:range wd:Q272623;
        rdfs:comment "CPU Architectures required for the code to work"@en .
`;

  const extractedQs = extractor.extract(multilineOwl, 'wd', 'Q');

  t.deepEqual(extractedQs, ['Q23', 'Q272683', 'Q234', 'Q272623']);
});