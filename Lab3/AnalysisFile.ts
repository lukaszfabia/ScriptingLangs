import * as path from "path";

export class AnaliysisFile {
  private fileName: string;
  private data: Array<string> = [];

  constructor(fileName: string) {
    this.fileName = fileName;
  }

  public readDataAndSplit(): void {
    const fs = require("fs");
    this.data = fs.readFileSync(this.fileName, "utf8").split("\n");
  }

  private get getFilePath(): string {
    return path.join(__dirname, this.fileName);
  }

  private getWords(): Array<string> {
    return this.data.map((line) => line.split(" ")).flat();
  }

  private get getNumberOfCharsAndWords(): [number, number] {
    const words = this.getWords();
    const chars = words.reduce((acc, curr) => acc + curr.length, 0);
    const wordsCount = words.length;

    return [chars, wordsCount];
  }

  private get mostCommonWord(): [string, number] {
    let mapWords = this.countKeyInMap(this.getWords());

    return this.findMax(mapWords);
  }

  private get mostCommonLetter(): [string, number] {
    let chars = this.getWords()
      .map((word) => word.split(""))
      .flat();

    const mapChar = this.countKeyInMap(chars);
    return this.findMax(mapChar);
  }

  private countKeyInMap(list: string[]): Map<string, number> {
    let map = new Map<string, number>();
    list.forEach((element) => {
      map.set(element, (map.get(element) || 0) + 1);
    });
    return map;
  }

  private findMax(map: Map<string, number>): [string, number] {
    const max = Math.max(...Array.from(map.values()));
    for (let [key, value] of map) {
      if (value === max) {
        return [key, value];
      }
    }
    return ["", 0];
  }

  public saveToJson(): void {
    const fs = require("fs");
    fs.writeFileSync("result.json", this.createJson());
  }

  private get getNumberOfLines(): number {
    return this.data.length;
  }

  private createJson(): string {
    const data = {
      "file path": this.getFilePath,
      "number of lines": this.getNumberOfLines,
      "number of chars": this.getNumberOfCharsAndWords[0],
      "number words": this.getNumberOfCharsAndWords[1],
      "most common word": this.mostCommonWord,
      "most common letter": this.mostCommonLetter,
    };

    return JSON.stringify(data);
  }
}
