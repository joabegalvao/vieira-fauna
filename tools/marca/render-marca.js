// Gera, a partir de tools/marca/marca.svg e das fontes do site:
//   tools/marca/marca-512.png         usado pelo optimize-images.py (favicon e ícones)
//   assets/img/compartilhamento.jpg   imagem de 1200x630 para WhatsApp e redes
//
// Uso (na raiz do projeto):
//   node tools/marca/render-marca.js
//
// Requer Node e Playwright com Chromium. Se o Playwright não estiver instalado
// neste projeto, informe os caminhos pelas variáveis de ambiente
// PLAYWRIGHT_MODULE (pasta node_modules/playwright) e CHROMIUM_PATH.
const path = require('path');
const fs = require('fs');
const os = require('os');

const playwrightModule = process.env.PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(playwrightModule);

const here = __dirname;
const root = path.resolve(here, '..', '..');
const svg = fs.readFileSync(path.join(here, 'marca.svg'), 'utf8');
const svgAt = (size) => svg.replace(/width="\d+" height="\d+"/, `width="${size}" height="${size}"`);

const fontFace = (family, file, style) => `@font-face { font-family: "${family}"; src: url("file://${path.join(root, 'assets/fonts', file)}") format("woff2"); font-style: ${style}; font-weight: 400 800; }`;
const fonts = [
  fontFace('Fraunces', 'fraunces-normal-latin.woff2', 'normal'),
  fontFace('Fraunces', 'fraunces-italic-latin.woff2', 'italic'),
  fontFace('Manrope', 'manrope-normal-latin.woff2', 'normal'),
].join('\n');

const photo = fs.readdirSync(path.join(root, 'assets/img')).filter((f) => /^spitz-depois-do-banho-\d+\.jpg$/.test(f)).sort().pop();

const card = `<!doctype html><html><head><meta charset="utf-8"><style>
${fonts}
body { margin: 0; width: 1200px; height: 630px; display: grid; grid-template-columns: 600px 600px; background: #f5efe4; color: #0b3b3a; font-family: Manrope, sans-serif; }
.left { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 0 56px; }
.name { margin-top: 28px; font-family: Fraunces, serif; font-weight: 600; font-size: 60px; line-height: 1; letter-spacing: -0.015em; }
.sub { margin-top: 14px; font-size: 18px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #12615c; }
.tag { margin-top: 26px; font-family: Fraunces, serif; font-style: italic; font-size: 26px; color: #4f5d5a; }
img { width: 600px; height: 630px; object-fit: cover; object-position: 50% 40%; display: block; }
</style></head><body>
<div class="left">${svgAt(180)}<div class="name">Vieira</div><div class="sub">Fauna Shopping</div><div class="tag">Pet shop em Maringá PR</div></div>
<img src="file://${path.join(root, 'assets/img', photo)}" alt="">
</body></html>`;

(async () => {
  const browser = await chromium.launch(
    process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}
  );

  let page = await browser.newPage({ viewport: { width: 512, height: 512 }, deviceScaleFactor: 1 });
  await page.setContent(`<body style="margin:0;background:transparent">${svg}</body>`);
  await page.screenshot({ path: path.join(here, 'marca-512.png'), omitBackground: true });
  await page.close();
  console.log('tools/marca/marca-512.png');

  page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  // a página é aberta por file:// para o Chromium aceitar as fontes e a foto locais
  const tmp = path.join(os.tmpdir(), 'vieira-compartilhamento.html');
  fs.writeFileSync(tmp, card);
  await page.goto('file://' + tmp, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  fs.unlinkSync(tmp);
  await page.screenshot({ path: path.join(root, 'assets/img/compartilhamento.jpg'), type: 'jpeg', quality: 86 });
  await page.close();
  console.log('assets/img/compartilhamento.jpg');

  await browser.close();
})();
