import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  if (error) {
    console.error(`Redis client not connected to the server: ${error}`);
  }
}).on('ready', () => {
  console.log('Redis client connected to the server');
});
