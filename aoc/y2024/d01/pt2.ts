import { Counter } from '../../index';


const aList = [];
const build = async function *() {
  for await (const line of console) {
    const [a, b] = line.split(/\s+/).map(x => parseInt(x, 10));
  
    aList.push(a);
    yield b;
  }  
};

(async () => {
  const bCount = await Counter(build());
  console.log(aList.reduce((acc, a) => {
    return acc + (a * (bCount[a] || 0));
  }, 0));
})();
