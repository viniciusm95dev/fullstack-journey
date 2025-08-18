export {};

declare global {
  var createMockCalculatorState: () => {
    display: string;
    expression: string;
    history: any[];
    memory: { value: number };
    isScientific: boolean;
    isDarkMode: boolean;
    showHistory: boolean;
  };
}
