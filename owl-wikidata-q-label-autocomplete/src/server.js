import express from 'express';
import swaggerUi from 'swagger-ui-express';
import extractor from './extractor.js';
import appendor from './appendor.js';
import { readFileSync } from 'fs';

const start = (host, port) => {
  const app = express();
  app.get('/', (req, res) => {
    let { text, importPrefix, idPrefix, apiUrl } = req.body;
    let ids = extractor.extract(text, importPrefix, idPrefix);

    appendor.append(text, ids);

    res.body = text;
  });

  const swaggerFile = JSON.parse(readFileSync('./swagger.json'));

  app.use(
    '/api-docs',
    swaggerUi.serve,
    swaggerUi.setup(swaggerFile)
  );

  app.listen(port, host);

  console.log(`Running on http://${ host }:${ port }`);
}

export default { start };