# SpeechSynthesis

This package is the only one that can convert speech to text in Node.js. I created it because the other options are either paid or not working. Give it a try and report any errors or correct the code.

## Requirements
- Python: Python must be installed on your system.

## Installation
```bash
npm i speechsynthesis
```

## Usage
```javascript
const { SpeechSynthesis } = require("speechsynthesis");
const speechSynthesis = new SpeechSynthesis();

speechSynthesis.listen().then((text) => {
  console.log(text);
});