const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1600, height: 1000}});
  for (const arg of process.argv.slice(2)) {
    const [name, ext] = arg.split(':');
    await p.goto('file://' + path.resolve(name + '.html'));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    const el = await p.$('#g');
    await el.screenshot({path: `out/${name}.${ext === 'jpg' ? 'jpg' : 'png'}`, type: ext === 'jpg' ? 'jpeg' : 'png', quality: ext === 'jpg' ? 88 : undefined});
  }
  await b.close();
})();
