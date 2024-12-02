export const bisect_left = (arr, x, lo = 0, hi = null) => {
  if (hi === null) hi = arr.length;

  while (lo < hi) {
    let mid = Math.floor((lo + hi) / 2);
    if (arr[mid] < x) {
      lo = mid + 1;
    } else {
      hi = mid;
    }
  }
  return lo;
}

export const sorted_insert = (arr, x) => {
  const i = bisect_left(arr, x);
  arr.splice(i, 0, x);
}

export function createDefaultDict(fn) {
  return new Proxy({}, {
    get(target, prop, receiver) {
      if (!(prop in target)) {
        target[prop] = fn();
      }
      return target[prop];
    },
    set(target, prop, value) {
      target[prop] = value;
      return true;
    }
  });
}

export async function Counter(iter) {
  async function asyncReduce(asyncGenerator, reducer, initialValue) {
    let accumulator = initialValue;
  
    for await (const value of asyncGenerator) {
      accumulator = await reducer(accumulator, value);
    }
  
    return accumulator;
  };

  const counts = await asyncReduce(iter, (acc, el) => ({
    ...acc,
    [el]: (acc[el] ? acc[el] : 0) + 1
  }), {});

  return new Proxy(counts, {
    get(target, prop, receiver) {
      return target[prop];
    }
  });
};