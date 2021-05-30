import test from 'ava';
import appendor from '../src/appendor.js';

test('extracting Qs out of multiline string', t => {
  const multilineOwl = `initial
  owl`;

  const extractedQs = appendor.append(multilineOwl, [
    `   rdfs:domain :CPURequirement ,
                :FaaSExecutionEnvironment`,
    `   rdfs:domain :CPURequirement ,
                :FaaSExecutionEnvironment`
  ]);

  t.deepEqual(extractedQs,
    `initial
  owl
   rdfs:domain :CPURequirement ,
                :FaaSExecutionEnvironment
   rdfs:domain :CPURequirement ,
                :FaaSExecutionEnvironment`);
});