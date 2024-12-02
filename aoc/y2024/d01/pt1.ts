import { sorted_insert } from '../../index';


const [aList, bList] = [[], []];

for await (const line of console) {
  const [a, b] = line.split(/\s+/).map(x => parseInt(x, 10));

  sorted_insert(aList, a);
  sorted_insert(bList, b);
}

const total = aList.reduce(
  (acc, n, i) => acc + Math.abs(n - bList[i]), 0
);

console.log(total);