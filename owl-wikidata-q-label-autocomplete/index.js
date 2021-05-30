import server from './src/server.js';
import env from './env.js';

server.start(env.host, env.port);