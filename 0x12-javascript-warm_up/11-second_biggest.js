#!/usr/bin/node
const arg = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  arg.sort((a, b) => a - b).reverse();
  console.log(arg[1]);
}
