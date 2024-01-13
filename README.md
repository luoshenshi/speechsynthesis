# SpeechSynthesis

This package is the only one that can convert speech to text in Node.js for free. I created it because the other options are either paid or not functional. Give it a try and report any errors or correct the code.

## Requirements

- Python: Python must be installed on your system.

## Installation

```bash
npm i @luoshenshi/speechsynthesis
```

## Usage

```javascript
const { SpeechSynthesis } = require("@luoshenshi/speechsynthesis");
const speech = new SpeechSynthesis("en");

(async () => {
  try {
    await speech.onReady();
    console.log("Listening...");
    const text = await speech.listen();
    console.log(text);
  } catch (err) {
    console.log(err.message);
  }
})();
```

**If you are running it for the first time, you might see**

```
Collecting PyAudio
```

**This is just installing the required Python packages. Run it again and enjoy!**
