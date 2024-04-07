import * as readline from "readline";
import { AnaliysisFile } from "./AnalysisFile";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const getInput = () =>
  rl.question("", (userInput: string) => {
    rl.close();
    let analiysis = new AnaliysisFile(userInput);
    analiysis.readDataAndSplit();
    analiysis.saveToJson();
  });

getInput();
