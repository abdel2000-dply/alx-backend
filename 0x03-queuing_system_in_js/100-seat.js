import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();
let reservationEnabled = true;
const port = 1245;

client.on('error', (err) => {
  console.log(err);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

setAsync('available_seats', 50);

function reserveSeat(number) {
  return setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats.toString() });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () =>
    console.log(`Seat reservation job ${job.id} completed`)
  );
  job.on('failed', (errorMessage) =>
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`)
  );
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();
    if (seats > 0) {
      await reserveSeat(--seats);
      if (seats === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
  res.json({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
