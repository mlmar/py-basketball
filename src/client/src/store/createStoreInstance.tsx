import { createContext, useContext } from 'react';
import { create, type StateCreator, type StoreApi, type UseBoundStore } from 'zustand';

type Provider = ({ children }: { children: React.ReactNode }) => React.ReactNode;
type UseStore<T> = (selector: (state: T) => unknown) => Partial<T>;

/**
 * Creates a store instance and context provider to access store instance
 * @param initializer -- zustand initializer for creating store
 * @returns [Provider, UseStore]
 */
export function createStoreInstance<T>(initializer: StateCreator<T, [], []>): [Provider, UseStore<T>] {
    const StoreContext = createContext<UseBoundStore<StoreApi<T>> | null>(null);

    // Create single store instance
    const useStoreInstance = create<T>(initializer);

    // Accesses the store instance hook from provider
    function useStore(selector: (state: T) => unknown): Partial<T> {
        const useStore = useContext(StoreContext);
        if (!useStore) {
            throw Error('Missing StoreContext.Provider parent');
        }
        return useStore(selector) as Partial<T>;
    }

    // Store provider to propagate store instance hook
    function Provider({ children }: { children: React.ReactNode }) {
        return <StoreContext.Provider value={useStoreInstance}> {children} </StoreContext.Provider>;
    }

    return [Provider, useStore];
}
