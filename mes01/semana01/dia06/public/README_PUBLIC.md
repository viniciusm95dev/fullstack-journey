# 📁 Pasta Public - Arquivos Estáticos

## 📂 Estrutura da Pasta Public

```
public/
├── calculator-icon.svg     # Ícone principal SVG (64x64)
├── favicon.ico            # Favicon do site (múltiplos tamanhos)
├── manifest.json          # PWA manifest
├── sw.js                  # Service Worker
├── robots.txt             # SEO - Crawler instructions
├── icon-192.png          # Ícone PWA 192x192 (criar)
├── icon-512.png          # Ícone PWA 512x512 (criar)
└── calculator-preview.png # Preview para redes sociais (criar)
```

## ✅ Arquivos Já Criados
- ✅ `calculator-icon.svg` - Ícone SVG principal
- ✅ `manifest.json` - Configuração PWA
- ✅ `sw.js` - Service Worker para cache
- ✅ `robots.txt` - SEO básico

## 🔄 Arquivos Para Gerar

### 1. favicon.ico
Converta o `calculator-icon.svg` para favicon.ico usando:
- https://favicon.io/favicon-converter/
- https://convertio.co/svg-ico/

### 2. icon-192.png e icon-512.png
Exporte o `calculator-icon.svg` como PNG nos tamanhos:
- 192x192px para `icon-192.png`
- 512x512px para `icon-512.png`

### 3. calculator-preview.png (Opcional)
Crie um preview 1200x630px para Open Graph:
- Screenshot da calculadora
- Logo + título
- Para redes sociais (Facebook, Twitter)

## 🛠️ Como Gerar os Arquivos PNG

### Opção 1: Online (Rápido)
1. Vá em https://convertio.co/svg-png/
2. Upload do `calculator-icon.svg`
3. Configure tamanho (192x192 ou 512x512)
4. Download e renomeie

### Opção 2: Usando Figma/Design
1. Importe o SVG no Figma
2. Redimensione para 192x192 ou 512x512
3. Export as PNG

### Opção 3: Command Line (Inkscape)
```bash
# Se tiver Inkscape instalado
inkscape calculator-icon.svg --export-png=icon-192.png --export-width=192 --export-height=192
inkscape calculator-icon.svg --export-png=icon-512.png --export-width=512 --export-height=512
```

## 📱 PWA - Progressive Web App

Com os arquivos fornecidos, sua calculadora será:
- ✅ **Instalável** no mobile/desktop
- ✅ **Funciona offline** (Service Worker)
- ✅ **Ícone próprio** na tela inicial
- ✅ **Experiência nativa**

## 🔍 SEO Otimizado

- ✅ **Favicon** para aba do navegador
- ✅ **Open Graph** para redes sociais
- ✅ **Manifest** para PWA
- ✅ **Robots.txt** para indexação

## 🚀 Para Deploy Completo

Certifique-se que todos os arquivos estão presentes:
1. Gere os PNGs faltantes
2. Crie o favicon.ico
3. Opcionalmente, crie o preview social
4. Faça deploy da pasta `public/` junto com o build