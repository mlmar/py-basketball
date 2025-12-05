import { createContext, useContext } from 'react';
import { create, type StateCreator } from 'zustand';

type Provider = ({ children }: { children: React.ReactNode }) => React.ReactNode;

/**
 * Creates a store instance and context provider to access store instance
 * @param initializer -- zustand initializer for creating store
 * @returns [Provider, UseStore]
 */
export function createStoreInstance<T>(initializer: StateCreator<T, [], []>): [Provider, typeof useStoreInstance] {
    // Create single store instance
    const useStoreInstance = create<T>(initializer);

    const StoreContext = createContext<typeof useStoreInstance | null>(null);

    // Accesses the store instance hook from provider
    const useStore: typeof useStoreInstance = function (selector) {
        const useProviderStore = useContext(StoreContext);
        if (!useProviderStore) {
            throw Error('Missing StoreContext.Provider parent');
        }
        return useProviderStore(selector);
    } as typeof useStoreInstance;

    // Store provider to propagate store instance hook
    function Provider({ children }: { children: React.ReactNode }) {
        return <StoreContext.Provider value={useStoreInstance}> {children} </StoreContext.Provider>;
    }

    return [Provider, useStore];
}
