import http from 'k6/http';
import { check } from 'k6';

export let options = {
  vus: 100,
  duration: '30s',
};

export default function () {
  let res = http.get('http://localhost:5000/games/play/');
  check(res, {
    'is status 200': (r) => r.status === 200,
  });
}
