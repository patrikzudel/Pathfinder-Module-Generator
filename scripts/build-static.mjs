import {mkdir, copyFile} from 'node:fs/promises';

const root = new URL('../', import.meta.url);
const output = new URL('dist/', root);
await mkdir(output, {recursive: true});
await copyFile(new URL('index.html', root), new URL('index.html', output));
await copyFile(new URL('Pathfinder_core.stl', root), new URL('pathfinder_core.stl', output));
console.log('Static site built in dist/');
