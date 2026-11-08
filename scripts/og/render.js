const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
for(const n of (process.argv[3]||'home,getiriler,masa').split(',')){await p.goto('file://'+process.argv[2]+'/'+n+'.html');await p.waitForTimeout(300);await p.screenshot({path:process.argv[2]+'/og-'+n+'.png'});}
await b.close();})();
