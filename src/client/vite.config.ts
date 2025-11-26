import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
    server: {
        port: 3000,
    },
    plugins: [react()],
    test: {
        environment: 'jsdom',
        globals: true, // Enables global access to Vitest APIs like `describe`, `it`, `expect`
        setupFiles: ['./src/test/setupTests.ts', './src/test/mocks.ts'],
    }
})
