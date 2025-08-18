import React, { useState, useEffect, useCallback } from 'react';
import { Calculator, History, Sun, Moon, Download, Copy } from 'lucide-react';
import * as math from 'mathjs';

// Tipos
interface HistoryEntry {
  expression: string;
  result: string;
  timestamp: Date;
}

interface MemoryState {
  value: number;
}

// Funções utilitárias
const formatNumber = (num: number): string => {
  if (isNaN(num) || !isFinite(num)) return 'Erro';
  if (Math.abs(num) > 1e15 || (Math.abs(num) < 1e-10 && num !== 0)) {
    return num.toExponential(6);
  }
  return parseFloat(num.toPrecision(12)).toString();
};

const safeEvaluate = (expression: string): number => {
  try {
    // Substitua símbolos comuns
    let expr = expression
      .replace(/×/g, '*')
      .replace(/÷/g, '/')
      .replace(/π/g, 'pi')
      .replace(/e/g, 'E')
      .replace(/√/g, 'sqrt');
    
    const result = math.evaluate(expr);
    return typeof result === 'number' ? result : NaN;
  } catch (error) {
    return NaN;
  }
};

// Componente principal da calculadora

const ScientificCalculator: React.FC = () => {
  const [display, setDisplay] = useState('0');
  const [expression, setExpression] = useState('');
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [memory, setMemory] = useState<MemoryState>({ value: 0 });
  const [isScientific, setIsScientific] = useState(true);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [showHistory, setShowHistory] = useState(false);

  // Manipulador de eventos de teclado

  const handleKeyPress = useCallback((event: KeyboardEvent) => {
    event.preventDefault();
    const key = event.key;
    
    if (key >= '0' && key <= '9' || key === '.') {
      handleNumberInput(key);
    } else if (['+', '-', '*', '/', '(', ')'].includes(key)) {
      handleOperatorInput(key === '*' ? '×' : key === '/' ? '÷' : key);
    } else if (key === 'Enter' || key === '=') {
      calculateResult();
    } else if (key === 'Escape') {
      clearAll();
    } else if (key === 'Backspace') {
      backspace();
    }
  }, []);

  useEffect(() => {
    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [handleKeyPress]);

  // Manipuladores de entrada

  const handleNumberInput = (num: string) => {
    if (display === '0' || display === 'Erro') {
      setDisplay(num);
      setExpression(num);
    } else {
      setDisplay(display + num);
      setExpression(expression + num);
    }
  };

  const handleOperatorInput = (operator: string) => {
    if (display === 'Erro') return;
    
    const newExpression = expression + operator;
    setExpression(newExpression);
    setDisplay(display + operator);
  };

  const calculateResult = () => {
    if (expression === '' || display === 'Erro') return;
    
    try {
      const result = safeEvaluate(expression);
      if (isNaN(result)) {
        setDisplay('Erro');
        return;
      }
      
      const formattedResult = formatNumber(result);
      setDisplay(formattedResult);
      
      // Adicionar ao histórico

      const historyEntry: HistoryEntry = {
        expression,
        result: formattedResult,
        timestamp: new Date()
      };
      setHistory(prev => [historyEntry, ...prev.slice(0, 49)]); // Keep last 50
      
      setExpression(formattedResult);
    } catch (error) {
      setDisplay('Erro');
    }
  };

  const clearAll = () => {
    setDisplay('0');
    setExpression('');
  };

  const backspace = () => {
    if (display.length <= 1 || display === 'Erro') {
      setDisplay('0');
      setExpression('');
    } else {
      const newDisplay = display.slice(0, -1);
      const newExpression = expression.slice(0, -1);
      setDisplay(newDisplay);
      setExpression(newExpression);
    }
  };

  // Funções científicas
  const handleFunction = (func: string) => {
    if (display === 'Erro') return;
    
    let newExpression = expression;
    
    switch (func) {
      case 'sin':
      case 'cos':
      case 'tan':
      case 'asin':
      case 'acos':
      case 'atan':
      case 'log':
      case 'ln':
      case 'sqrt':
        newExpression = expression + `${func}(`;
        break;
      case 'x²':
        newExpression = expression + '^2';
        break;
      case 'x³':
        newExpression = expression + '^3';
        break;
      case 'x^y':
        newExpression = expression + '^';
        break;
      case '!':
        const num = parseFloat(display);
        if (num >= 0 && num <= 170 && Number.isInteger(num)) {
          const factorial = math.factorial(num);
          setDisplay(formatNumber(factorial));
          setExpression(formatNumber(factorial));
          return;
        }
        break;
      case '±':
        if (expression && !isNaN(parseFloat(display))) {
          const negated = -parseFloat(display);
          setDisplay(formatNumber(negated));
          setExpression(formatNumber(negated));
          return;
        }
        break;
      case 'π':
        newExpression = expression + 'π';
        break;
      case 'e':
        newExpression = expression + 'e';
        break;
    }
    
    setExpression(newExpression);
    setDisplay(display + func);
  };

  // Funções de memória
  const memoryAdd = () => {
    const num = parseFloat(display);
    if (!isNaN(num)) {
      setMemory({ value: memory.value + num });
    }
  };

  const memorySubtract = () => {
    const num = parseFloat(display);
    if (!isNaN(num)) {
      setMemory({ value: memory.value - num });
    }
  };

  const memoryRecall = () => {
    setDisplay(formatNumber(memory.value));
    setExpression(formatNumber(memory.value));
  };

  const memoryClear = () => {
    setMemory({ value: 0 });
  };

  // Funções de histórico
  const exportHistory = () => {
    const content = history
      .map(entry => `${entry.expression} = ${entry.result} (${entry.timestamp.toLocaleString()})`)
      .join('\n');
    
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'calculadora-historico.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  const copyHistory = () => {
    const content = history
      .map(entry => `${entry.expression} = ${entry.result}`)
      .join('\n');
    navigator.clipboard.writeText(content);
  };

  const useHistoryEntry = (entry: HistoryEntry) => {
    setDisplay(entry.result);
    setExpression(entry.result);
    setShowHistory(false);
  };

  // Componente de botão
  const Button: React.FC<{
    children: React.ReactNode;
    onClick: () => void;
    className?: string;
    'aria-label'?: string;
  }> = ({ children, onClick, className = '', 'aria-label': ariaLabel }) => (
    <button
      onClick={onClick}
      className={`p-3 rounded-lg font-medium transition-all duration-200 hover:scale-105 active:scale-95 focus:outline-none focus:ring-2 focus:ring-blue-500 ${className}`}
      aria-label={ariaLabel}
    >
      {children}
    </button>
  );

  return (
    <div className={`min-h-screen transition-colors duration-300 ${isDarkMode ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-900'}`}>
      <div className="max-w-md mx-auto p-4">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Calculator className="w-6 h-6" />
            <h1 className="text-xl font-bold">Calculadora Científica</h1>
          </div>
          <div className="flex gap-2">
            <Button
              onClick={() => setShowHistory(!showHistory)}
              className={`p-2 ${isDarkMode ? 'bg-gray-700 hover:bg-gray-600' : 'bg-white hover:bg-gray-50'}`}
              aria-label="Mostrar histórico"
            >
              <History className="w-4 h-4" />
            </Button>
            <Button
              onClick={() => setIsDarkMode(!isDarkMode)}
              className={`p-2 ${isDarkMode ? 'bg-gray-700 hover:bg-gray-600' : 'bg-white hover:bg-gray-50'}`}
              aria-label="Alternar tema"
            >
              {isDarkMode ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
            </Button>
          </div>
        </div>

        {/* Display */}
        <div className={`p-4 rounded-lg mb-4 ${isDarkMode ? 'bg-gray-800' : 'bg-white'}`}>
          <div className="text-right">
            <div className="text-sm opacity-60 h-6 overflow-hidden">
              {expression}
            </div>
            <div className="text-3xl font-mono break-all" role="display" aria-live="polite">
              {display}
            </div>
          </div>
        </div>

        {/* Alternar modo */}
        <div className="flex mb-4">
          <Button
            onClick={() => setIsScientific(!isScientific)}
            className={`flex-1 ${isScientific 
              ? (isDarkMode ? 'bg-blue-600 hover:bg-blue-700' : 'bg-blue-500 hover:bg-blue-600 text-white')
              : (isDarkMode ? 'bg-gray-700 hover:bg-gray-600' : 'bg-gray-300 hover:bg-gray-400')
            }`}
          >
            {isScientific ? 'Modo Científico' : 'Modo Padrão'}
          </Button>
        </div>

        {/* Painel Histórico */}
        {showHistory && (
          <div className={`mb-4 p-4 rounded-lg ${isDarkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <div className="flex justify-between items-center mb-2">
              <h3 className="font-semibold">Histórico</h3>
              <div className="flex gap-2">
                <Button
                  onClick={copyHistory}
                  className={`p-1 text-xs ${isDarkMode ? 'bg-gray-700 hover:bg-gray-600' : 'bg-gray-200 hover:bg-gray-300'}`}
                  aria-label="Copiar histórico"
                >
                  <Copy className="w-3 h-3" />
                </Button>
                <Button
                  onClick={exportHistory}
                  className={`p-1 text-xs ${isDarkMode ? 'bg-gray-700 hover:bg-gray-600' : 'bg-gray-200 hover:bg-gray-300'}`}
                  aria-label="Exportar histórico"
                >
                  <Download className="w-3 h-3" />
                </Button>
              </div>
            </div>
            <div className="max-h-40 overflow-y-auto space-y-1">
              {history.length === 0 ? (
                <p className="text-sm opacity-60">Nenhum cálculo realizado</p>
              ) : (
                history.slice(0, 10).map((entry, index) => (
                  <div
                    key={index}
                    onClick={() => useHistoryEntry(entry)}
                    className={`text-xs p-2 rounded cursor-pointer transition-colors ${
                      isDarkMode ? 'hover:bg-gray-700' : 'hover:bg-gray-100'
                    }`}
                  >
                    <div className="font-mono">{entry.expression} = {entry.result}</div>
                  </div>
                ))
              )}
            </div>
          </div>
        )}

        {/* Botões da calculadora */}
        <div className="space-y-2">
          {/* Funções Científicas Linha 1 */}
          {isScientific && (
            <div className="grid grid-cols-5 gap-2">
              {['sin', 'cos', 'tan', 'ln', 'log'].map((func) => (
                <Button
                  key={func}
                  onClick={() => handleFunction(func)}
                  className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
                >
                  {func}
                </Button>
              ))}
            </div>
          )}

          {/* Funções Científicas Linha 2 */}
          {isScientific && (
            <div className="grid grid-cols-5 gap-2">
              {['asin', 'acos', 'atan', 'x²', 'x³'].map((func) => (
                <Button
                  key={func}
                  onClick={() => handleFunction(func)}
                  className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
                >
                  {func}
                </Button>
              ))}
            </div>
          )}

          {/* Funções Científicas Linha 3 */}
          {isScientific && (
            <div className="grid grid-cols-5 gap-2">
              <Button
                onClick={() => handleFunction('x^y')}
                className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
              >
                x^y
              </Button>
              <Button
                onClick={() => handleFunction('sqrt')}
                className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
              >
                √
              </Button>
              <Button
                onClick={() => handleFunction('!')}
                className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
              >
                n!
              </Button>
              <Button
                onClick={() => handleFunction('π')}
                className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
              >
                π
              </Button>
              <Button
                onClick={() => handleFunction('e')}
                className={`text-sm ${isDarkMode ? 'bg-purple-600 hover:bg-purple-700 text-white' : 'bg-purple-500 hover:bg-purple-600 text-white'}`}
              >
                e
              </Button>
            </div>
          )}

          {/* Funções de memória */}
          <div className="grid grid-cols-4 gap-2">
            <Button
              onClick={memoryClear}
              className={`text-sm ${isDarkMode ? 'bg-orange-600 hover:bg-orange-700 text-white' : 'bg-orange-500 hover:bg-orange-600 text-white'}`}
            >
              MC
            </Button>
            <Button
              onClick={memoryRecall}
              className={`text-sm ${isDarkMode ? 'bg-orange-600 hover:bg-orange-700 text-white' : 'bg-orange-500 hover:bg-orange-600 text-white'}`}
            >
              MR
            </Button>
            <Button
              onClick={memoryAdd}
              className={`text-sm ${isDarkMode ? 'bg-orange-600 hover:bg-orange-700 text-white' : 'bg-orange-500 hover:bg-orange-600 text-white'}`}
            >
              M+
            </Button>
            <Button
              onClick={memorySubtract}
              className={`text-sm ${isDarkMode ? 'bg-orange-600 hover:bg-orange-700 text-white' : 'bg-orange-500 hover:bg-orange-600 text-white'}`}
            >
              M-
            </Button>
          </div>

          {/* Grade principal da calculadora */}
          <div className="grid grid-cols-4 gap-2">
            {/* Linha 1 */}
            <Button
              onClick={clearAll}
              className={`${isDarkMode ? 'bg-red-600 hover:bg-red-700 text-white' : 'bg-red-500 hover:bg-red-600 text-white'}`}
            >
              C
            </Button>
            <Button
              onClick={backspace}
              className={`${isDarkMode ? 'bg-gray-600 hover:bg-gray-700 text-white' : 'bg-gray-400 hover:bg-gray-500 text-white'}`}
            >
              ⌫
            </Button>
            <Button
              onClick={() => handleFunction('±')}
              className={`${isDarkMode ? 'bg-gray-600 hover:bg-gray-700 text-white' : 'bg-gray-400 hover:bg-gray-500 text-white'}`}
            >
              ±
            </Button>
            <Button
              onClick={() => handleOperatorInput('÷')}
              className={`${isDarkMode ? 'bg-blue-600 hover:bg-blue-700 text-white' : 'bg-blue-500 hover:bg-blue-600 text-white'}`}
            >
              ÷
            </Button>

            {/* Linha 2 */}
            <Button
              onClick={() => handleNumberInput('7')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              7
            </Button>
            <Button
              onClick={() => handleNumberInput('8')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              8
            </Button>
            <Button
              onClick={() => handleNumberInput('9')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              9
            </Button>
            <Button
              onClick={() => handleOperatorInput('×')}
              className={`${isDarkMode ? 'bg-blue-600 hover:bg-blue-700 text-white' : 'bg-blue-500 hover:bg-blue-600 text-white'}`}
            >
              ×
            </Button>

            {/* Linha 3 */}
            <Button
              onClick={() => handleNumberInput('4')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              4
            </Button>
            <Button
              onClick={() => handleNumberInput('5')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              5
            </Button>
            <Button
              onClick={() => handleNumberInput('6')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              6
            </Button>
            <Button
              onClick={() => handleOperatorInput('-')}
              className={`${isDarkMode ? 'bg-blue-600 hover:bg-blue-700 text-white' : 'bg-blue-500 hover:bg-blue-600 text-white'}`}
            >
              -
            </Button>

            {/* Linha 4 */}
            <Button
              onClick={() => handleNumberInput('1')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              1
            </Button>
            <Button
              onClick={() => handleNumberInput('2')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              2
            </Button>
            <Button
              onClick={() => handleNumberInput('3')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              3
            </Button>
            <Button
              onClick={() => handleOperatorInput('+')}
              className={`${isDarkMode ? 'bg-blue-600 hover:bg-blue-700 text-white' : 'bg-blue-500 hover:bg-blue-600 text-white'}`}
            >
              +
            </Button>

            {/* Linha 5 */}
            <Button
              onClick={() => handleOperatorInput('(')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              (
            </Button>
            <Button
              onClick={() => handleNumberInput('0')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              0
            </Button>
            <Button
              onClick={() => handleOperatorInput(')')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              )
            </Button>
            <Button
              onClick={() => handleNumberInput('.')}
              className={`${isDarkMode ? 'bg-gray-700 hover:bg-gray-600 text-white' : 'bg-white hover:bg-gray-50'}`}
            >
              .
            </Button>
          </div>

          {/* Botão igual */}
          <Button
            onClick={calculateResult}
            className={`w-full ${isDarkMode ? 'bg-green-600 hover:bg-green-700 text-white' : 'bg-green-500 hover:bg-green-600 text-white'}`}
          >
            =
          </Button>
        </div>
      </div>
    </div>
  );
};

export default ScientificCalculator;