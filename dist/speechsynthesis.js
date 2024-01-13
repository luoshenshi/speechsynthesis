const { spawn } = require("child_process");
let pythonProcess;
class SpeechSynthesis {
  #languageCode;

  constructor(languageCode) {
    this.#languageCode = languageCode;
  }

  listen() {
    return new Promise((resolve, reject) => {
      if (!pythonProcess) {
        pythonProcess = spawn("python", [
          __dirname.replace("dist", "synthesis\\") + "main.py",
          this.#languageCode,
        ]);
      }

      let output = "";
      let error = "";

      pythonProcess.stdout.on("data", (data) => {
        if (data.toString().trim() === "UnknownValueError") {
          reject(new Error("Apologies, the audio wasn't clear enough."));
        }
        if (data.toString().includes("readyCode1")) {
          data = data.toString().replace("readyCode1", "");
        }
        output += data.toString().trim();
      });

      pythonProcess.stderr.on("data", (data) => {
        error += data;
      });

      pythonProcess.on("close", (code) => {
        if (code === 0) {
          resolve(output);
        } else {
          reject(new Error(error));
        }
      });
    });
  }

  onReady() {
    return new Promise((resolve, reject) => {
      if (!pythonProcess) {
        pythonProcess = spawn("python", [
          __dirname.replace("dist", "synthesis\\") + "main.py",
          this.#languageCode,
        ]);
      }

      pythonProcess.stdout.once("data", (data) => {
        let output = data.toString();
        if (output.includes("readyCode1")) {
          resolve();
        } else {
          console.log(output.trim());
        }
      });

      pythonProcess.on("close", (code) => {
        if (code !== 0) {
          reject(new Error(`Python process exited with code ${code}`));
        }
      });
    });
  }
}

module.exports = { SpeechSynthesis };
