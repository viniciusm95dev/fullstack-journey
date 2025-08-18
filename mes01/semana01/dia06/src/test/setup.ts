import { vi } from 'vitest';

import '@testing-library/jest-dom';

// Jogo simulador Média
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(), // deprecated
    removeListener: vi.fn(), // deprecated
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

// Observador de redimensionamento simulado
global.ResizeObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}));

// Observador de interseção simulado
global.IntersectionObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}));

// API de área de transferência simulada
Object.assign(navigator, {
  clipboard: {
    writeText: vi.fn().mockImplementation(() => Promise.resolve()),
    readText: vi.fn().mockImplementation(() => Promise.resolve('')),
  },
});

// Utilitários de teste globais
global.createMockCalculatorState = () => ({
  display: '0',
  expression: '',
  history: [],
  memory: { value: 0 },
  isScientific: true,
  isDarkMode: false,
  showHistory: false,
});