#!/usr/bin/node
if (process.argv.length <= 1) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(1, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 1]);
}
