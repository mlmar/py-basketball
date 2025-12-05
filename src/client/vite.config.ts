import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tanstackRouter from '@tanstack/router-plugin/vite';
import path from 'path';
// @ts-ignore
import eslint from 'vite-plugin-eslint';

// https://vite.dev/config/
export default defineConfig({
    server: {
        port: 3000,
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
        },
    },
    plugins: [
        tanstackRouter({
            target: 'react',
            autoCodeSplitting: true,
        }),
        react(),
        eslint()
    ],
    test: {
        environment: 'jsdom',
        globals: true, // Enables global access to Vitest APIs like `describe`, `it`, `expect`
        setupFiles: ['./src/test/setupTests.ts', './src/test/mocks.ts'],
    }
})
