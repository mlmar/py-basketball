import './App.less';
import { createRouter, RouterProvider } from '@tanstack/react-router';
import { routeTree } from './routeTree.gen';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { GlobalStoreProvider } from '@/store/useGlobalStore';

// Create a new router instance
const router = createRouter({ routeTree, scrollRestoration: false });

// Register the router instance for type safety
declare module '@tanstack/react-router' {
    interface Register {
        router: typeof router;
    }
}

// Query client instance
const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            staleTime: Infinity,
            refetchOnMount: false,
            retry: false
        }
    }
});

/**
 * Base app component for providers
 *  -   All routes should be placed in the src/routes folder
 *  -   All UI should be placed in the src/components (Base components) and src/features (Pages) folders
 */
function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <GlobalStoreProvider>
                <RouterProvider router={router} />
            </GlobalStoreProvider>
        </QueryClientProvider>
    );
}

export default App;
